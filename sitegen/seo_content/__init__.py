"""All SEO landing pages, one module per cluster. Order here = order of hub cards."""
from . import apps, cities, core, devices, fr, international, sports

ALL = core.PAGES + apps.PAGES + devices.PAGES + sports.PAGES + cities.PAGES + international.PAGES + fr.PAGES
