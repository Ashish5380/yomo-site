"""Pricing, security and about page bodies."""
from build_site import icon, MAIL
from pages_index import request_form

CHECK = icon('check', 'w-4 h-4 text-[#047857] shrink-0 mt-0.5', '2.5')
DASH = '<span class="text-outline-variant">—</span>'

CTA_BLOCK = f"""
  <section class="w-full max-w-7xl mx-auto px-6 lg:px-12 py-16" id="request">
    <div class="rounded-3xl bg-primary-container text-on-primary p-8 lg:p-14 relative overflow-hidden shadow-lift border border-white/10">
      <div class="absolute -top-24 -right-24 w-96 h-96 rounded-full bg-[#fde047]/15 blur-3xl pointer-events-none"></div>
      <div class="relative z-10 max-w-2xl">
        <div class="inline-flex items-center gap-2.5 px-3.5 py-1 rounded-full bg-white/10 border border-white/15 text-[#82fab0] mb-4">
          <span class="w-2 h-2 rounded-full bg-[#82fab0] animate-pulse"></span>
          <span class="font-label text-label-sm uppercase font-bold tracking-wider">Private beta · invite only</span>
        </div>
        <h2 class="font-display text-[34px] leading-[42px] lg:text-[44px] lg:leading-[52px] font-extrabold tracking-tight">See your own numbers clearly.</h2>
        <p class="mt-3 font-body text-body-lg text-on-primary-container max-w-xl leading-relaxed">Request an invite — tell us your email and we'll reply from {MAIL} with the next step.</p>
        <div class="mt-7 max-w-md">
          {request_form('Yomo invite request — subpage CTA')}
        </div>
      </div>
    </div>
  </section>
"""


PRICING = f"""
<main class="w-full pt-20">
  <section class="max-w-7xl mx-auto px-6 lg:px-12 pt-14 pb-10 w-full">
    <div class="text-center max-w-2xl mx-auto rise">
      <span class="font-label text-label-sm uppercase tracking-wider text-secondary font-bold">Pricing</span>
      <h1 class="mt-3 font-display text-[40px] leading-[48px] lg:text-[52px] lg:leading-[58px] text-primary font-extrabold tracking-[-0.03em]">Three plans. No lock-in.</h1>
      <p class="mt-4 font-body text-body-lg text-secondary">
        The free plan is genuinely usable. Plus adds the detail. Pro adds taxes and forward-looking maths. Exporting your data, deleting it and correcting a transaction stay free on every plan.
      </p>
    </div>
  </section>

  <section class="max-w-7xl mx-auto px-6 lg:px-12 pb-16 w-full" id="plans">
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 items-stretch">
      <div class="bg-surface-container-lowest rounded-2xl p-8 border border-hairline flex flex-col justify-between rise">
        <div>
          <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Free</span>
          <div class="mt-3 flex items-baseline gap-1"><span class="font-display text-[40px] leading-[46px] font-extrabold text-primary tnum">₹0</span><span class="font-body text-body-md text-secondary">/ forever</span></div>
          <p class="font-body text-body-md text-secondary mt-2">The daily numbers, without a card.</p>
          <ul class="mt-6 flex flex-col gap-3 font-body text-body-md text-primary">
            <li class="flex items-start gap-2">{CHECK}<span>5 chat questions a day</span></li>
            <li class="flex items-start gap-2">{CHECK}<span>30 days of transaction history</span></li>
            <li class="flex items-start gap-2">{CHECK}<span>Safe-to-spend, budgets and 1 goal</span></li>
            <li class="flex items-start gap-2">{CHECK}<span>Digest totals and essential alerts</span></li>
            <li class="flex items-start gap-2">{CHECK}<span>1 shared summary a week</span></li>
          </ul>
        </div>
        <a class="mt-8 h-12 rounded-xl border border-hairline bg-surface-container-lowest text-primary font-label text-label-lg flex items-center justify-center hover:bg-surface-container transition-colors" href="#request">Start free</a>
      </div>

      <div class="bg-primary-container text-on-primary rounded-2xl p-8 border border-white/10 shadow-lift relative overflow-hidden flex flex-col justify-between rise rise-1">
        <div class="absolute -top-28 -right-24 w-72 h-72 rounded-full bg-[#fde047]/15 blur-3xl pointer-events-none"></div>
        <div class="relative">
          <div class="flex items-center justify-between">
            <span class="font-label text-label-sm text-tertiary-fixed uppercase font-bold tracking-wider">Plus</span>
            <span class="font-label text-[10px] px-2 py-0.5 rounded-full bg-white/10 border border-white/15 text-[#82fab0] uppercase tracking-wider font-bold">Most people</span>
          </div>
          <div class="mt-3 flex items-baseline gap-1"><span class="font-display text-[40px] leading-[46px] font-extrabold tnum">₹399</span><span class="font-body text-body-md text-on-primary-container">/ month</span></div>
          <p class="font-body text-body-sm text-on-primary-container mt-1">₹3,990 a year — two months free</p>
          <ul class="mt-6 flex flex-col gap-3 font-body text-body-md">
            <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#82fab0] shrink-0 mt-0.5', '2.5')}<span>Everything in Free, without the daily cap</span></li>
            <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#82fab0] shrink-0 mt-0.5', '2.5')}<span>Full history and unlimited goals</span></li>
            <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#82fab0] shrink-0 mt-0.5', '2.5')}<span>The leak list — every merchant behind a category</span></li>
            <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#82fab0] shrink-0 mt-0.5', '2.5')}<span>Portfolio depth: holdings, XIRR, drift</span></li>
            <li class="flex items-start gap-2">{icon('check', 'w-4 h-4 text-[#82fab0] shrink-0 mt-0.5', '2.5')}<span>Every alert, the spend map, the full weekly story</span></li>
          </ul>
        </div>
        <a class="mt-8 h-12 rounded-xl bg-[#82fab0] text-[#00210f] font-label text-label-lg font-bold flex items-center justify-center gap-2 hover:bg-[#65dd96] transition-colors relative" href="#request">Choose Plus {icon('arrow', 'w-4 h-4', '2.5')}</a>
      </div>

      <div class="bg-surface-container-lowest rounded-2xl p-8 border border-hairline flex flex-col justify-between rise rise-2">
        <div>
          <span class="font-label text-label-sm text-secondary uppercase font-bold tracking-wider">Pro</span>
          <div class="mt-3 flex items-baseline gap-1"><span class="font-display text-[40px] leading-[46px] font-extrabold text-primary tnum">₹899</span><span class="font-body text-body-md text-secondary">/ month</span></div>
          <p class="font-body text-body-sm text-secondary mt-1">₹7,999 a year — two months free</p>
          <ul class="mt-6 flex flex-col gap-3 font-body text-body-md text-primary">
            <li class="flex items-start gap-2">{CHECK}<span>Everything in Plus</span></li>
            <li class="flex items-start gap-2">{CHECK}<span>Old vs new tax pack, with the working</span></li>
            <li class="flex items-start gap-2">{CHECK}<span>What-if planner before you commit</span></li>
            <li class="flex items-start gap-2">{CHECK}<span>Unlimited connected accounts</span></li>
          </ul>
        </div>
        <a class="mt-8 h-12 rounded-xl border border-hairline bg-surface-container-lowest text-primary font-label text-label-lg flex items-center justify-center hover:bg-surface-container transition-colors" href="#request">Choose Pro</a>
      </div>
    </div>
    <p class="font-body text-body-sm text-secondary text-center mt-6">
      Prices in ₹, inclusive of taxes. Plans are activated by hand during the beta — request one and we'll set it up. Cancel anytime; your export and delete rights never depend on a plan.
    </p>
  </section>

  <section class="w-full bg-surface-container-low py-20 border-y border-hairline">
    <div class="max-w-5xl mx-auto px-6 lg:px-12">
      <h2 class="font-headline text-[30px] leading-[38px] text-primary font-extrabold tracking-tight text-center">What changes between plans</h2>
      <div class="mt-10 bg-surface-container-lowest rounded-2xl border border-hairline overflow-x-auto rise">
        <table class="w-full min-w-[600px] text-left border-collapse">
          <thead>
            <tr class="bg-surface-container-low">
              <th class="p-4 font-label text-label-md text-secondary text-left">Feature</th>
              <th class="p-4 font-label text-label-md text-secondary text-center w-24">Free</th>
              <th class="p-4 font-label text-label-md text-secondary text-center w-24">Plus</th>
              <th class="p-4 font-label text-label-md text-secondary text-center w-24">Pro</th>
            </tr>
          </thead>
          <tbody class="font-body text-body-md text-primary">
            <tr class="border-t border-hairline"><td class="p-4">Chat questions</td><td class="p-4 text-center tnum">5 / day</td><td class="p-4 text-center">Unlimited</td><td class="p-4 text-center">Unlimited</td></tr>
            <tr class="border-t border-hairline bg-surface-container-low/40"><td class="p-4">History</td><td class="p-4 text-center">30 days</td><td class="p-4 text-center">All</td><td class="p-4 text-center">All</td></tr>
            <tr class="border-t border-hairline"><td class="p-4">Goals</td><td class="p-4 text-center">1</td><td class="p-4 text-center">Unlimited</td><td class="p-4 text-center">Unlimited</td></tr>
            <tr class="border-t border-hairline bg-surface-container-low/40"><td class="p-4">Leak list (count is free, the list is Plus)</td><td class="p-4 text-center">{DASH}</td><td class="p-4 text-center text-[#047857] font-semibold">Included</td><td class="p-4 text-center text-[#047857] font-semibold">Included</td></tr>
            <tr class="border-t border-hairline"><td class="p-4">Portfolio depth — holdings, XIRR, drift</td><td class="p-4 text-center">Headline only</td><td class="p-4 text-center text-[#047857] font-semibold">Included</td><td class="p-4 text-center text-[#047857] font-semibold">Included</td></tr>
            <tr class="border-t border-hairline bg-surface-container-low/40"><td class="p-4">Weekly digest</td><td class="p-4 text-center">Totals</td><td class="p-4 text-center">Full story</td><td class="p-4 text-center">Full story</td></tr>
            <tr class="border-t border-hairline"><td class="p-4">Alerts</td><td class="p-4 text-center">Essentials</td><td class="p-4 text-center">Every alert</td><td class="p-4 text-center">Every alert</td></tr>
            <tr class="border-t border-hairline bg-surface-container-low/40"><td class="p-4">Spend map</td><td class="p-4 text-center">{DASH}</td><td class="p-4 text-center text-[#047857] font-semibold">Included</td><td class="p-4 text-center text-[#047857] font-semibold">Included</td></tr>
            <tr class="border-t border-hairline"><td class="p-4">Old vs new tax pack</td><td class="p-4 text-center">{DASH}</td><td class="p-4 text-center">{DASH}</td><td class="p-4 text-center text-[#047857] font-semibold">Included</td></tr>
            <tr class="border-t border-hairline bg-surface-container-low/40"><td class="p-4">What-if planner</td><td class="p-4 text-center">{DASH}</td><td class="p-4 text-center">{DASH}</td><td class="p-4 text-center text-[#047857] font-semibold">Included</td></tr>
            <tr class="border-t border-hairline"><td class="p-4">Unlimited connected accounts</td><td class="p-4 text-center">{DASH}</td><td class="p-4 text-center">{DASH}</td><td class="p-4 text-center text-[#047857] font-semibold">Included</td></tr>
            <tr class="border-t border-hairline bg-[#ecfdf5]"><td class="p-4 font-semibold">Export, delete my data, correct a transaction</td><td class="p-4 text-center text-[#047857] font-bold">Always</td><td class="p-4 text-center text-[#047857] font-bold">Always</td><td class="p-4 text-center text-[#047857] font-bold">Always</td></tr>
          </tbody>
        </table>
      </div>
      <p class="font-body text-body-sm text-secondary mt-4 text-center">Trust features are deliberately outside the billing system, so no plan can gate them.</p>
    </div>
  </section>

  <section class="max-w-5xl mx-auto px-6 lg:px-12 py-20" id="faq">
    <h2 class="font-headline text-[30px] leading-[38px] text-primary font-extrabold tracking-tight text-center mb-10">Billing questions</h2>
    <div class="flex flex-col gap-4">
      <details class="bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft">
        <summary class="flex items-center justify-between gap-4"><h3 class="font-headline text-[17px] text-primary font-bold">How is payment taken during the beta?</h3><span class="w-7 h-7 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span></summary>
        <p class="mt-4 pt-4 border-t border-hairline font-body text-body-md text-secondary leading-relaxed">By hand, on purpose. You request a plan from the app or by email, we confirm the price in writing and activate it. No card is stored by Yomo, and there is no auto-renewal you cannot see.</p>
      </details>
      <details class="bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft">
        <summary class="flex items-center justify-between gap-4"><h3 class="font-headline text-[17px] text-primary font-bold">What happens if I stop paying?</h3><span class="w-7 h-7 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span></summary>
        <p class="mt-4 pt-4 border-t border-hairline font-body text-body-md text-secondary leading-relaxed">The account drops to Free at the end of the period. Nothing is deleted, and exporting or deleting your data stays available.</p>
      </details>
      <details class="bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft">
        <summary class="flex items-center justify-between gap-4"><h3 class="font-headline text-[17px] text-primary font-bold">Can I switch plans or get a refund?</h3><span class="w-7 h-7 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span></summary>
        <p class="mt-4 pt-4 border-t border-hairline font-body text-body-md text-secondary leading-relaxed">Yes. Ask in the app or at <a class="text-primary font-semibold underline" href="mailto:{MAIL}">{MAIL}</a> and we will move you, pro-rate or refund the current period — a beta should not trap anyone.</p>
      </details>
      <details class="bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft">
        <summary class="flex items-center justify-between gap-4"><h3 class="font-headline text-[17px] text-primary font-bold">Do I need a credit card to start?</h3><span class="w-7 h-7 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span></summary>
        <p class="mt-4 pt-4 border-t border-hairline font-body text-body-md text-secondary leading-relaxed">No. The Free plan needs no payment details at all.</p>
      </details>
    </div>
  </section>

  {CTA_BLOCK}
</main>
"""

SECURITY = f"""
<main class="w-full pt-20">
  <section class="max-w-7xl mx-auto px-6 lg:px-12 pt-14 pb-16 w-full">
    <div class="text-center max-w-2xl mx-auto rise">
      <span class="font-label text-label-sm uppercase tracking-wider text-secondary font-bold">Security &amp; privacy</span>
      <h1 class="mt-3 font-display text-[40px] leading-[48px] lg:text-[52px] lg:leading-[58px] text-primary font-extrabold tracking-[-0.03em]">Read-only. Encrypted. Yours.</h1>
      <p class="mt-4 font-body text-body-lg text-secondary">
        Yomo can read the money that you connect, with your explicit consent. It can never move it, hold it or trade it — there is no code path for that.
      </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mt-14">
      <div class="p-6 rounded-2xl bg-surface-container-lowest border border-hairline shadow-soft flex flex-col gap-3 rise">
        <div class="w-10 h-10 rounded-xl bg-[#ecfdf5] text-[#047857] border border-[#a7f3d0]/60 flex items-center justify-center">{icon('eye', 'w-5 h-5', '2')}</div>
        <h2 class="font-headline text-headline-sm text-primary font-bold">Read-only by construction</h2>
        <p class="font-body text-body-md text-secondary">No payment, transfer or order-placement code exists in the product. Not a permission we promise — a capability we never built.</p>
      </div>
      <div class="p-6 rounded-2xl bg-surface-container-lowest border border-hairline shadow-soft flex flex-col gap-3 rise rise-1">
        <div class="w-10 h-10 rounded-xl bg-surface-container-low border border-hairline text-primary flex items-center justify-center">{icon('lock', 'w-5 h-5', '2')}</div>
        <h2 class="font-headline text-headline-sm text-primary font-bold">Encrypted at rest</h2>
        <p class="font-body text-body-md text-secondary">Alert text and statement payloads are stored encrypted; the database never holds them in plaintext. Traffic runs over TLS.</p>
      </div>
      <div class="p-6 rounded-2xl bg-surface-container-lowest border border-hairline shadow-soft flex flex-col gap-3 rise rise-2">
        <div class="w-10 h-10 rounded-xl bg-[#fef9c3] border border-[#fde047]/60 text-primary flex items-center justify-center">{icon('shield', 'w-5 h-5', '2')}</div>
        <h2 class="font-headline text-headline-sm text-primary font-bold">No products, no commissions</h2>
        <p class="font-body text-body-md text-secondary">Yomo is not a SEBI-registered adviser and sells nothing. No one pays us to rank a fund, a card or a broker.</p>
      </div>
      <div class="p-6 rounded-2xl bg-surface-container-lowest border border-hairline shadow-soft flex flex-col gap-3 rise rise-3">
        <div class="w-10 h-10 rounded-xl bg-surface-container-low border border-hairline text-primary flex items-center justify-center">{icon('x', 'w-5 h-5', '2')}</div>
        <h2 class="font-headline text-headline-sm text-primary font-bold">Consent you can revoke</h2>
        <p class="font-body text-body-md text-secondary">Disconnect Gmail, a broker, a forwarding address or the SMS reader inside the app. The feed stops at that moment.</p>
      </div>
    </div>
  </section>

  <section class="w-full bg-surface-container-low py-20 border-y border-hairline">
    <div class="max-w-4xl mx-auto px-6 lg:px-12">
      <h2 class="font-headline text-[30px] leading-[38px] text-primary font-extrabold tracking-tight">What Yomo actually reads</h2>
      <div class="mt-8 flex flex-col gap-4 font-body text-body-md text-secondary">
        <div class="p-5 rounded-xl bg-surface-container-lowest border border-hairline flex items-start gap-3">
          <span class="w-8 h-8 rounded-lg bg-surface-container-low border border-hairline flex items-center justify-center shrink-0 text-primary">{icon('mail', 'w-4 h-4', '2')}</span>
          <p><span class="text-primary font-semibold">Gmail bank alerts.</span> Google's read-only OAuth scope, limited to messages from the bank senders you approve. Yomo stores the parsed transaction — amount, date, merchant — not your mailbox.</p>
        </div>
        <div class="p-5 rounded-xl bg-surface-container-lowest border border-hairline flex items-start gap-3">
          <span class="w-8 h-8 rounded-lg bg-surface-container-low border border-hairline flex items-center justify-center shrink-0 text-primary">{icon('doc', 'w-4 h-4', '2')}</span>
          <p><span class="text-primary font-semibold">Statements and CAS.</span> PDFs and CSVs you upload or share: bank statements, credit-card bills and CAMS/KFintech, NSDL or CDSL consolidated statements for mutual funds and demat.</p>
        </div>
        <div class="p-5 rounded-xl bg-surface-container-lowest border border-hairline flex items-start gap-3">
          <span class="w-8 h-8 rounded-lg bg-surface-container-low border border-hairline flex items-center justify-center shrink-0 text-primary">{icon('chart', 'w-4 h-4', '2')}</span>
          <p><span class="text-primary font-semibold">Broker reads.</span> Zerodha through a Kite Connect read session you authorise, plus Groww and INDmoney connections. Holdings and positions are read; orders are never touched.</p>
        </div>
        <div class="p-5 rounded-xl bg-surface-container-lowest border border-hairline flex items-start gap-3">
          <span class="w-8 h-8 rounded-lg bg-surface-container-low border border-hairline flex items-center justify-center shrink-0 text-primary">{icon('phone', 'w-4 h-4', '2')}</span>
          <p><span class="text-primary font-semibold">Bank SMS, on Android only.</span> An allowlist of bank sender headers decides what leaves the phone. Personal messages and OTPs are never read or uploaded.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="max-w-4xl mx-auto px-6 lg:px-12 py-20 w-full" id="data-deletion">
    <h2 class="font-headline text-[30px] leading-[38px] text-primary font-extrabold tracking-tight">Delete everything, whenever.</h2>
    <p class="mt-3 font-body text-body-lg text-secondary">Two taps in Settings: export the ledger as CSV, or delete the account and its data permanently. No retention queue for your transactions, no waiting on support.</p>
    <div class="mt-8 p-6 rounded-2xl bg-surface-container-lowest border border-hairline shadow-soft flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <span class="w-10 h-10 rounded-xl bg-[#fee2e2] text-[#ef4444] border border-[#fca5a5] flex items-center justify-center shrink-0">{icon('x', 'w-5 h-5', '2')}</span>
        <div>
          <span class="font-label text-label-lg text-primary font-bold">Want a human to confirm it?</span>
          <p class="font-body text-body-sm text-secondary">Write to <a class="text-primary font-semibold underline" href="mailto:{MAIL}?subject=Data%20Deletion%20Request">{MAIL}</a> with the subject "Data Deletion Request".</p>
        </div>
      </div>
      <a class="h-12 px-6 rounded-xl bg-primary-container text-on-primary font-label text-label-lg flex items-center justify-center gap-2 hover:bg-primary transition-colors shrink-0" href="mailto:{MAIL}?subject=Data%20Deletion%20Request">Request deletion {icon('arrow', 'w-4 h-4', '2.2')}</a>
    </div>
    <p class="mt-4 font-body text-body-sm text-secondary">Nightly backups are kept for 14 days for disaster recovery and then removed; a deletion request also removes the account from the active database immediately.</p>
  </section>

  <section class="max-w-4xl mx-auto px-6 lg:px-12 pb-20 w-full" id="faq">
    <h2 class="font-headline text-[30px] leading-[38px] text-primary font-extrabold tracking-tight mb-8">Security FAQ</h2>
    <div class="flex flex-col gap-4">
      <details class="bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft">
        <summary class="flex items-center justify-between gap-4"><h3 class="font-headline text-[17px] text-primary font-bold">Is the sync really read-only?</h3><span class="w-7 h-7 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span></summary>
        <p class="mt-4 pt-4 border-t border-hairline font-body text-body-md text-secondary leading-relaxed">Yes, structurally. Google's scope is read-only, the broker session is a read session, statements are files you hand over, and the Android reader only forwards bank messages. There is no capability anywhere in Yomo to withdraw, transfer or trade.</p>
      </details>
      <details class="bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft">
        <summary class="flex items-center justify-between gap-4"><h3 class="font-headline text-[17px] text-primary font-bold">Does the language model see my data?</h3><span class="w-7 h-7 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span></summary>
        <p class="mt-4 pt-4 border-t border-hairline font-body text-body-md text-secondary leading-relaxed">Raw alert text and statement files never reach the model. It receives computed facts — totals, categories, merchant names, dates — and every rupee figure in a reply is produced in Python and checked before it is shown. Account numbers, OTPs and PANs are scrubbed from replies.</p>
      </details>
      <details class="bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft">
        <summary class="flex items-center justify-between gap-4"><h3 class="font-headline text-[17px] text-primary font-bold">How do I stop a feed?</h3><span class="w-7 h-7 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span></summary>
        <p class="mt-4 pt-4 border-t border-hairline font-body text-body-md text-secondary leading-relaxed">Connections in Settings. Disconnecting Gmail revokes the token, removing a forwarding address stops new mail, and uninstalling the Android app ends the SMS reader. Historical rows stay until you delete them — that is the point of the delete control.</p>
      </details>
      <details class="bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft">
        <summary class="flex items-center justify-between gap-4"><h3 class="font-headline text-[17px] text-primary font-bold">Do you sell my data or show ads?</h3><span class="w-7 h-7 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span></summary>
        <p class="mt-4 pt-4 border-t border-hairline font-body text-body-md text-secondary leading-relaxed">No. No ads, no data sale, no lead-gen for lenders or card issuers, and no affiliate placement pretending to be a recommendation. You pay for the product; that is the business model.</p>
      </details>
      <details class="bg-surface-container-lowest rounded-2xl p-6 border border-hairline shadow-soft">
        <summary class="flex items-center justify-between gap-4"><h3 class="font-headline text-[17px] text-primary font-bold">Is Yomo giving me investment advice?</h3><span class="w-7 h-7 rounded-full bg-surface-container-low flex items-center justify-center chev text-secondary">{icon('chevron', 'w-4 h-4', '2.2')}</span></summary>
        <p class="mt-4 pt-4 border-t border-hairline font-body text-body-md text-secondary leading-relaxed">No. Yomo is not a SEBI-registered investment adviser and does not sell investment products. Roast, Pro and Zen describe your own numbers — analytics and education, not personalised advice.</p>
      </details>
    </div>
  </section>

  {CTA_BLOCK}
</main>
"""

ABOUT = f"""
<main class="w-full pt-20">
  <section class="max-w-7xl mx-auto px-6 lg:px-12 pt-14 pb-16 w-full">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
      <div class="lg:col-span-7 flex flex-col gap-5 rise">
        <span class="inline-flex w-fit items-center gap-2 px-3.5 py-1.5 rounded-full bg-[#ecfdf5] border border-[#a7f3d0]/60 text-[#047857] font-label text-label-sm">
          <span class="w-1.5 h-1.5 rounded-full bg-[#10b981]"></span> Chat-first · Read-only · Made in India
        </span>
        <h1 class="font-display text-[40px] leading-[48px] lg:text-[54px] lg:leading-[60px] text-primary font-extrabold tracking-[-0.03em]">A money app that talks like a friend and counts like an accountant.</h1>
        <p class="font-body text-body-lg text-secondary">
          Most money apps give you a dashboard and let you do the thinking. Yomo flips it: ask in plain words — "how much went to food this month?", "can I afford Goa?", "old regime or new?" — and get an answer in rupees that is actually computed from your own records.
        </p>
        <p class="font-body text-body-lg text-secondary">
          It reads the alerts and documents you already receive: Gmail bank alerts, forwarded emails, statements you upload, and on Android the bank SMS on your phone. It never asks for a bank login, never stores an OTP, and cannot move a rupee.
        </p>
        <p class="font-body text-body-lg text-primary font-semibold">The mission is simple: every Indian should be able to read their own money.</p>
        <div class="flex flex-wrap items-center gap-3 pt-2">
          <a class="h-12 px-7 rounded-xl bg-primary-container text-on-primary font-label text-label-lg font-bold flex items-center justify-center gap-2 hover:bg-primary transition-colors" href="index.html#request">Request an invite {icon('arrow', 'w-4 h-4', '2.2')}</a>
          <a class="h-12 px-6 rounded-xl border border-hairline bg-surface-container-lowest text-primary font-label text-label-lg flex items-center justify-center gap-2 hover:bg-surface-container transition-colors" href="mailto:{MAIL}">{icon('mail', 'w-4 h-4', '2')} {MAIL}</a>
        </div>
      </div>
      <div class="lg:col-span-5 flex flex-col items-center gap-6 rise rise-1">
        <div class="relative">
          <div class="absolute inset-0 rounded-3xl bg-[#e6007e]/15 blur-2xl"></div>
          <div class="relative w-44 h-44 rounded-3xl overflow-hidden border border-hairline bg-surface-container-low shadow-soft mascot-float">
            <img alt="Yomo mascot" class="w-full h-full object-contain p-1" src="assets/mascot.png"/>
          </div>
        </div>
        <div class="w-full max-w-sm rounded-2xl bg-surface-container-lowest border border-hairline shadow-soft p-6 flex flex-col gap-3">
          <div class="flex items-center justify-between">
            <span class="font-label text-label-lg text-primary font-bold">Talk to the humans</span>
            <span class="font-label text-label-sm px-2 py-0.5 rounded-full bg-surface-container-low text-secondary border border-hairline font-bold">We reply</span>
          </div>
          <p class="font-body text-body-md text-secondary">Questions, feedback, partnerships or press — write to <a class="text-primary font-semibold underline" href="mailto:{MAIL}">{MAIL}</a>.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="w-full bg-surface-container-low py-20 border-y border-hairline">
    <div class="max-w-7xl mx-auto px-6 lg:px-12 grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="p-7 rounded-2xl bg-surface-container-lowest border border-hairline shadow-soft flex flex-col gap-3 rise">
        {icon('chat', 'w-6 h-6 text-[#047857]', '1.8')}
        <h2 class="font-headline text-headline-sm text-primary font-bold">Chat first, always</h2>
        <p class="font-body text-body-md text-secondary">If you can text, you can use Yomo. No tabs, no pivot tables, no onboarding video about "financial wellness".</p>
      </div>
      <div class="p-7 rounded-2xl bg-surface-container-lowest border border-hairline shadow-soft flex flex-col gap-3 rise rise-1">
        {icon('eye', 'w-6 h-6 text-[#047857]', '1.8')}
        <h2 class="font-headline text-headline-sm text-primary font-bold">Read-only by design</h2>
        <p class="font-body text-body-md text-secondary">Consent-driven feeds and a product with no transfer code. Yomo can see, never touch.</p>
      </div>
      <div class="p-7 rounded-2xl bg-surface-container-lowest border border-hairline shadow-soft flex flex-col gap-3 rise rise-2">
        {icon('shield', 'w-6 h-6 text-[#047857]', '1.8')}
        <h2 class="font-headline text-headline-sm text-primary font-bold">No products, no commissions</h2>
        <p class="font-body text-body-md text-secondary">Not an adviser, not a distributor. The only incentive is that the numbers are right.</p>
      </div>
    </div>
  </section>

  <section class="max-w-4xl mx-auto px-6 lg:px-12 py-20 w-full">
    <h2 class="font-headline text-[30px] leading-[38px] text-primary font-extrabold tracking-tight">How it is built</h2>
    <div class="mt-8 flex flex-col gap-5 font-body text-body-lg text-secondary">
      <p class="pt-5 border-t border-hairline"><span class="text-primary font-semibold">The model never does the arithmetic.</span> Every balance, total, percentage and projection is computed in code in integer paise, turned into a rupee string, and handed to the assistant to quote. If a reply needs a number, the number was calculated first — a rule enforced in the system, not asked for in a prompt.</p>
      <p class="pt-5 border-t border-hairline"><span class="text-primary font-semibold">Three voices, one set of facts.</span> Roast tells you the truth sharply, Pro gives you the analysis, Zen gives you calm guardrails. Roast unlocks after your first week, once there is enough real history to be fair about it.</p>
      <p class="pt-5 border-t border-hairline"><span class="text-primary font-semibold">Built in India for Indian money.</span> Salary dates, UPI narrations, 21 banks' alert formats, credit-card cycles, CAS statements, SIPs and two tax regimes are first-class objects — not localisations bolted on later.</p>
      <p class="pt-5 border-t border-hairline"><span class="text-primary font-semibold">Small, deliberate releases.</span> Yomo runs as a private beta. Features land when they are tested against real statements, and the free plan stays useful on purpose.</p>
    </div>
  </section>

  {CTA_BLOCK}
</main>
"""
