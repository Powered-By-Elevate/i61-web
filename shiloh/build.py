#!/usr/bin/env python3
"""Shiloh Collective — bookable event venue + mission, IA mapped from socialhouseroswell.com.
Six pages. Photos are TEMPORARY CC stock (see assets/stock/CREDITS.md) until Shiloh's own
photography exists. Facts from jefflyle.com/shiloh-collective, paraphrased."""
import os, shutil

INK, GOLD, CREAM, PAPER = '#131315', '#C6A670', '#F4EFE6', '#FBF9F5'
STONE, LINE, DEEP = '#8A8378', '#DED8CC', '#1E1D1C'
NAV = [('Home','index.html'), ('Mission','mission.html'), ('Gather','gather.html'),
       ('The Build','build.html'), ('Visit','visit.html'), ('Book Now','book.html')]

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}} html{{scroll-behavior:smooth}}
body{{background:{PAPER};color:{INK};font-family:Georgia,'Times New Roman',serif;
 font-size:18px;line-height:1.7;-webkit-font-smoothing:antialiased}}
a{{color:inherit}} .wrap{{max-width:1180px;margin:0 auto;padding:0 32px}}
.narrow{{max-width:760px;margin:0 auto}}
header{{position:sticky;top:0;z-index:50;background:rgba(251,249,245,.94);
 backdrop-filter:saturate(1.2) blur(8px);border-bottom:1px solid {LINE}}}
.bar{{display:flex;align-items:center;justify-content:space-between;height:86px}}
.brand{{display:flex;align-items:center;gap:14px;text-decoration:none}}
.brand img{{width:46px;height:46px;display:block}}
.brand b{{font-family:Helvetica,Arial,sans-serif;font-size:15px;letter-spacing:.18em;
 text-transform:uppercase;font-weight:700}}
nav ul{{display:flex;gap:30px;list-style:none;align-items:center}}
nav a{{font-family:Helvetica,Arial,sans-serif;font-size:12.5px;letter-spacing:.16em;
 text-transform:uppercase;text-decoration:none;color:{STONE};padding-bottom:3px;
 border-bottom:1px solid transparent;transition:color .18s,border-color .18s}}
nav a:hover,nav a.on{{color:{INK};border-color:{GOLD}}}
nav a.cta{{background:{INK};color:{CREAM};padding:12px 22px;border:0;letter-spacing:.14em}}
nav a.cta:hover{{background:{GOLD};color:{INK}}}
.menu{{display:none;font-size:24px;background:none;border:0;cursor:pointer}}
.hero{{position:relative;background:{DEEP};color:{CREAM};min-height:74vh;display:flex;align-items:center;
 background-size:cover;background-position:center}}
.hero .wrap{{padding:100px 32px;position:relative;z-index:2}}
.hero.dim::before{{content:"";position:absolute;inset:0;
 background:linear-gradient(100deg,rgba(15,14,13,.82) 34%,rgba(15,14,13,.38) 75%,rgba(15,14,13,.55))}}
.hero h1{{font-size:clamp(33px,4.5vw,60px);line-height:1.16;font-weight:400;max-width:17ch}}
.hero p{{margin-top:26px;max-width:54ch;font-size:20px;color:#EDE7DA}}
.kick{{font-family:Helvetica,Arial,sans-serif;font-size:12px;letter-spacing:.28em;
 text-transform:uppercase;color:{GOLD};margin-bottom:22px}}
.rule{{width:88px;height:2px;background:{GOLD};margin:30px 0}}
.btn{{display:inline-block;font-family:Helvetica,Arial,sans-serif;font-size:12.5px;
 letter-spacing:.16em;text-transform:uppercase;text-decoration:none;padding:17px 34px;
 background:{GOLD};color:{INK};transition:background .18s,color .18s;border:0;cursor:pointer}}
.btn:hover{{background:{CREAM}}}
.btn.ghost{{background:transparent;color:{CREAM};box-shadow:inset 0 0 0 1px rgba(244,239,230,.5)}}
.btn.ghost:hover{{background:{CREAM};color:{INK};box-shadow:none}}
.btn.dark{{background:{INK};color:{CREAM}}} .btn.dark:hover{{background:{GOLD};color:{INK}}}
section{{padding:104px 0}} section.tight{{padding:70px 0}}
.eyebrow{{font-family:Helvetica,Arial,sans-serif;font-size:12px;letter-spacing:.26em;
 text-transform:uppercase;color:{STONE};margin-bottom:18px}}
h2{{font-size:clamp(27px,3vw,40px);line-height:1.24;font-weight:400;max-width:21ch}}
h3{{font-family:Helvetica,Arial,sans-serif;font-size:15px;letter-spacing:.13em;
 text-transform:uppercase;font-weight:700;margin-bottom:12px}}
.lede{{font-size:21px;line-height:1.62;max-width:60ch;color:#3A362F}}
p+p{{margin-top:18px}}
.ph{{overflow:hidden;background:#E8E2D6;border:1px solid {LINE}}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block}}
.ph.tall{{aspect-ratio:3/4}} .ph.wide{{aspect-ratio:16/9}} .ph.sq{{aspect-ratio:1/1}}
.slot{{background:repeating-linear-gradient(45deg,#EFEAE0 0 12px,#EBE5D9 12px 24px);
 border:1px solid {LINE};display:flex;align-items:center;justify-content:center;
 text-align:center;padding:26px}}
.slot span{{font-family:Helvetica,Arial,sans-serif;font-size:11px;letter-spacing:.2em;
 text-transform:uppercase;color:{STONE};max-width:28ch;line-height:1.9}}
.slot.sq{{aspect-ratio:1/1}}
.gal{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}
.gal .ph:first-child{{grid-column:span 2;grid-row:span 2}}
.feat{{display:grid;grid-template-columns:repeat(3,1fr);gap:50px 44px;margin-top:56px}}
.feat.two{{grid-template-columns:repeat(2,1fr);gap:52px}}
.feat p{{font-size:17px;color:#3A362F}}
.band{{background:{DEEP};color:{CREAM};text-align:center}}
.band h2{{margin:0 auto;max-width:23ch}} .band p{{color:#E4DDD0;max-width:56ch;margin:20px auto 0}}
.split{{display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center}}
.stack>*+*{{margin-top:22px}}
.facts{{list-style:none;margin-top:30px}}
.facts li{{display:flex;gap:18px;padding:15px 0;border-top:1px solid {LINE};font-size:17px}}
.facts b{{font-family:Helvetica,Arial,sans-serif;font-size:11.5px;letter-spacing:.16em;
 text-transform:uppercase;color:{STONE};min-width:136px;padding-top:3px}}
.phase{{display:flex;gap:26px;padding:26px 0;border-top:1px solid {LINE};align-items:baseline}}
.phase .n{{font-family:Helvetica,Arial,sans-serif;font-size:12px;letter-spacing:.2em;
 text-transform:uppercase;color:{GOLD};min-width:96px}}
.note{{background:{CREAM};border-left:3px solid {GOLD};padding:26px 30px;margin-top:44px}}
.note p{{font-size:15.5px;line-height:1.85;color:#3A362F}}
form.book{{margin-top:44px;display:grid;grid-template-columns:1fr 1fr;gap:22px}}
form.book label{{font-family:Helvetica,Arial,sans-serif;font-size:11.5px;letter-spacing:.16em;
 text-transform:uppercase;color:{STONE};display:block;margin-bottom:9px}}
form.book input,form.book select,form.book textarea{{width:100%;padding:14px 16px;
 border:1px solid {LINE};background:#fff;font-family:Georgia,serif;font-size:16.5px;color:{INK}}}
form.book .full{{grid-column:1/-1}}
.stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:50px}}
.stat{{background:{CREAM};border-top:3px solid {GOLD};padding:30px 26px}}
.stat b{{font-size:40px;display:block;line-height:1.1;font-weight:400}}
.stat span{{font-family:Helvetica,Arial,sans-serif;font-size:12px;letter-spacing:.14em;
 text-transform:uppercase;color:{STONE};display:block;margin-top:12px;line-height:1.8}}
.team{{display:grid;grid-template-columns:repeat(4,1fr);gap:26px;margin-top:50px}}
.team figcaption{{margin-top:14px}}
.team b{{font-family:Helvetica,Arial,sans-serif;font-size:13px;letter-spacing:.1em;
 text-transform:uppercase}}
.team span{{display:block;font-family:Helvetica,Arial,sans-serif;font-size:11.5px;
 letter-spacing:.12em;text-transform:uppercase;color:{STONE};margin-top:5px}}
.tiles{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:44px}}
.tile{{border:1px solid {LINE};padding:30px 20px;text-align:center;
 font-family:Helvetica,Arial,sans-serif;font-size:12px;letter-spacing:.14em;
 text-transform:uppercase;color:{STONE};line-height:1.9}}
.vrow{{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;padding:38px 0}}
.vrow:nth-child(even) .txt{{order:2}}
.steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:44px;margin-top:50px}}
.steps .n{{font-family:Helvetica,Arial,sans-serif;font-size:13px;letter-spacing:.2em;
 color:{GOLD};display:block;margin-bottom:14px}}
.checks{{list-style:none;margin-top:36px;columns:2;column-gap:56px}}
.checks li{{padding:11px 0 11px 30px;position:relative;font-size:17.5px;break-inside:avoid}}
.checks li::before{{content:"";position:absolute;left:0;top:20px;width:12px;height:12px;
 background:{GOLD}}}
footer{{background:{INK};color:#A9A296;padding:72px 0 44px;font-family:Helvetica,Arial,sans-serif;
 font-size:13.5px}}
footer a{{color:{CREAM};text-decoration:none}} footer a:hover{{color:{GOLD}}}
.fgrid{{display:grid;grid-template-columns:2fr 1fr 1fr;gap:44px}}
.fbrand{{display:flex;align-items:center;gap:14px;margin-bottom:18px}}
.fbrand img{{width:52px;height:52px}}
.fbrand b{{color:{CREAM};font-size:14px;letter-spacing:.18em;text-transform:uppercase}}
.flist{{list-style:none}} .flist li{{margin-top:11px}}
.fh{{color:{CREAM};letter-spacing:.16em;font-size:11.5px;text-transform:uppercase}}
.fbot{{margin-top:52px;padding-top:24px;border-top:1px solid #2C2A28;display:flex;
 justify-content:space-between;gap:20px;flex-wrap:wrap;font-size:12px;color:#7C766C}}
@media(max-width:900px){{
 .split,.feat,.feat.two,.fgrid,form.book,.stats,.steps,.vrow{{grid-template-columns:1fr;gap:34px}}
 .team,.tiles{{grid-template-columns:repeat(2,1fr)}} .checks{{columns:1}}
 .vrow:nth-child(even) .txt{{order:0}}
 .gal{{grid-template-columns:repeat(2,1fr)}}
 .gal .ph:first-child{{grid-column:span 2;grid-row:auto;aspect-ratio:16/9}}
 nav ul{{display:none}} .menu{{display:block}} section{{padding:70px 0}}
}}"""

def nav_html(active):
    out=[]
    for t,h in NAV:
        cls='cta' if t=='Book Now' else ('on' if h==active else '')
        attr = f' class="{cls}"' if cls else ''
        out.append(f'<li><a href="{h}"{attr}>{t}</a></li>')
    return ''.join(out)

def ph(img, alt, cls='wide'):
    return f'<div class="ph {cls}"><img src="assets/stock/{img}" alt="{alt}" loading="lazy"></div>'

def page(title, active, body, desc):
    flinks=''.join(f'<li><a href="{h}">{t}</a></li>' for t,h in NAV)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Shiloh Collective</title><meta name="description" content="{desc}">
<style>{CSS}</style></head><body>
<header><div class="wrap bar">
<a class="brand" href="index.html"><img src="assets/seal.png" alt=""><b>Shiloh Collective</b></a>
<nav><ul>{nav_html(active)}</ul></nav><button class="menu" aria-label="Menu">&#9776;</button>
</div></header>
{body}
<footer><div class="wrap"><div class="fgrid">
<div><div class="fbrand"><img src="assets/seal.png" alt=""><b>Shiloh Collective</b></div>
<p style="max-width:40ch;line-height:1.8">An event venue and equipping centre for young adults in
Dawsonville, Georgia — where every booking funds the mission. A work of Transforming Truth
Ministries, supported by Project i61.</p></div>
<div><b class="fh">Pages</b><ul class="flist">{flinks}<li><a href="give.html">Give</a></li></ul></div>
<div><b class="fh">Contact</b><ul class="flist">
<li><a href="tel:+16782766486">(678) 276-6486</a></li>
<li>PO Box 277<br>Dawsonville, GA 30534</li></ul></div>
</div><div class="fbot">
<span>&copy; 2026 Shiloh Collective &middot; Transforming Truth Ministries &middot;
<a href="assets/stock/CREDITS.md" style="color:#7C766C">temporary photo credits</a></span>
<span style="letter-spacing:.2em;text-transform:uppercase">Built to Lift</span></div>
</div></footer></body></html>"""

FEATURES = [
 ("A room that changes shape","Open plan and movable furniture — a class of twelve in the morning, a supper for a hundred that night."),
 ("Everything already here","Tables, chairs and settings included. Nobody arrives with a van full of gear."),
 ("Easy catering access","Bring your caterer or bring the food; the layout makes either simple."),
 ("Indoors and out","Covered space and open ground, so a gathering is not trapped by weather or walls."),
 ("Made for teaching","Screens, sound and sightlines that let the person at the front actually be heard."),
 ("A venue with purpose","Every booking funds the mentorship work that happens here the rest of the week."),
]
USES = [
 ("Weddings & receptions","Warm timber, long tables and evening light — and a team that treats your day as the point, not an interruption."),
 ("Company offsites & retreats","Daylight, screens and sound, with lunch made simple."),
 ("Church & community","Overflow services, midweek teaching, funerals and the meals that follow them."),
 ("Classes & cohorts","The layout this building was designed around — small groups, long tables, someone teaching."),
]
PHASES = [
 ("Phase 1","Complete","Shell, structure and the decisions that could not be undone later."),
 ("Phase 2","Nearing completion — August 2026","The bulk of the interior renovation, with a target date now set."),
 ("Phase 3","Scoped, needs identified","The remaining fit-out. Costs are known; funding sets the date."),
]
WAYS = [
 ("By phone","Call (678) 276-6486 and give directly."),
 ("CashApp","$TransformingTruth"),
 ("By mail","Transforming Truth Ministries, PO Box 277, Dawsonville, GA 30534"),
 ("Materials or trade","Timber, fixtures, or a week of skilled labour. Much of this building arrived that way."),
]

home = f"""
<div class="hero dim" style="background-image:url('assets/stock/gal1.jpg')"><div class="wrap">
<div class="kick">Dawsonville, Georgia</div>
<h1>A venue where every gathering funds the work.</h1>
<p>Shiloh Collective is an event space and a mentorship centre in one building — book it for a
wedding, an offsite or a supper, and the booking pays for the week that follows.</p>
<div class="rule"></div>
<a class="btn" href="book.html">Book Your Event</a>
<a class="btn ghost" href="gather.html" style="margin-left:12px">See the Space</a>
</div></div>

<section class="tight"><div class="wrap"><div class="gal">
{ph('gal3.jpg','Interior with brick and steel','')}
{ph('gal2.jpg','Long tables set for dinner','sq')}
{ph('gal4.jpg','Hands at work in the wood shop','sq')}
{ph('gal5.jpg','String lights at night','sq')}
{ph('givehero.jpg','A community dinner','sq')}
</div></div></section>

<section><div class="wrap">
<div class="eyebrow">What the building does</div>
<h2>Built plainly, so it can be used hard.</h2>
<div class="feat">{''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t,d in FEATURES)}</div>
</div></section>

<section class="band"><div class="wrap">
<div class="eyebrow" style="color:{GOLD}">Why it exists</div>
<h2>Small, strong and local beats large and far away.</h2>
<p>Shiloh is one equipping station, in one town, for the young adults already in it. The venue is
how it pays its own way.</p>
<div style="margin-top:34px"><a class="btn" href="mission.html">Read the Mission</a></div>
</div></section>

<section><div class="wrap split">
<div class="stack">
<div class="eyebrow">Where it stands</div>
<h2>Phase 2 is nearly finished.</h2>
<p class="lede">The building is a 2,800 square foot warehouse, renovated in stages — each one paid
for before it begins. Phase 3 is scoped; funding sets its date.</p>
<div style="margin-top:14px"><a class="btn dark" href="build.html">Follow the Build</a></div>
</div>
{ph('buildwide.jpg','Framing under construction','tall')}
</div></section>

<section class="tight"><div class="wrap" style="text-align:center">
<h2 style="margin:0 auto">Ready to see it?</h2>
<div style="margin-top:30px"><a class="btn dark" href="book.html">Book Your Event</a></div>
</div></section>
"""

TEAM = [
 ("Jeff Lyle","Founder & Teacher"),
 ("Amy Lyle","Co-founder & Hospitality"),
 ("Mark Samples","Build & Operations"),
 ("Deborah","Intercession & Care"),
]

mission = f"""
<section><div class="wrap narrow">
<div class="eyebrow">Our mission</div>
<h2 style="max-width:24ch">Where gathering builds people.</h2>
<div class="rule"></div>
<p class="lede">When you book Shiloh Collective for a wedding, an offsite or a supper, the room
does not pocket the money. It spends it on the week that follows — mentoring young adults,
spiritually and practically, in the same building you celebrated in.</p>
<p>That is the whole model. There is no separate fundraising arm and no gala season. The venue is
how the mission pays its own way.</p>
</div></section>

<section class="tight"><div class="wrap">
<div class="eyebrow">The problem we work on</div>
<h2 style="max-width:26ch">Young adults are leaving small towns unanchored — or staying in them
adrift.</h2>
<p class="lede" style="margin-top:22px">Not for lack of talent. For lack of people close enough
to teach a trade, a habit and a faith at the same table. Shiloh exists to be that table.</p>
<div class="stats">
<div class="stat"><b>2,800</b><span>square feet of warehouse, renovated by hand</span></div>
<div class="stat"><b>3</b><span>phases — each paid for before its work begins</span></div>
<div class="stat"><b>$0</b><span>debt on the building, by design</span></div>
</div>
<div class="note"><p><b>Before launch:</b> the reference page leads with three hard statistics
about its cause. When Jeff has real numbers on the young adults this work serves — cohort size,
completions, placements — they belong in these boxes. Until then the boxes carry build facts,
because we do not invent statistics.</p></div>
</div></section>

<section><div class="wrap split">
<div class="stack">
<div class="eyebrow">What changes with mentorship</div>
<h2>Sent, not just launched.</h2>
<p>A young adult with no one close by learns by trial, mostly error, and often leaves. One who is
known — taught a trade, fed weekly, corrected kindly, prayed for by name — tends to stay, build
and bring the next one along. We have watched both happen. The difference is not talent. It is
proximity.</p>
</div>
{ph('gal4.jpg','A trade taught by hand','tall')}
</div></section>

<section class="band"><div class="wrap">
<div class="eyebrow" style="color:{GOLD}">The name</div>
<h2>&ldquo;&hellip; that they may be called oaks of righteousness, the planting of the
Lord.&rdquo;</h2>
<p>Isaiah 61 is where this work gets its name and its method: rebuild the ruined places, and do
it by raising up the people who live there.</p>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Who is behind this</div>
<h2>A ministry, and the mechanism alongside it.</h2>
<div class="feat two" style="margin-top:44px">
<div><h3>Transforming Truth Ministries</h3><p>Jeff and Amy Lyle's teaching ministry, and the
hands running Shiloh day to day. The building, the mentoring and the meals are theirs to
steward.</p></div>
<div><h3>Project i61</h3><p>An equipping mechanism for small, strong local initiatives — built on
relationships rather than programmes. i61 does not run Shiloh. It comes alongside the people who
do, and Shiloh is its first connection project.</p></div>
</div>
</div></section>

<section class="tight"><div class="wrap">
<div class="eyebrow">The people</div>
<h2>Small team. Long obedience.</h2>
<div class="team">
{''.join(f'<figure><div class="slot tall"><span>Portrait — {n}</span></div>'
         f'<figcaption><b>{n}</b><span>{r}</span></figcaption></figure>' for n,r in TEAM)}
</div>
<div class="note"><p><b>Before launch:</b> confirm names, roles and headshots with Jeff — this
list is drawn from the current Shiloh page and needs his sign-off.</p></div>
</div></section>

<section class="band"><div class="wrap">
<h2>Book the room. Fund the work.</h2>
<p>Or come and see it first — the walkthrough is the best argument we have.</p>
<div style="margin-top:34px"><a class="btn" href="book.html">Book Your Event</a>
<a class="btn ghost" href="give.html" style="margin-left:12px">Give Directly</a></div>
</div></section>
"""

gather = f"""
<div class="hero dim" style="min-height:56vh;background-image:url('assets/stock/gal1.jpg')"><div class="wrap">
<div class="kick">Gather</div>
<h1 style="font-size:clamp(30px,4vw,52px)">A warehouse with warmth, in the North Georgia
foothills.</h1>
<p>Timber, light and an open floor that takes your vision rather than imposing ours — minutes
from downtown Dawsonville.</p>
</div></div>

<section class="tight"><div class="wrap narrow" style="text-align:center">
<p class="lede" style="margin:0 auto">No ballroom carpet. No banquet-hall sameness. No venue
manager watching the clock. And no invoice that vanishes into a company — every booking funds
the mentoring work this building exists for.</p>
<div style="margin-top:34px"><a class="btn dark" href="book.html">Check a Date</a></div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">What sets Shiloh apart</div>
<div class="vrow"><div class="txt">
<h3>Inside and out, one gathering</h3>
<p>The main room opens to covered space and open ground, so a ceremony, a supper and a bonfire
can be one continuous evening instead of three separate logistics problems.</p>
</div>{ph('gal5.jpg','Evening lights outdoors','wide')}</div>
<div class="vrow"><div class="txt">
<h3>A room that takes your vision</h3>
<p>Warm timber, plain walls and honest materials — a canvas that flatters whatever you bring,
from bare-table rustic to full florals. Tables, chairs and settings are already here.</p>
</div>{ph('gal3.jpg','Open interior with brick and steel','wide')}</div>
<div class="vrow"><div class="txt">
<h3>People who serve like it matters</h3>
<p>The same people who mentor here all week host your event. Hospitality is not a service tier
at Shiloh. It is the house habit.</p>
</div>{ph('gal2.jpg','Tables set for dinner','wide')}</div>
</div></section>

<section class="tight"><div class="wrap">
<div class="eyebrow">Shiloh is right for you if&hellip;</div>
<ul class="checks">
<li>You want an intimate gathering, not a production line</li>
<li>You would rather design the room than rent a look</li>
<li>Warm, honest materials beat mirror-and-chandelier polish</li>
<li>Indoor-outdoor flow matters to your day</li>
<li>You like knowing where the money goes</li>
<li>You want hosts who treat your event as the point, not an interruption</li>
</ul>
</div></section>

<section class="tight"><div class="wrap"><div class="gal">
{ph('gather.jpg','The venue approach','')}
{ph('gal1.jpg','Reception under timber','sq')}
{ph('givehero.jpg','A community dinner','sq')}
{ph('gal4.jpg','The wood shop','sq')}
{ph('gal2.jpg','Dinner seating','sq')}
</div></div></section>

<section class="band"><div class="wrap">
<h2>Weddings, offsites, church and cohorts.</h2>
<p>Use is donation-based — there is no rate card. Tell us the date and what you are dreaming.</p>
<div style="margin-top:34px"><a class="btn" href="book.html">Book Your Event</a></div>
</div></section>
"""

build_pg = f"""
<section class="tight"><div class="wrap">
<div class="eyebrow">The build</div>
<h2 style="max-width:24ch">A 2,800 square foot warehouse, renovated in phases.</h2>
<p class="lede" style="margin-top:22px">Each phase is funded before the work on it starts. That is
slower than borrowing, and it is why there is no debt on this building.</p>
</div></section>

<section class="tight"><div class="wrap">{ph('buildwide.jpg','Construction in progress','wide')}</div></section>

<section><div class="wrap narrow">
<div class="eyebrow">Where things stand</div>
{''.join(f'<div class="phase"><div class="n">{n}</div><div><b>{s}</b>'
         f'<p style="margin-top:10px">{d}</p></div></div>' for n,s,d in PHASES)}
<div class="note"><p><b>Before launch:</b> replace these phase notes with the live updates from
Jeff's own log, and set a real target date on Phase 3. This page should change most often — it is
the reason people come back.</p></div>
</div></section>

<section class="band"><div class="wrap">
<h2>Phase 3 is scoped. The date depends on the giving.</h2>
<p>The costs are known. What is not yet known is when.</p>
<div style="margin-top:34px"><a class="btn" href="give.html">Fund the Next Phase</a></div>
</div></section>
"""

visit = f"""
<section><div class="wrap split">
<div>
<div class="eyebrow">Visit</div><h2>Dawsonville, Georgia.</h2><div class="rule"></div>
<p>Shiloh sits in the North Georgia foothills — minutes from downtown Dawsonville, an easy drive
up GA-400, and close enough to the mountains that your guests can make a weekend of it.</p>
<ul class="facts">
<li><b>Mail</b><span>PO Box 277, Dawsonville, GA 30534</span></li>
<li><b>Phone</b><span><a href="tel:+16782766486" style="color:{INK}">(678) 276-6486</a></span></li>
<li><b>Building</b><span>2,800 sq ft warehouse, under renovation</span></li>
<li><b>Street address</b><span>Published once Phase 3 is complete</span></li>
<li><b>Parking</b><span>On site</span></li>
<li><b>Visits</b><span>By arrangement — call ahead while work is ongoing</span></li>
</ul>
</div>
<div class="slot sq"><span>Map — embed once the street address is public</span></div>
</div></section>

<section class="tight"><div class="wrap">{ph('visitwide.jpg','North Georgia countryside','wide')}</div></section>

<section class="tight"><div class="wrap">
<div class="eyebrow">The neighborhood</div>
<h2>Worth arriving early for.</h2>
<p class="lede" style="margin-top:20px">Dawsonville is racing heritage, mountain trailheads and a
courthouse square — with the start of the Appalachians twenty minutes up the road.</p>
<div class="tiles">
<div class="tile">Downtown Dawsonville</div>
<div class="tile">Amicalola Falls State Park</div>
<div class="tile">Georgia Racing Hall of Fame</div>
<div class="tile">North Georgia Premium Outlets</div>
<div class="tile">Etowah River</div>
<div class="tile">GA-400 Corridor</div>
<div class="tile">Local Coffee &amp; Eats</div>
<div class="tile">Your business here?</div>
</div>
<div class="note"><p><b>Before launch:</b> the reference links each neighborhood tile to a real
local partner. Swap these general landmarks for the businesses Jeff actually wants to send guests
to, with links and logos as those relationships form.</p></div>
</div></section>
"""

book = f"""
<div class="hero dim" style="min-height:52vh;background-image:url('assets/stock/gal2.jpg')"><div class="wrap">
<div class="kick">Book now</div>
<h1 style="font-size:clamp(30px,3.8vw,50px)">Book your event.</h1>
<p>Weddings, offsites, church gatherings, classes and suppers. Every booking funds the mission.</p>
</div></div>

<section class="tight"><div class="wrap">
<div class="eyebrow">How it works</div>
<div class="steps">
<div><span class="n">01</span><h3>Send the enquiry</h3><p>Tell us the date, the headcount and
what you are imagining. We will confirm whether the room is free.</p></div>
<div><span class="n">02</span><h3>Walk the building</h3><p>Come see it — the walkthrough is
where most decisions get easy. Call and we will set a time.</p></div>
<div><span class="n">03</span><h3>Set your gift</h3><p>There is no rate card. Venue use is
donation-based: we agree a gift that fits your event, and all of it funds the work.</p></div>
</div>
</div></section>

<section><div class="wrap narrow">
<div class="eyebrow">Enquire</div>
<h2>Check a date.</h2>
<form class="book" action="mailto:hello@shilohcollective.org" method="get">
<div><label for="n">Name</label><input id="n" name="name" required></div>
<div><label for="e">Email</label><input id="e" name="email" type="email" required></div>
<div><label for="d">Preferred date</label><input id="d" name="date" type="date"></div>
<div><label for="g">Estimated guests</label><input id="g" name="guests" type="number" min="1"></div>
<div class="full"><label for="t">Event type</label><select id="t" name="type">
<option>Wedding / reception</option><option>Company offsite</option>
<option>Church / community</option><option>Class / cohort</option><option>Other</option>
</select></div>
<div class="full"><label for="m">Tell us about it</label>
<textarea id="m" name="notes" rows="5"></textarea></div>
<div class="full"><button class="btn dark" type="submit">Send Enquiry</button>
<span style="margin-left:18px;font-size:14px;color:{STONE}">or call
<a href="tel:+16782766486" style="color:{INK}">(678) 276-6486</a></span></div>
</form>
</div></section>

<section class="tight"><div class="wrap narrow">
<div class="eyebrow">See it first</div>
<h2>Schedule a walkthrough.</h2>
<p style="margin-top:18px">While the renovation is live, tours run by arrangement. Call
<a href="tel:+16782766486" style="color:{INK}">(678) 276-6486</a> and we will meet you at the
building.</p>
<div class="note"><p><b>Before launch:</b> wire the form to a real endpoint (Formspree or
similar) and confirm the enquiry address — <i>hello@shilohcollective.org is a placeholder</i>.
The reference uses a scheduling widget for tours; add one here if Jeff wants self-serve booking.
Confirm the donation-based wording with Jeff and Amy — it is Matt's current understanding, not
their published policy.</p></div>
</div></section>
"""

give = f"""
<div class="hero dim" style="min-height:52vh;background-image:url('assets/stock/givehero.jpg')"><div class="wrap">
<div class="kick">Support the build</div>
<h1 style="font-size:clamp(30px,3.8vw,50px)">Every phase is paid for before it starts.</h1>
<p>Which means giving does not disappear into an account. It puts up a wall.</p>
</div></div>

<section><div class="wrap">
<div class="feat two">{''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t,d in WAYS)}</div>
<div class="narrow"><div class="note"><p><b>Before launch:</b> confirm the giving routes and the
exact legal wording with Transforming Truth Ministries. Do not describe a gift as tax-deductible
until the correct entity and its status are confirmed in writing — Project i61's own determination
is still pending and the two must not be conflated.</p></div></div>
</div></section>

<section class="band"><div class="wrap">
<h2>Or come and look at it first.</h2>
<p>Call ahead and someone will walk you through what is finished and what is not.</p>
<div style="margin-top:34px"><a class="btn" href="visit.html">Plan a Visit</a></div>
</div></section>
"""

PAGES = [
 ('index.html','Home',home,'An event venue and equipping centre in Dawsonville, Georgia — every booking funds the mission.'),
 ('mission.html','Mission',mission,'Why Shiloh Collective exists, and who leads it.'),
 ('gather.html','Gather',gather,'Weddings, offsites, church and cohorts at Shiloh Collective.'),
 ('build.html','The Build',build_pg,'Phase-by-phase progress on the Shiloh Collective renovation.'),
 ('visit.html','Visit',visit,'Where Shiloh Collective is and how to arrange a visit.'),
 ('book.html','Book Now',book,'Check a date and book Shiloh Collective for your event.'),
 ('give.html','Give',give,'Ways to support the Shiloh Collective build.'),
]
os.makedirs('assets', exist_ok=True)
src='/home/user/agentic-os/os-vault/wiki/projects/assets/i61/seal_i61_oak_a-slight.png'
if os.path.exists(src): shutil.copy(src,'assets/seal.png')
for fn,title,body,desc in PAGES:
    open(fn,'w').write(page(title,fn,body,desc)); print('wrote',fn)
