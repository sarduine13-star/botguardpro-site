# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r".\src\App.jsx")
content = p.read_text(encoding="utf-8")

target = """            Bots Are Costing You<br />More Than You Think</h2>"""

insert = """            Bots Are Costing You<br />More Than You Think</h2>
        </div>
      </section>

      <section style={{
        padding: "70px 20px",
        background: "linear-gradient(180deg, #08111f 0%, #0b1324 100%)",
        borderTop: "1px solid rgba(0,255,163,0.12)",
        borderBottom: "1px solid rgba(0,255,163,0.12)"
      }}>
        <div style={{ maxWidth: "900px", margin: "0 auto", textAlign: "center" }}>
          <div style={{
            display: "inline-block",
            padding: "6px 12px",
            border: "1px solid rgba(0,255,163,0.25)",
            borderRadius: "999px",
            color: "#00FFA3",
            fontSize: "12px",
            fontWeight: 800,
            letterSpacing: "0.18em",
            marginBottom: "16px"
          }}>
            FOUNDERS BETA • LIMITED ACCESS
          </div>

          <h2 style={{
            fontFamily: "'Syne', sans-serif",
            fontSize: "clamp(1.8rem, 3.5vw, 2.7rem)",
            fontWeight: 900,
            color: "#ffffff",
            marginBottom: "16px"
          }}>
            Join the BotGuard Pro Founders Beta
          </h2>

          <p style={{
            maxWidth: "720px",
            margin: "0 auto 28px",
            color: "rgba(255,255,255,0.72)",
            fontSize: "1.05rem",
            lineHeight: 1.7
          }}>
            Be among the first to uncover hidden revenue loss caused by fake traffic.
            Free for a limited number of early adopters.
          </p>

          <div style={{
            display: "inline-block",
            textAlign: "left",
            color: "#ffffff",
            lineHeight: 1.9,
            fontSize: "1rem",
            marginBottom: "24px"
          }}>
            <div>✓ Free Access for 90 Days</div>
            <div>✓ Automated Bot Traffic Audit</div>
            <div>✓ Real-Time Revenue Loss Insights</div>
            <div>✓ AI-Powered Detection & Reporting</div>
            <div>✓ Locked-In Lifetime Founder Pricing</div>
            <div>✓ No Credit Card Required</div>
          </div>

          <div style={{
            color: "#00FFA3",
            fontWeight: 800,
            marginBottom: "24px",
            fontSize: "1rem"
          }}>
            Only 25 Founding Accounts Available
          </div>

          <div style={{
            display: "flex",
            gap: "14px",
            justifyContent: "center",
            flexWrap: "wrap",
            marginBottom: "16px"
          }}>
            <a
              href="#pricing"
              style={{
                display: "inline-block",
                background: "linear-gradient(90deg, #00FFA3 0%, #7CFFB2 100%)",
                color: "#03120d",
                padding: "14px 26px",
                borderRadius: "12px",
                textDecoration: "none",
                fontWeight: 800,
                boxShadow: "0 0 24px rgba(0,255,163,0.22)"
              }}
            >
              Claim Free Beta
            </a>

            <a
              href="#calculator"
              style={{
                display: "inline-block",
                border: "1px solid rgba(0,255,163,0.55)",
                color: "#00FFA3",
                padding: "14px 26px",
                borderRadius: "12px",
                textDecoration: "none",
                fontWeight: 800,
                background: "rgba(255,255,255,0.02)"
              }}
            >
              Run Free Audit
            </a>
          </div>

          <div style={{
            color: "rgba(255,255,255,0.5)",
            fontSize: "0.92rem"
          }}>
            Setup in under 10 minutes | Cancel anytime
          </div>
        </div>
      </section>

      <section style={{"""

if target not in content:
    raise SystemExit("Target text not found exactly. No changes made.")

content = content.replace(target, insert, 1)
p.write_text(content, encoding="utf-8")
print("UPDATED:", p)
