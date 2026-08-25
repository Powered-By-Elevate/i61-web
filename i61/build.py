#!/usr/bin/env python3
"""Project i61 — public site. Same design family as sites/shiloh, dark masthead.
Voice: Walt's vision language, external register (faith-forward is correct here).
Hard rules baked in: no officer names on the site (Walt removed people from the one-pager,
2026-08-12); never claims 501(c)(3) status (determination pending); no money figures."""
import os

INK, GOLD, CREAM, PAPER = '#131315', '#C6A670', '#F4EFE6', '#FBF9F5'
STONE, LINE, DEEP = '#8A8378', '#DED8CC', '#1E1D1C'
NAV = [('Home','index.html'), ('Mission','mission.html'),
       ('Projects','projects.html'), ('Connect','connect.html')]

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}} html{{scroll-behavior:smooth}}
body{{background:{PAPER};color:{INK};font-family:Georgia,'Times New Roman',serif;
 font-size:18px;line-height:1.7;-webkit-font-smoothing:antialiased}}
a{{color:inherit}} .wrap{{max-width:1180px;margin:0 auto;padding:0 32px}}
.narrow{{max-width:760px;margin:0 auto}}
header{{position:sticky;top:0;z-index:50;background:rgba(19,19,21,.96);
 backdrop-filter:blur(8px);border-bottom:1px solid #2C2A28}}
.bar{{display:flex;align-items:center;justify-content:space-between;height:86px}}
.brand{{display:flex;align-items:center;gap:14px;text-decoration:none;color:{CREAM}}}
.brand img{{width:48px;height:48px;display:block}}
.brand b{{font-family:Helvetica,Arial,sans-serif;font-size:15px;letter-spacing:.18em;
 text-transform:uppercase;font-weight:700}}
.brand b i{{font-style:normal;text-transform:none}}
nav ul{{display:flex;gap:30px;list-style:none;align-items:center}}
nav a{{font-family:Helvetica,Arial,sans-serif;font-size:12.5px;letter-spacing:.16em;
 text-transform:uppercase;text-decoration:none;color:#A9A296;padding-bottom:3px;
 border-bottom:1px solid transparent;transition:color .18s,border-color .18s}}
nav a:hover,nav a.on{{color:{CREAM};border-color:{GOLD}}}
nav a.cta{{background:{GOLD};color:{INK};padding:12px 22px;border:0;letter-spacing:.14em}}
nav a.cta:hover{{background:{CREAM}}}
.menu{{display:none;font-size:24px;background:none;border:0;cursor:pointer;color:{CREAM}}}
.hero{{position:relative;background:{DEEP};color:{CREAM};min-height:76vh;display:flex;
 align-items:center;background-size:cover;background-position:center}}
.hero .wrap{{padding:100px 32px;position:relative;z-index:2}}
.hero.dim::before{{content:"";position:absolute;inset:0;
 background:linear-gradient(100deg,rgba(15,14,13,.85) 36%,rgba(15,14,13,.45) 78%,rgba(15,14,13,.6))}}
.hero h1{{font-size:clamp(33px,4.5vw,60px);line-height:1.16;font-weight:400;max-width:18ch}}
.hero p{{margin-top:26px;max-width:56ch;font-size:20px;color:#EDE7DA}}
.kick{{font-family:Helvetica,Arial,sans-serif;font-size:12px;letter-spacing:.28em;
 text-transform:uppercase;color:{GOLD};margin-bottom:22px}}
.rule{{width:88px;height:2px;background:{GOLD};margin:30px 0}}
.btn{{display:inline-block;font-family:Helvetica,Arial,sans-serif;font-size:12.5px;
 letter-spacing:.16em;text-transform:uppercase;text-decoration:none;padding:17px 34px;
 background:{GOLD};color:{INK};transition:background .18s;border:0;cursor:pointer}}
.btn:hover{{background:{CREAM}}}
.btn.ghost{{background:transparent;color:{CREAM};box-shadow:inset 0 0 0 1px rgba(244,239,230,.5)}}
.btn.ghost:hover{{background:{CREAM};color:{INK};box-shadow:none}}
.btn.dark{{background:{INK};color:{CREAM}}} .btn.dark:hover{{background:{GOLD};color:{INK}}}
section{{padding:104px 0}} section.tight{{padding:70px 0}}
.eyebrow{{font-family:Helvetica,Arial,sans-serif;font-size:12px;letter-spacing:.26em;
 text-transform:uppercase;color:{STONE};margin-bottom:18px}}
h2{{font-size:clamp(27px,3vw,40px);line-height:1.24;font-weight:400;max-width:22ch}}
h3{{font-family:Helvetica,Arial,sans-serif;font-size:15px;letter-spacing:.13em;
 text-transform:uppercase;font-weight:700;margin-bottom:12px}}
.lede{{font-size:21px;line-height:1.62;max-width:60ch;color:#3A362F}}
p+p{{margin-top:18px}}
.ph{{overflow:hidden;background:#E8E2D6;border:1px solid {LINE}}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block}}
.ph.tall{{aspect-ratio:3/4}} .ph.wide{{aspect-ratio:16/9}} .ph.sq{{aspect-ratio:1/1}}
.steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:44px;margin-top:56px}}
.steps .n{{font-family:Helvetica,Arial,sans-serif;font-size:13px;letter-spacing:.2em;
 color:{GOLD};display:block;margin-bottom:14px}}
.steps p{{font-size:17px;color:#3A362F}}
.band{{background:{DEEP};color:{CREAM};text-align:center;position:relative;overflow:hidden;
 background-size:cover;background-position:center}}
.band.dim::before{{content:"";position:absolute;inset:0;background:rgba(15,14,13,.78)}}
.band .wrap{{position:relative;z-index:2}}
.band h2{{margin:0 auto;max-width:26ch}} .band p{{color:#E4DDD0;max-width:58ch;margin:20px auto 0}}
.split{{display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center}}
.stack>*+*{{margin-top:22px}}
.feat{{display:grid;grid-template-columns:repeat(3,1fr);gap:50px 44px;margin-top:56px}}
.feat.two{{grid-template-columns:repeat(2,1fr);gap:52px}}
.feat p{{font-size:17px;color:#3A362F}}
.isnot{{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid {LINE};margin-top:50px}}
.isnot>div{{padding:44px 40px}}
.isnot>div:first-child{{background:{CREAM};border-right:1px solid {LINE}}}
.isnot ul{{list-style:none;margin-top:22px}}
.isnot li{{padding:10px 0 10px 28px;position:relative;font-size:17px}}
.isnot li::before{{content:"";position:absolute;left:0;top:19px;width:11px;height:11px;background:{GOLD}}}
.isnot .no li::before{{background:{LINE}}}
.card{{border:1px solid {LINE};background:#fff}}
.card .body{{padding:36px 38px}}
.note{{background:{CREAM};border-left:3px solid {GOLD};padding:26px 30px;margin-top:44px}}
.note p{{font-size:15.5px;line-height:1.85;color:#3A362F}}
form.c{{margin-top:44px;display:grid;grid-template-columns:1fr 1fr;gap:22px}}
form.c label{{font-family:Helvetica,Arial,sans-serif;font-size:11.5px;letter-spacing:.16em;
 text-transform:uppercase;color:{STONE};display:block;margin-bottom:9px}}
form.c input,form.c select,form.c textarea{{width:100%;padding:14px 16px;border:1px solid {LINE};
 background:#fff;font-family:Georgia,serif;font-size:16.5px;color:{INK}}}
form.c .full{{grid-column:1/-1}}
footer{{background:{INK};color:#A9A296;padding:72px 0 44px;
 font-family:Helvetica,Arial,sans-serif;font-size:13.5px}}
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
 .split,.feat,.feat.two,.fgrid,.steps,.isnot,form.c{{grid-template-columns:1fr;gap:34px}}
 .isnot>div:first-child{{border-right:0;border-bottom:1px solid {LINE}}}
 nav ul{{display:none}} .menu{{display:block}} section{{padding:70px 0}}
}}"""

def nav_html(active):
    out=[]
    for t,h in NAV:
        cls='cta' if t=='Connect' else ('on' if h==active else '')
        attr=f' class="{cls}"' if cls else ''
        out.append(f'<li><a href="{h}"{attr}>{t}</a></li>')
    return ''.join(out)

def ph(img, alt, cls='wide'):
    return f'<div class="ph {cls}"><img src="assets/stock/{img}" alt="{alt}" loading="lazy"></div>'

def page(title, active, body, desc):
    flinks=''.join(f'<li><a href="{h}">{t}</a></li>' for t,h in NAV)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Project i61</title><meta name="description" content="{desc}">
<style>{CSS}</style></head><body>
<header><div class="wrap bar">
<a class="brand" href="index.html"><img src="assets/seal.png" alt="">
<b>Project <i>i61</i></b></a>
<nav><ul>{nav_html(active)}</ul></nav><button class="menu" aria-label="Menu">&#9776;</button>
</div></header>
{body}
<footer><div class="wrap"><div class="fgrid">
<div><div class="fbrand"><img src="assets/seal.png" alt=""><b>Project i61</b></div>
<p style="max-width:42ch;line-height:1.8">An equipping mechanism for small, strong local
initiatives — built on relationships, not programmes. Organizing as a nonprofit in South
Carolina.</p></div>
<div><b class="fh">Pages</b><ul class="flist">{flinks}</ul></div>
<div><b class="fh">First project</b><ul class="flist">
<li><a href="../shiloh/index.html">Shiloh Collective</a></li>
<li>Dawsonville, Georgia</li></ul></div>
</div><div class="fbot">
<span>&copy; 2026 Project i61 &middot;
<a href="assets/stock/CREDITS.md" style="color:#7C766C">temporary photo credits</a></span>
<span style="letter-spacing:.2em;text-transform:uppercase;color:{GOLD}">Built to Lift</span></div>
</div></footer></body></html>"""

home = f"""
<div class="hero dim" style="background-image:url('assets/stock/bridge.jpg')"><div class="wrap">
<div class="kick">Project i61</div>
<h1>We help the people who are already building.</h1>
<p>Project i61 is an equipping mechanism for small, strong local initiatives — the bridge between
people with a work in their hands and the resources, skills and friends that work needs.</p>
<div class="rule"></div>
<a class="btn" href="connect.html">Connect With Us</a>
<a class="btn ghost" href="mission.html" style="margin-left:12px">Why We Exist</a>
</div></div>

<section><div class="wrap">
<div class="eyebrow">The model</div>
<h2>We don't build our own centres. We come alongside.</h2>
<div class="steps">
<div><span class="n">01</span><h3>Find the builders</h3><p>Every town has people already doing
the work — a teacher, a tradesman, a pastor with a warehouse and a vision. We look for them, not
for markets.</p></div>
<div><span class="n">02</span><h3>Come alongside</h3><p>Money is the least of it. Skills, tools,
counsel, connections and stubborn friendship — whatever the work actually needs, for as long as
it needs it.</p></div>
<div><span class="n">03</span><h3>Stay small on purpose</h3><p>Relationships are the core of the
mission. Small equipping stations change a town's culture; institutions mostly change their own
org charts.</p></div>
</div>
</div></section>

<section class="band dim" style="background-image:url('assets/stock/sunrise.jpg')"><div class="wrap">
<div class="eyebrow" style="color:{GOLD}">The name</div>
<h2>&ldquo;&hellip; that they may be called oaks of righteousness, the planting of the
Lord.&rdquo;</h2>
<p>Isaiah 61 — the chapter this work is named for. Rebuild the ruined places, and do it by
raising up the people who live there. The oak on our seal grows above the line and roots below
it: what holds is what nobody sees.</p>
</div></section>

<section><div class="wrap split">
<div class="stack">
<div class="eyebrow">First connection project</div>
<h2>Shiloh Collective, Dawsonville.</h2>
<p class="lede">An equipping centre for young adults, built by hand inside a 2,800 square foot
warehouse — led by the people of Transforming Truth Ministries. i61 does not run it. We come
alongside the people who do.</p>
<div style="margin-top:14px"><a class="btn dark" href="../shiloh/index.html">Visit Shiloh
Collective</a></div>
</div>
{ph('hands.jpg','Volunteers building together','tall')}
</div></section>

<section class="tight"><div class="wrap">
<div class="eyebrow">How we carry ourselves</div>
<div class="feat">
<div><h3>Hospitality</h3><p>A stranger should feel expected. In every room we touch, that is a
design decision before it is a value.</p></div>
<div><h3>Gratitude</h3><p>We build like people who were handed something — because we were.</p></div>
<div><h3>Generosity</h3><p>Capacity gets shared. What we help build belongs to its town, not to
us.</p></div>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>Building something in your town?</h2>
<p>Tell us about it. The next connection project starts with a conversation, not an application.</p>
<div style="margin-top:34px"><a class="btn" href="connect.html">Start the Conversation</a></div>
</div></section>
"""

mission = f"""
<section><div class="wrap narrow">
<div class="eyebrow">Our mission</div>
<h2 style="max-width:26ch">Kingdom builders are already out there. Our job is to make sure they
don't build alone.</h2>
<div class="rule"></div>
<p class="lede">Project i61 exists to equip small but strong local initiatives — works led by
people who know their town, love it, and have already started. We bring resources, skill and
friendship to what they are building, and we keep the relationship at the centre, because that is
the mission, not a method for it.</p>
<p>We believe change that lasts comes from small equipping stations, not large institutions — from
people who choose to do life together in a place, rather than administrate it from a distance.</p>
</div></section>

<section class="tight"><div class="wrap">
<div class="eyebrow">Plainly, then</div>
<div class="isnot">
<div><h3>i61 is</h3><ul>
<li>An equipping mechanism for local works already under way</li>
<li>Built on relationships that outlast any single project</li>
<li>A supplier of skills, tools, counsel and connections</li>
<li>Small on purpose, and intending to stay that way</li>
</ul></div>
<div class="no"><h3>i61 is not</h3><ul>
<li>A headquarters, a franchise or a network with a logo pack</li>
<li>A grant portal with an application form</li>
<li>The owner or operator of the works it serves</li>
<li>Finished when the money is spent — we stay</li>
</ul></div>
</div>
</div></section>

<section class="band dim" style="background-image:url('assets/stock/land.jpg')"><div class="wrap">
<div class="eyebrow" style="color:{GOLD}">Isaiah 61</div>
<h2>Rebuild the ancient ruins. Raise up the former devastations.</h2>
<p>The chapter we are named for is a commission to restore places through people — and its
promise is that the restored become &ldquo;oaks of righteousness,&rdquo; strong enough to hold
others. That is the whole theory of change.</p>
</div></section>

<section><div class="wrap split">
<div class="stack">
<div class="eyebrow">Where we are</div>
<h2>Early, and honest about it.</h2>
<p>Project i61 is organizing as a nonprofit in South Carolina; our federal tax-status
determination is in process. Our first connection project is live in Dawsonville, Georgia, and
the lessons it teaches us are shaping how we serve the next one.</p>
</div>
{ph('work.jpg','A trade taught by hand','tall')}
</div></section>

<section class="band"><div class="wrap">
<h2>Built to lift.</h2>
<p>The tagline is the test: if what we do doesn't lift the people doing the work, we stop doing
it.</p>
<div style="margin-top:34px"><a class="btn" href="projects.html">See the Work</a></div>
</div></section>
"""

projects = f"""
<section class="tight"><div class="wrap">
<div class="eyebrow">Projects</div>
<h2 style="max-width:24ch">Connection projects — one at a time, done properly.</h2>
<p class="lede" style="margin-top:22px">We would rather serve one work well than badge twenty. A
connection project is a long commitment to people, not a line in an annual report.</p>
</div></section>

<section class="tight"><div class="wrap">
<div class="card"><div class="ph wide" style="border:0">
<img src="assets/stock/hands.jpg" alt="Volunteers building together" loading="lazy"></div>
<div class="body">
<div class="eyebrow" style="margin-bottom:10px">First connection project &middot; Dawsonville, GA</div>
<h2 style="font-size:30px">Shiloh Collective</h2>
<p style="margin-top:16px;max-width:66ch">A mentorship and equipping centre for young adults, led
by Jeff and Amy Lyle through Transforming Truth Ministries — a 2,800 square foot warehouse being
renovated in phases, each one paid for before its work begins. Young adults are trained in a
trade and in the habits that keep a life steady, fed at the same table, and sent. i61 comes
alongside with skills, resources and friendship.</p>
<div style="margin-top:26px"><a class="btn dark" href="../shiloh/index.html">Visit Shiloh
Collective</a></div>
</div></div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">What makes a connection project</div>
<h2>What we look for.</h2>
<div class="feat two" style="margin-top:44px">
<div><h3>Local people, already moving</h3><p>The work exists before we arrive. We fund momentum,
not intentions.</p></div>
<div><h3>Small and rooted</h3><p>Led by people who live there and plan to stay — a work the town
would miss.</p></div>
<div><h3>Builds people, not just things</h3><p>Whatever gets constructed, the real output is
young adults, families and neighbours who are stronger for it.</p></div>
<div><h3>Open books, plain dealing</h3><p>We work with people who tell the truth about money,
timelines and setbacks — and we do the same.</p></div>
</div>
</div></section>

<section class="band dim" style="background-image:url('assets/stock/table.jpg')"><div class="wrap">
<h2>The next one starts with a conversation.</h2>
<p>If this sounds like the work in your hands, we would like to hear about it.</p>
<div style="margin-top:34px"><a class="btn" href="connect.html">Tell Us About Your Work</a></div>
</div></section>
"""

connect = f"""
<div class="hero dim" style="min-height:52vh;background-image:url('assets/stock/table.jpg')"><div class="wrap">
<div class="kick">Connect</div>
<h1 style="font-size:clamp(30px,3.8vw,50px)">Start the conversation.</h1>
<p>Builders, partners, and people who want to help lift — this is the front door.</p>
</div></div>

<section><div class="wrap narrow">
<div class="eyebrow">Write to us</div>
<h2>Tell us who you are and what you are building.</h2>
<form class="c" action="mailto:hello@projecti61.org" method="get">
<div><label for="n">Name</label><input id="n" name="name" required></div>
<div><label for="e">Email</label><input id="e" name="email" type="email" required></div>
<div class="full"><label for="w">I am&hellip;</label><select id="w" name="who">
<option>Building something local and want to talk</option>
<option>Interested in partnering or serving</option>
<option>Interested in giving</option>
<option>Praying for the work and want updates</option>
<option>Something else</option>
</select></div>
<div class="full"><label for="m">The work, in your own words</label>
<textarea id="m" name="notes" rows="6"></textarea></div>
<div class="full"><button class="btn dark" type="submit">Send</button></div>
</form>
<div class="note"><p><b>Before launch:</b> wire the form to a real endpoint and stand up the
email — <i>hello@projecti61.org is a placeholder and the domain is not yet registered</i>. On
giving: until the federal determination letter is in hand, this site must not describe Project
i61 as a 501(c)(3) or any gift as tax-deductible. Route interested givers to a conversation, not
a checkout.</p></div>
</div></section>

<section class="band"><div class="wrap">
<h2>See the first work.</h2>
<p>Shiloh Collective is the best introduction to what coming alongside actually looks like.</p>
<div style="margin-top:34px"><a class="btn" href="../shiloh/index.html">Visit Shiloh Collective</a></div>
</div></section>
"""

PAGES = [
 ('index.html','Home',home,'Project i61 — an equipping mechanism for small, strong local initiatives. Built to lift.'),
 ('mission.html','Mission',mission,'Why Project i61 exists: equipping the people already building, and staying small on purpose.'),
 ('projects.html','Projects',projects,'Connection projects — starting with Shiloh Collective in Dawsonville, Georgia.'),
 ('connect.html','Connect',connect,'Start a conversation with Project i61 — builders, partners, givers.'),
]
for fn,title,body,desc in PAGES:
    open(fn,'w').write(page(title,fn,body,desc)); print('wrote',fn)
