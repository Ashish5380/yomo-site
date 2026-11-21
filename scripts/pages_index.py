"""Page bodies. Appended to build_site.py (kept in a separate module for length)."""
from build_site import icon, page, MAIL


def request_form(subject: str = "Yomo invite request", plan: str = "Free",
                 button: str = "Request invite", compact: bool = False) -> str:
    h = "h-12" if compact else "h-14"
    return f"""<form class="flex flex-col sm:flex-row items-stretch gap-3 w-full" data-waitlist data-subject="{subject}" data-plan="{plan}">
        <input class="flex-1 {h} px-4 bg-surface-container-lowest text-primary placeholder:text-secondary rounded-xl font-body text-body-md border border-hairline focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all" placeholder="Enter your email" type="email" required aria-label="Your email"/>
        <button class="{h} px-7 rounded-xl bg-primary-container text-on-primary font-label text-label-lg hover:bg-primary-hover transition-all shadow-[0_4px_16px_rgba(16,18,34,0.18)] hover:-translate-y-0.5 flex items-center justify-center gap-2 btn-shimmer" type="submit">
          {button}
          {icon('arrow', 'w-4 h-4', '2.2')}
        </button>
      </form>
      <p data-sent class="hidden mt-2 font-body text-body-sm text-[#047857]">Your mail app is opening with the request ready — send it and we'll reply from {MAIL}.</p>"""


INDEX = f"""
<main class="w-full pt-20">
  <!-- Status strip -->
  <section class="w-full max-w-7xl mx-auto px-6 lg:px-12 pt-8 pb-3">
    <div class="flex items-center justify-between flex-wrap gap-4">
      <div class="inline-flex items-center gap-2.5 px-3.5 py-1.5 rounded-full bg-[#ecfdf5] border border-[#a7f3d0]/60">
        <span class="w-2 h-2 rounded-full bg-[#10b981] animate-pulse"></span>
        <span class="font-label text-[11px] tracking-wide text-[#047857] uppercase font-bold">Private beta for India · invite only</span>
      </div>
      <div class="hidden sm:flex items-center gap-3 text-secondary font-label text-label-sm">
        <span class="flex items-center gap-1.5 font-medium">{icon('shield', 'w-4 h-4 text-[#047857]', '2')} Zero bank credentials</span>
        <span class="text-outline-variant">•</span>
        <span class="font-medium">Bank alerts from 21 Indian banks</span>
      </div>
    </div>
  </section>

  <!-- Hero -->
  <section class="w-full max-w-7xl mx-auto px-6 lg:px-12 pt-6 pb-20 relative">
    <div class="absolute -top-16 left-1/4 w-[540px] h-[540px] rounded-full bg-gradient-to-tr from-[#fef08a]/35 via-[#e0e7ff]/30 to-transparent blur-3xl -z-10 pointer-events-none glow-pulse"></div>
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-14 items-center">
      <div class="lg:col-span-7 flex flex-col items-start">
        <h1 class="font-display text-[42px] leading-[48px] lg:text-[58px] lg:leading-[64px] text-primary tracking-[-0.035em] font-extrabold">
          Money makes sense when your assistant
          <span class="relative inline-block whitespace-nowrap"><span class="relative z-10">actually reads</span><span class="absolute -bottom-1 left-0 w-full h-1 bg-[#fef08a] -z-0 rounded-sm"></span></span>
          the numbers.
        </h1>
        <p class="mt-6 font-body text-[17px] leading-[26px] text-secondary max-w-2xl">
          Yomo reads the bank alerts already sitting in your Gmail, the statements you forward, and — on Android — the bank SMS on your phone. Then it answers what you can spend, what you owe and where the money went. No bank logins. No OTPs. No spam.
        </p>

        <div class="mt-8 flex items-start gap-4 p-4 lg:p-5 rounded-2xl bg-surface-container-lowest border border-hairline shadow-soft max-w-xl w-full relative">
          <div class="relative shrink-0 mascot-float">
            <div class="absolute inset-0 rounded-2xl bg-[#e6007e]/15 blur-md -z-10"></div>
            <div class="w-20 h-20 rounded-2xl bg-surface-container-low border border-hairline p-1.5 flex items-center justify-center overflow-hidden">
              <img alt="Yomo assistant" class="w-full h-full object-cover rounded-xl" src="assets/mascot.png"/>
            </div>
            <span class="absolute -bottom-1 -right-1 flex h-5 w-5 items-center justify-center rounded-full bg-[#10b981] ring-2 ring-white">
              {icon('check', 'w-3 h-3 text-white', '3')}
            </span>
          </div>
          <div class="flex flex-col flex-1 pl-1">
            <div class="flex items-center gap-2 mb-1">
              <span class="font-label text-[12px] text-primary uppercase font-bold tracking-wider">Yomo pulse</span>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-[#ecfdf5] text-[#047857] font-bold border border-[#a7f3d0]/60">Illustrative</span>
            </div>
            <p class="font-body text-body-md text-primary leading-relaxed">
              "Safe to spend today <span class="font-semibold tnum text-primary bg-[#fef9c3]/70 px-1 py-0.5 rounded">₹1,180</span>. Netflix <span class="font-semibold tnum text-primary">₹799</span> tomorrow. Goa trip savings 62% done."
            </p>
            <div class="mt-2 flex items-center gap-3 text-[11px] text-secondary font-medium">
              <span class="flex items-center gap-1 text-[#047857]"><span class="w-1.5 h-1.5 rounded-full bg-[#10b981]"></span> Read-only feed</span>
              <span class="text-outline-variant">•</span>
              <span>Every number computed in the app</span>
            </div>
          </div>
        </div>

        <div class="mt-8 flex flex-col gap-2 w-full max-w-lg" id="request">
          {request_form()}
        </div>
        <div class="mt-3 flex items-center gap-3 text-secondary font-body text-body-sm">
          <span>Not ready yet?</span>
          <a class="text-primary font-semibold hover:underline inline-flex items-center gap-1 transition-colors" href="#how-it-works">
            See how it reads your data
            {icon('chevron', 'w-3.5 h-3.5', '2')}
          </a>
        </div>
      </div>

      <div class="lg:col-span-5 relative">
        <div class="absolute -top-12 -right-8 w-80 h-80 rounded-full bg-[#fef9c3]/50 blur-3xl -z-10"></div>
        <div class="absolute -bottom-8 -left-8 w-80 h-80 rounded-full bg-[#eef2ff]/70 blur-3xl -z-10"></div>
        <div class="flex flex-col gap-4">
          <div class="bg-surface-container-lowest rounded-2xl p-5 shadow-soft border border-hairline">
            <div class="flex items-center justify-between pb-3 border-b border-hairline">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-[#10b981] animate-pulse"></span>
                <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Ledger chat · example</span>
              </div>
              <span class="font-body text-body-sm text-secondary tnum font-medium">11:42 AM</span>
            </div>
            <div class="flex justify-end mt-4 mb-3">
              <div class="bg-surface-container-low text-primary rounded-2xl rounded-tr-none px-4 py-2.5 max-w-[85%] font-body text-body-md">
                Can I afford dinner out at Bastian this weekend?
              </div>
            </div>
            <div class="flex items-start gap-3">
              <div class="w-9 h-9 rounded-xl bg-surface-container-low border border-hairline shrink-0 p-0.5 overflow-hidden">
                <img alt="Yomo" class="w-full h-full object-cover rounded-lg" src="assets/mascot.png"/>
              </div>
              <div class="bg-surface-container-lowest rounded-2xl rounded-tl-none p-4 font-body text-body-md text-primary border border-hairline flex-1">
                <p class="leading-relaxed">Safe to spend today is <span class="font-semibold tnum">₹1,180</span>. Payday is the 25th — 6 days away. That leaves <span class="font-semibold text-[#047857] tnum">₹3,400</span> of weekend headroom once the pending electricity bill (<span class="tnum font-medium">₹1,420</span>) is set aside.</p>
                <div class="mt-2.5 pt-2 border-t border-hairline flex items-center justify-between text-body-sm text-secondary">
                  <span>From 2 bank feeds</span>
                  <span class="text-[#047857] font-semibold flex items-center gap-1">{icon('check', 'w-3.5 h-3.5', '2.5')} Verified</span>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-surface-container-lowest rounded-2xl p-5 shadow-soft border border-hairline">
            <div class="flex items-center justify-between mb-4">
              <div>
                <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Pacing engine</span>
                <h2 class="font-headline text-headline-sm text-primary font-bold">Daily discretionary runway</h2>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-[#ecfdf5] border border-[#a7f3d0]/60 text-[#047857] font-label text-label-sm font-bold tnum whitespace-nowrap">₹475 / day</span>
            </div>
            <div class="grid grid-cols-2 min-[420px]:grid-cols-3 gap-3 pt-1">
              <div class="p-3.5 rounded-xl bg-surface-container-low border border-hairline">
                <span class="font-body text-body-sm text-secondary block">Cycle start</span>
                <span class="font-currency-card text-currency-card text-primary tnum font-bold">₹68,500</span>
                <span class="text-[11px] text-secondary font-medium">Nov 01</span>
              </div>
              <div class="p-3.5 rounded-xl bg-surface-container-low border border-hairline">
                <span class="font-body text-body-sm text-secondary block">Spent so far</span>
                <span class="font-currency-card text-currency-card text-primary tnum font-bold">₹41,200</span>
                <span class="text-[11px] text-[#e53935] font-semibold">60.1% cycle</span>
              </div>
              <div class="col-span-2 min-[420px]:col-span-1 p-3.5 rounded-xl bg-[#ecfdf5] border border-[#a7f3d0]/80">
                <span class="font-body text-body-sm text-[#047857] block font-medium">Safe to spend</span>
                <span class="font-currency-card text-currency-card text-[#047857] tnum font-extrabold">₹12,450</span>
                <span class="text-[11px] text-[#047857] font-semibold">6 days left</span>
              </div>
            </div>
            <div class="mt-3.5 p-3 rounded-xl bg-surface-container-low border border-hairline flex items-center justify-between">
              <div class="flex items-center gap-2.5">
                <span class="w-2 h-2 rounded-full bg-[#e11d48] animate-ping"></span>
                <span class="font-body text-body-sm text-primary">Upcoming: <strong class="font-semibold">Netflix India</strong></span>
              </div>
              <span class="font-body text-body-sm font-bold text-primary tnum">₹799 · 26 Nov</span>
            </div>
          </div>

          <div class="bg-surface-container-lowest rounded-2xl p-5 shadow-soft border border-hairline">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded-lg bg-[#f3e8ff] text-[#7e22ce] flex items-center justify-center">{icon('tax', 'w-3.5 h-3.5', '2.2')}</span>
                <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Old vs new regime</span>
              </div>
              <span class="font-label text-label-sm text-[#047857] font-bold bg-[#ecfdf5] border border-[#a7f3d0]/60 px-2.5 py-0.5 rounded-full">Pro</span>
            </div>
            <div class="mt-3 flex items-center justify-between bg-surface-container-low p-3.5 rounded-xl border border-hairline gap-3">
              <div>
                <span class="font-body text-[12px] text-secondary block font-medium">On ₹18.4L CTC</span>
                <span class="font-headline text-headline-sm text-primary font-extrabold">New regime saves <span class="text-[#047857] tnum">₹41,912</span></span>
              </div>
              <div class="text-right shrink-0">
                <span class="font-body text-[12px] text-secondary block font-medium">Computed from</span>
                <span class="font-label text-label-md text-primary font-bold">your salary facts</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div class="w-full max-w-7xl mx-auto px-6 lg:px-12"><div class="w-full h-px bg-hairline"></div></div>

  <!-- How it works -->
  <section class="w-full max-w-7xl mx-auto px-6 lg:px-12 py-24" id="how-it-works">
    <div class="flex flex-col items-center text-center max-w-2xl mx-auto mb-16 rise">
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-[#fef9c3] border border-[#fde047]/60 text-primary mb-3">
        <span class="font-label text-label-sm uppercase font-bold tracking-wider">Read-only, all the way down</span>
      </div>
      <h2 class="font-headline text-[32px] leading-[40px] text-primary font-extrabold tracking-tight">Three steps. No bank password.</h2>
      <p class="font-body text-body-lg text-secondary mt-3">
        Yomo never logs into your bank. It reads the alerts and documents that already reach you — and only the ones you point it at.
      </p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-surface-container-lowest rounded-2xl p-8 border border-hairline shadow-soft flex flex-col justify-between rise">
        <div>
          <div class="w-12 h-12 rounded-xl bg-surface-container-low border border-hairline flex items-center justify-center text-primary mb-6">{icon('mail', 'w-6 h-6')}</div>
          <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Step 01</span>
          <h3 class="font-headline text-headline-sm text-primary mt-1 mb-3 font-bold">You connect a read-only feed</h3>
          <p class="font-body text-body-md text-secondary leading-relaxed">
            Gmail bank alerts through Google's read-only OAuth, a private forwarding address at <span class="text-primary font-semibold">goyomo.in</span>, statement PDFs and CSVs you upload, or the Android app's on-device SMS reader.
          </p>
        </div>
        <div class="mt-6 p-3.5 bg-surface-container-low rounded-xl border border-hairline">
          <div class="flex items-center gap-2 text-body-sm text-secondary">
            <span class="w-2 h-2 rounded-full bg-[#10b981]"></span>
            <span class="font-mono text-primary font-semibold text-xs">you@goyomo.in</span>
          </div>
        </div>
      </div>
      <div class="bg-surface-container-lowest rounded-2xl p-8 border border-hairline shadow-soft flex flex-col justify-between rise rise-1">
        <div>
          <div class="w-12 h-12 rounded-xl bg-[#ecfdf5] border border-[#a7f3d0]/60 flex items-center justify-center text-[#047857] mb-6">{icon('doc', 'w-6 h-6')}</div>
          <span class="font-label text-label-sm text-[#047857] uppercase font-bold tracking-wider">Step 02</span>
          <h3 class="font-headline text-headline-sm text-primary mt-1 mb-3 font-bold">Yomo reads the numbers</h3>
          <p class="font-body text-body-md text-secondary leading-relaxed">
            It checks the sender, pulls out the amount, merchant and date in <span class="text-primary font-bold">₹</span>, and names Indian merchants like Swiggy, Blinkit or Third Wave. OTPs are dropped; alert text is stored encrypted and never handed to the language model.
          </p>
        </div>
        <div class="mt-6 p-3.5 bg-surface-container-low rounded-xl border border-hairline flex items-center justify-between">
          <span class="font-body text-body-sm text-secondary font-medium">OTPs retained</span>
          <span class="font-label text-label-sm text-[#e53935] font-bold">none</span>
        </div>
      </div>
      <div class="bg-surface-container-lowest rounded-2xl p-8 border border-hairline shadow-soft flex flex-col justify-between rise rise-2">
        <div>
          <div class="w-12 h-12 rounded-xl bg-[#fef9c3] border border-[#fde047]/70 flex items-center justify-center text-primary mb-6">{icon('chat', 'w-6 h-6')}</div>
          <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Step 03</span>
          <h3 class="font-headline text-headline-sm text-primary mt-1 mb-3 font-bold">You ask, Yomo answers</h3>
          <p class="font-body text-body-md text-secondary leading-relaxed">
            "How much went to food this month?" "Can I afford Goa?" "Old regime or new?" Every figure is computed in the app from your own records and cited in rupees — never guessed by the model.
          </p>
        </div>
        <div class="mt-6 p-3.5 bg-surface-container-low rounded-xl border border-hairline flex items-center justify-between">
          <span class="font-body text-body-sm text-secondary font-medium">Voice</span>
          <span class="font-label text-label-sm text-primary font-bold">Roast · Pro · Zen</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Features -->
  <section class="w-full bg-surface-container-low py-24 border-y border-hairline" id="features">
    <div class="max-w-7xl mx-auto px-6 lg:px-12">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6 rise">
        <div>
          <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Built for Indian money</span>
          <h2 class="font-headline text-[32px] leading-[40px] text-primary font-extrabold mt-2 tracking-tight">Discipline without manual accounting.</h2>
        </div>
        <p class="font-body text-body-md text-secondary max-w-md">
          Salary dates, UPI, credit-card cycles, CAS statements and two tax regimes — the parts of Indian money that spreadsheets never quite survive.
        </p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="bg-surface-container-lowest rounded-2xl p-8 border border-hairline shadow-soft flex flex-col justify-between rise">
          <div>
            <div class="flex items-center justify-between mb-6">
              <span class="w-10 h-10 rounded-xl bg-[#eef2ff] flex items-center justify-center text-primary border border-hairline">{icon('rupee', 'w-5 h-5', '2')}</span>
              <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Salary pacing</span>
            </div>
            <h3 class="font-headline text-headline-md text-primary font-bold">Safe to spend &amp; pacing</h3>
            <p class="font-body text-body-md text-secondary mt-3 leading-relaxed">
              One number you can trust: what is genuinely left after fixed bills, subscriptions and what you have already set aside — paced to your salary date, not the calendar month.
            </p>
          </div>
          <div class="mt-8 p-4 rounded-xl bg-surface-container-low border border-hairline">
            <div class="flex justify-between items-center mb-2">
              <span class="font-body text-body-sm text-secondary font-medium">Remaining discretionary balance</span>
              <span class="font-headline text-headline-sm text-primary font-bold tnum">₹14,250</span>
            </div>
            <div class="w-full bg-surface-container-highest h-2 rounded-full overflow-hidden">
              <div class="bg-primary-container h-full rounded-full" style="width: 68%;"></div>
            </div>
            <div class="flex justify-between items-center mt-2.5 font-body text-body-sm text-secondary">
              <span>Day 19 of 30</span>
              <span class="text-[#047857] font-bold tnum">₹1,295/day runway</span>
            </div>
          </div>
        </div>
        <div class="bg-surface-container-lowest rounded-2xl p-8 border border-hairline shadow-soft flex flex-col justify-between rise rise-1">
          <div>
            <div class="flex items-center justify-between mb-6">
              <span class="w-10 h-10 rounded-xl bg-[#ecfdf5] flex items-center justify-center text-[#047857] border border-[#a7f3d0]/60">{icon('chart', 'w-5 h-5', '2')}</span>
              <span class="font-label text-label-sm text-[#047857] uppercase font-bold tracking-wider">Consolidated holdings</span>
            </div>
            <h3 class="font-headline text-headline-md text-primary font-bold">Portfolio &amp; net worth</h3>
            <p class="font-body text-body-md text-secondary mt-3 leading-relaxed">
              Mutual funds from a CAS statement, demat and NPS holdings, and broker positions from Zerodha, Groww and INDmoney — one net-worth line, no API keys you don't want to share.
            </p>
          </div>
          <div class="mt-8 p-4 rounded-xl bg-surface-container-low border border-hairline flex flex-col gap-2.5">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-[#10b981]"></span><span class="font-body text-body-sm text-primary font-medium">Parag Parikh Flexi Cap</span></div>
              <span class="font-body text-body-sm text-primary tnum font-bold">₹4,82,410</span>
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-[#3b82f6]"></span><span class="font-body text-body-sm text-primary font-medium">Nifty 50 Index Direct</span></div>
              <span class="font-body text-body-sm text-primary tnum font-bold">₹2,18,050</span>
            </div>
            <div class="pt-2 border-t border-hairline flex items-center justify-between text-body-sm text-secondary">
              <span>Equity growth</span>
              <span class="text-[#047857] font-bold tnum">+16.4% XIRR</span>
            </div>
          </div>
        </div>
        <div class="bg-surface-container-lowest rounded-2xl p-8 border border-hairline shadow-soft flex flex-col justify-between rise">
          <div>
            <div class="flex items-center justify-between mb-6">
              <span class="w-10 h-10 rounded-xl bg-[#fef9c3] flex items-center justify-center text-primary border border-[#fde047]/60">{icon('tax', 'w-5 h-5', '2')}</span>
              <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Pro plan</span>
            </div>
            <h3 class="font-headline text-headline-md text-primary font-bold">Old vs new tax regime</h3>
            <p class="font-body text-body-md text-secondary mt-3 leading-relaxed">
              A rupee comparison built on your actual salary, 80C and 80D deductions, HRA and the standard deduction — with the working shown, not a vague percentage.
            </p>
          </div>
          <div class="mt-8 grid grid-cols-2 gap-3">
            <div class="p-3.5 rounded-xl bg-surface-container-low border border-hairline">
              <span class="font-label text-label-sm text-secondary block font-medium min-h-[40px] min-[420px]:min-h-0">Old regime</span>
              <span class="font-currency-card text-[16px] min-[420px]:text-currency-card text-primary tnum font-bold">₹1,84,320</span>
              <span class="font-body text-body-sm text-secondary mt-1 block">with 80C + 80D</span>
            </div>
            <div class="p-3.5 rounded-xl bg-[#ecfdf5] border border-[#a7f3d0]/80">
              <span class="font-label text-label-sm text-[#047857] block font-medium min-h-[40px] min-[420px]:min-h-0">New regime</span>
              <span class="font-currency-card text-[16px] min-[420px]:text-currency-card text-[#047857] tnum font-extrabold">₹1,42,408</span>
              <span class="font-body text-body-sm text-[#047857] font-bold mt-1 block">Saves ₹41,912</span>
            </div>
          </div>
        </div>
        <div class="bg-surface-container-lowest rounded-2xl p-8 border border-hairline shadow-soft flex flex-col justify-between rise rise-1">
          <div>
            <div class="flex items-center justify-between mb-6">
              <span class="w-10 h-10 rounded-xl bg-[#f3e8ff] flex items-center justify-center text-[#7e22ce] border border-[#d8b4fe]/60">{icon('tag', 'w-5 h-5', '2')}</span>
              <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Merchant intelligence</span>
            </div>
            <h3 class="font-headline text-headline-md text-primary font-bold">Auto-categorisation you can correct</h3>
            <p class="font-body text-body-md text-secondary mt-3 leading-relaxed">
              UPI narrations turn into real merchant names — Third Wave Coffee, Decathlon, Blinkit, Apollo Pharmacy. Every guess is yours to approve, change, or explain.
            </p>
          </div>
          <div class="mt-8 flex flex-col gap-2.5 bg-surface-container-low p-3.5 rounded-xl border border-hairline">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded text-[11px] bg-surface-container-lowest border border-hairline font-bold text-secondary">UPI</span>
                <span class="font-body text-body-sm font-semibold text-primary">Third Wave Coffee</span>
              </div>
              <span class="font-body text-body-sm text-primary font-bold tnum">₹340.00</span>
            </div>
            <div class="flex items-center justify-between text-body-sm text-secondary pt-1 border-t border-hairline">
              <div class="flex items-center gap-1.5">
                <div class="w-4 h-4 rounded overflow-hidden shrink-0"><img alt="" class="w-full h-full object-cover" src="assets/mascot.png"/></div>
                <span class="text-[12px] text-[#047857] font-medium">Dining · auto-confirmed</span>
              </div>
              <span class="text-[11px] text-primary font-bold underline">Change</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Privacy -->
  <section class="w-full max-w-7xl mx-auto px-6 lg:px-12 py-24" id="privacy">
    <div class="bg-surface-container-lowest rounded-3xl p-8 lg:p-14 border border-hairline shadow-soft relative overflow-hidden rise">
      <div class="absolute -top-20 -right-20 w-72 h-72 rounded-full bg-[#fef9c3]/40 blur-3xl pointer-events-none"></div>
      <div class="inline-flex items-center gap-3 px-4 py-2 rounded-full bg-surface-container-low border border-hairline mb-6">
        <div class="w-6 h-6 rounded-lg overflow-hidden border border-hairline"><img alt="" class="w-full h-full object-cover" src="assets/mascot.png"/></div>
        <span class="font-label text-label-sm text-primary uppercase font-bold tracking-wider">Read-only, always</span>
      </div>
      <h2 class="font-headline text-[32px] leading-[40px] text-primary font-extrabold max-w-2xl tracking-tight">
        Yomo never moves money, never places orders, and never asks for a bank password or an OTP.
      </h2>
      <p class="font-body text-body-lg text-secondary mt-3 max-w-3xl leading-relaxed">
        Most finance apps ask for a bank login, an aggregator consent or full SMS access. Yomo reads only the financial alerts and documents you connect, and it tells you exactly what it stores.
      </p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-12 pt-8 border-t border-hairline">
        <div class="bg-surface-container-low p-6 lg:p-7 rounded-2xl border border-hairline">
          <div class="flex items-center gap-2 mb-4">
            <div class="w-6 h-6 rounded-full bg-[#ecfdf5] border border-[#a7f3d0] text-[#047857] flex items-center justify-center">{icon('check', 'w-3.5 h-3.5', '2.5')}</div>
            <h3 class="font-headline text-headline-sm text-primary font-bold">What Yomo keeps</h3>
          </div>
          <ul class="flex flex-col gap-3 font-body text-body-md text-secondary">
            <li class="flex items-start gap-2.5"><span class="text-primary font-bold leading-5">•</span><span>A payment ledger: merchant, date, amount in <span class="text-primary font-semibold">₹</span></span></li>
            <li class="flex items-start gap-2.5"><span class="text-primary font-bold leading-5">•</span><span>Holdings from the CAS statements and broker reads you connect</span></li>
            <li class="flex items-start gap-2.5"><span class="text-primary font-bold leading-5">•</span><span>Budgets, goals and the nudges you set</span></li>
            <li class="flex items-start gap-2.5"><span class="text-primary font-bold leading-5">•</span><span>Alert text, encrypted at rest, so a transaction can be parsed and checked</span></li>
          </ul>
        </div>
        <div class="bg-surface-container-low p-6 lg:p-7 rounded-2xl border border-hairline">
          <div class="flex items-center gap-2 mb-4">
            <div class="w-6 h-6 rounded-full bg-[#fee2e2] border border-[#fca5a5] text-[#ef4444] flex items-center justify-center">{icon('x', 'w-3.5 h-3.5', '2.5')}</div>
            <h3 class="font-headline text-headline-sm text-primary font-bold">What Yomo never keeps</h3>
          </div>
          <ul class="flex flex-col gap-3 font-body text-body-md text-secondary">
            <li class="flex items-start gap-2.5"><span class="text-[#ef4444] font-bold leading-5">•</span><span>Bank passwords, PINs or UPI credentials</span></li>
            <li class="flex items-start gap-2.5"><span class="text-[#ef4444] font-bold leading-5">•</span><span>One-time passwords — discarded before anything is stored</span></li>
            <li class="flex items-start gap-2.5"><span class="text-[#ef4444] font-bold leading-5">•</span><span>Any authority to move money or place an order</span></li>
            <li class="flex items-start gap-2.5"><span class="text-[#ef4444] font-bold leading-5">•</span><span>Personal or marketing email outside the financial senders you connect</span></li>
          </ul>
        </div>
      </div>
      <div class="mt-8 p-5 lg:p-6 rounded-2xl bg-surface-container-low border border-hairline flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3.5">
          <div class="w-10 h-10 rounded-xl bg-surface-container-lowest border border-hairline flex items-center justify-center text-primary shrink-0">{icon('download', 'w-5 h-5', '2')}</div>
          <div>
            <h4 class="font-label text-label-lg text-primary font-bold">Your data is yours. Period.</h4>
            <p class="font-body text-body-sm text-secondary">Export your ledger as CSV whenever you want, or delete everything from Settings — no email, no waiting.</p>
          </div>
        </div>
        <div class="flex items-center gap-2 shrink-0">
          <span class="text-[12px] font-bold text-[#047857] bg-[#ecfdf5] border border-[#a7f3d0]/80 px-3.5 py-1.5 rounded-xl flex items-center gap-1.5">
            {icon('check', 'w-3.5 h-3.5', '2.5')} Export &amp; delete in-app
          </span>
        </div>
      </div>
    </div>
  </section>

  <!-- Pricing -->
  <section class="w-full bg-surface-container py-24 px-6 lg:px-12" id="pricing">
    <div class="max-w-7xl mx-auto">
      <div class="flex flex-col items-center text-center max-w-2xl mx-auto mb-14 rise">
        <span class="font-label text-label-sm uppercase tracking-wider text-secondary font-bold">Pricing</span>
        <h2 class="font-headline text-[32px] leading-[40px] text-primary font-extrabold mt-2 tracking-tight">Start free. Pay when you want the whole picture.</h2>
        <p class="font-body text-body-lg text-secondary mt-3">Three plans, monthly or yearly. Deleting your data, exporting it and correcting a transaction are never paid features.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
        <div class="bg-surface-container-lowest rounded-2xl p-7 border border-hairline flex flex-col justify-between rise">
          <div>
            <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Free</span>
            <div class="mt-3 flex items-baseline gap-1"><span class="font-headline text-[34px] leading-[40px] font-extrabold text-primary tnum">₹0</span><span class="font-body text-body-sm text-secondary">/ forever</span></div>
            <p class="font-body text-body-md text-secondary mt-2">Enough to see whether the numbers land.</p>
            <ul class="mt-6 flex flex-col gap-3 font-body text-body-md text-primary">
              <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#047857] mt-0.5', '2.5')}<span>5 questions a day, 30 days of history</span></li>
              <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#047857] mt-0.5', '2.5')}<span>Safe-to-spend and budgets</span></li>
              <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#047857] mt-0.5', '2.5')}<span>One goal and totals in the weekly digest</span></li>
            </ul>
          </div>
          <a class="mt-8 h-12 rounded-xl border border-hairline bg-surface-container-lowest text-primary font-label text-label-lg flex items-center justify-center hover:bg-surface-container transition-colors" href="pricing.html">See what Free includes</a>
        </div>
        <div class="bg-primary-container text-on-primary rounded-2xl p-7 border border-white/10 flex flex-col justify-between shadow-lift relative overflow-hidden rise rise-1">
          <div class="absolute -top-24 -right-24 w-64 h-64 rounded-full bg-[#fde047]/15 blur-3xl pointer-events-none"></div>
          <div class="relative">
            <div class="flex items-center justify-between">
              <span class="font-label text-label-sm text-tertiary-fixed uppercase font-bold tracking-wider">Plus</span>
              <span class="font-label text-[10px] px-2 py-0.5 rounded-full bg-white/10 border border-white/15 text-[#82fab0] uppercase tracking-wider font-bold">Most people</span>
            </div>
            <div class="mt-3 flex items-baseline gap-1"><span class="font-headline text-[34px] leading-[40px] font-extrabold tnum">₹399</span><span class="font-body text-body-sm text-on-primary-container">/ month</span></div>
            <p class="font-body text-body-sm text-on-primary-container mt-1">or ₹3,990 a year — two months free</p>
            <ul class="mt-6 flex flex-col gap-3 font-body text-body-md">
              <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#82fab0] mt-0.5', '2.5')}<span>Unlimited chat and full history</span></li>
              <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#82fab0] mt-0.5', '2.5')}<span>The leak list — every merchant behind the spend</span></li>
              <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#82fab0] mt-0.5', '2.5')}<span>Portfolio depth: holdings, XIRR, drift</span></li>
              <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#82fab0] mt-0.5', '2.5')}<span>Every alert, the spend map and the full weekly story</span></li>
            </ul>
          </div>
          <a class="mt-8 h-12 rounded-xl bg-[#82fab0] text-[#00210f] font-label text-label-lg font-bold flex items-center justify-center gap-2 hover:bg-[#65dd96] transition-colors" href="pricing.html#plans">Choose Plus {icon('arrow', 'w-4 h-4', '2.5')}</a>
        </div>
        <div class="bg-surface-container-lowest rounded-2xl p-7 border border-hairline flex flex-col justify-between rise rise-2">
          <div>
            <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Pro</span>
            <div class="mt-3 flex items-baseline gap-1"><span class="font-headline text-[34px] leading-[40px] font-extrabold text-primary tnum">₹899</span><span class="font-body text-body-sm text-secondary">/ month</span></div>
            <p class="font-body text-body-sm text-secondary mt-1">or ₹7,999 a year</p>
            <ul class="mt-6 flex flex-col gap-3 font-body text-body-md text-primary">
              <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#047857] mt-0.5', '2.5')}<span>Everything in Plus</span></li>
              <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#047857] mt-0.5', '2.5')}<span>Old vs new tax pack, with the working shown</span></li>
              <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#047857] mt-0.5', '2.5')}<span>What-if planner and unlimited accounts</span></li>
            </ul>
          </div>
          <a class="mt-8 h-12 rounded-xl border border-hairline bg-surface-container-lowest text-primary font-label text-label-lg flex items-center justify-center hover:bg-surface-container transition-colors" href="pricing.html#plans">Choose Pro</a>
        </div>
      </div>
      <p class="font-body text-body-sm text-secondary text-center mt-6">Plans are activated by hand during the beta — request one and we'll set it up. Cancel anytime.</p>
    </div>
  </section>

  <!-- FAQ -->
  <section class="w-full max-w-4xl mx-auto px-6 lg:px-12 py-20" id="faq">
    <div class="text-center mb-12 rise">
      <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Questions</span>
      <h2 class="font-headline text-[32px] leading-[40px] text-primary font-extrabold mt-2 tracking-tight">The ones people actually ask</h2>
    </div>
    <div class="flex flex-col gap-4">
      <details class="group bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft rise">
        <summary class="flex items-center justify-between cursor-pointer select-none gap-4">
          <h3 class="font-headline text-[17px] text-primary font-bold">How does Yomo read my bank data without my bank password?</h3>
          <span class="w-7 h-7 shrink-0 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span>
        </summary>
        <p class="mt-4 font-body text-body-md text-secondary leading-relaxed pt-4 border-t border-hairline">
          Four read-only lanes: your Gmail bank alerts through Google's read-only OAuth, a private forwarding address on <span class="text-primary font-semibold">goyomo.in</span> that you point bank emails at, statement PDFs and CSVs you upload or share, and — on Android — an on-device reader that only sends messages from allowlisted bank senders. No bank login, no OTP, and no screen scraping at any point.
        </p>
      </details>
      <details class="group bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft rise">
        <summary class="flex items-center justify-between cursor-pointer select-none gap-4">
          <h3 class="font-headline text-[17px] text-primary font-bold">Can Yomo move money or place orders?</h3>
          <span class="w-7 h-7 shrink-0 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span>
        </summary>
        <p class="mt-4 font-body text-body-md text-secondary leading-relaxed pt-4 border-t border-hairline">
          Never. There is no payment, transfer or order-placement code in the product. It cannot reach a UPI switch, a bank API or a broker's order endpoint. Yomo is an analytical observer — it reads numbers and explains them.
        </p>
      </details>
      <details class="group bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft rise">
        <summary class="flex items-center justify-between cursor-pointer select-none gap-4">
          <h3 class="font-headline text-[17px] text-primary font-bold">Which banks and brokers work today?</h3>
          <span class="w-7 h-7 shrink-0 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span>
        </summary>
        <p class="mt-4 font-body text-body-md text-secondary leading-relaxed pt-4 border-t border-hairline">
          Bank alerts are recognised from 21 Indian banks — HDFC, ICICI, SBI, Axis, Kotak, PNB, Bank of Baroda, IDBI, IndusInd, Yes, Canara, Union, Federal, IDFC First, AU, Bank of India, Indian Overseas, UCO, Indian, Central and Standard Chartered. Statement files parse for HDFC, ICICI, SBI, Axis, Kotak and Standard Chartered plus credit-card statements, and CAS from CAMS/KFintech, NSDL and CDSL. Broker reads cover Zerodha, Groww and INDmoney.
        </p>
      </details>
      <details class="group bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft rise">
        <summary class="flex items-center justify-between cursor-pointer select-none gap-4">
          <h3 class="font-headline text-[17px] text-primary font-bold">Do I have to give Yomo my phone's SMS access?</h3>
          <span class="w-7 h-7 shrink-0 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span>
        </summary>
        <p class="mt-4 font-body text-body-md text-secondary leading-relaxed pt-4 border-t border-hairline">
          Only if you want the Android app to catch UPI spends as they happen — and then only messages from allowlisted bank senders are read. Personal SMS and OTPs never leave the phone. The web app works without any SMS access at all.
        </p>
      </details>
      <details class="group bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft rise">
        <summary class="flex items-center justify-between cursor-pointer select-none gap-4">
          <h3 class="font-headline text-[17px] text-primary font-bold">How do I export or delete everything?</h3>
          <span class="w-7 h-7 shrink-0 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span>
        </summary>
        <p class="mt-4 font-body text-body-md text-secondary leading-relaxed pt-4 border-t border-hairline">
          Both live in Settings. The CSV export is immediate; "Delete my data" permanently removes your transactions, holdings, chat history and connected feeds. Server backups roll off within 14 days. If you would rather ask a human, <a class="text-primary font-semibold underline" href="mailto:{MAIL}?subject=Data%20Deletion%20Request">email {MAIL}</a> and we'll confirm in writing.
        </p>
      </details>
      <details class="group bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft rise">
        <summary class="flex items-center justify-between cursor-pointer select-none gap-4">
          <h3 class="font-headline text-[17px] text-primary font-bold">Is this investment advice?</h3>
          <span class="w-7 h-7 shrink-0 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span>
        </summary>
        <p class="mt-4 font-body text-body-md text-secondary leading-relaxed pt-4 border-t border-hairline">
          No. Yomo is not a SEBI-registered investment adviser, does not sell or distribute investment products, and takes no commission from anyone. Roast, Pro and Zen are three ways of explaining your own numbers — analytics and education, not personalised advice.
        </p>
      </details>
    </div>
  </section>

  <!-- Final CTA -->
  <section class="w-full max-w-7xl mx-auto px-6 lg:px-12 py-16">
    <div class="rounded-3xl bg-primary-container text-on-primary p-8 lg:p-16 relative overflow-hidden shadow-lift border border-white/10">
      <div class="absolute -top-24 -right-24 w-96 h-96 rounded-full bg-[#fde047]/15 blur-3xl pointer-events-none"></div>
      <div class="absolute -bottom-24 -left-24 w-96 h-96 rounded-full bg-[#65dd96]/15 blur-3xl pointer-events-none"></div>
      <div class="relative z-10 max-w-2xl">
        <div class="inline-flex items-center gap-2.5 px-3.5 py-1 rounded-full bg-white/10 border border-white/15 text-[#82fab0] mb-4">
          <span class="w-2 h-2 rounded-full bg-[#82fab0] animate-pulse"></span>
          <span class="font-label text-label-sm uppercase font-bold tracking-wider">Private beta · invite only</span>
        </div>
        <h2 class="font-display text-[36px] leading-[44px] lg:text-[48px] lg:leading-[56px] font-extrabold text-on-primary tracking-tight">Ready for clear money math?</h2>
        <p class="mt-4 font-body text-body-lg text-on-primary-container max-w-xl leading-relaxed">
          Get the whole picture — runway, investments and taxes in rupees — without handing over a bank password.
        </p>
        <div class="mt-8 max-w-md">
          {request_form('Yomo invite request — site CTA')}
        </div>
        <p class="mt-4 font-body text-body-sm text-on-primary-container/80">Read-only by design · 21 bank alert formats · no credit card to start</p>
      </div>
    </div>
  </section>
</main>
"""
