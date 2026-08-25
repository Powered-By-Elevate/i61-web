# Shiloh Collective — website

Seven static pages, no build step, no dependencies. Open `index.html` or run
`python3 -m http.server` in this directory. `python3 build.py` regenerates everything —
copy, structure and styling all live in `build.py` as literals.

## Framing (settled 2026-08-24)

**Shiloh is a bookable event venue whose bookings fund the mission** — Matt's direction, and the
same model as the reference. IA mapped from `socialhouseroswell.com` (five tabs, no dropdowns,
no parallax, restraint as the craft), extended by two pages the reference doesn't need:

| Page | Role |
|---|---|
| `index.html` | Hero → gallery → feature blocks → mission band → build status → CTA |
| `mission.html` | The mentorship work, Jeff & Amy Lyle / Transforming Truth, the i61 relationship |
| `gather.html` | Event types: weddings, offsites, church/community, classes |
| `build.html` | Phase-by-phase renovation progress — the page people return for |
| `visit.html` | Location facts (street address withheld until Phase 3) |
| `book.html` | Enquiry form — **the conversion page** (nav CTA) |
| `give.html` | Giving routes (footer-linked; secondary conversion) |

## Photos — TEMPORARY

All images are **Creative Commons stock via Openverse**, chosen as stand-ins and each one
looked at before use (first fetch produced a bathroom labelled "renovation" — visual grading is
not optional). **Attribution required and recorded: `assets/stock/CREDITS.md`**, linked from the
footer. Replace every one with Shiloh's own photography before launch; the credits link comes out
only when the last CC image does.

## Before launch

1. **Real photography** — the only thing between this and finished.
2. `book.html` form → real endpoint (Formspree or similar); `hello@shilohcollective.org` is a
   placeholder; pricing/capacity need Jeff and Amy's numbers.
3. `build.html` phase notes → Jeff's live updates, real Phase 3 target date.
4. **Giving legal wording** — confirm entity + status in writing; nothing claims tax-deductibility.
   i61's determination is pending and the two entities must not be conflated.
5. Street address + map on `visit.html` once public.
6. Platform call: keep static, or port to Squarespace if Amy/Tracy must self-edit.

Facts sourced from `jefflyle.com/shiloh-collective`, paraphrased — none of the reference site's
copy or photography is used anywhere.
