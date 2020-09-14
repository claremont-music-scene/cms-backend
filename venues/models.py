from django.db import models


def venue_media_path(instance, filename):
    return f"venues/{instance.slug}/{filename}"


class Venue(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    is_public = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=venue_media_path, blank=True, null=True)

    address_street = models.CharField(max_length=128, blank=True, null=True)
    address_city = models.CharField(max_length=64, blank=True, null=True)
    address_full = models.CharField(max_length=256, blank=True, null=True)

    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    phone = models.CharField(blank=True, max_length=30)
    email = models.EmailField(blank=True)
    calendar_url = models.URLField(blank=True)

    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()

    def get_absolute_url(self):
        return reverse("venue-detail", kwargs={"slug": self.slug})

    @property
    def formatted_address(self):
        return f"{self.name}, {self.address.formatted}"

    def upcoming_events(self):
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        recurring_events_here = self.recurringevent_set.all()
        event_instances = self.event_set.filter(begin__gte=now)
        event_ids = [e.uid for e in event_instances]
        events_list = []

        for recurring in recurring_events_here:
            recur_insts = get_recurring_instances(recurring.uid)

            for inst in recur_insts:
                if inst["id"] in event_ids:
                    continue
                event = RecurringEvent(
                    uid=inst["recurringEventId"],
                    begin=parser.parse(inst["start"]["dateTime"]),
                    end=parser.parse(inst["end"]["dateTime"]),
                    title=inst["summary"],
                    slug=slugify(inst["summary"]),
                )
                setattr(event, "detail_url", event.get_detail_url(inst["id"]))
                if "description" in inst:
                    event.description = inst["description"]
                events_list.append((event.begin, event))

        events_list.extend([(e.begin, e) for e in event_instances])
        events_list = sorted(events_list, key=lambda x: x[0])
        return [e[1] for e in events_list]
