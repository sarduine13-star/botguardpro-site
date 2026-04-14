# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r".\src\App.jsx")
content = p.read_text(encoding="utf-8")

marker = """function SocialProof() {"""

component = """
function FoundersBeta() {
  return (
    <section style={{
      padding: "70px 20px",
      background: "linear-gradient(180deg, #08111f 0%, #0b1324 100%)",
      borderTop: "1px solid rgba(0,255,136,0.12)",
      borderBottom: "1px solid rgba(0,255,136,0.12)"
    }}>
      <div style={{ maxWidth: 900, margin: "0 auto", textAlign: "center" }}>
        <div style={{
          display: "inline-block",
          padding: "6px 12px",
          border: "1px solid rgba(0,255,136,0.25)",
          borderRadius: "999px",
          color: "#00ff88",
          fontSize: 12,
          fontWeight: 800,
          letterSpacing: "0.18em",
          marginBottom: "16px",
          fontFamily: "'Space Mono', monospace"
        }}>
          FOUNDERS BETA • LIMITED ACCESS
        </div>

        <h2 style={{
          fontFamily: "'Syne', sans-serif",
          fontSize: "clamp(1.8rem, 3.5vw, 2.7rem)",
          fontWeight: 900,
          color: "#ffffff",
          marginBottom: "16px",
          letterSpacing: "-1px"
        }}>
          Join the BotGuard Pro Founders Beta
        </h2>

        <p style={{
          maxWidth: 720,
          margin: "0 auto 28px",
          color: "rgba(255,255,255,0.72)",
          fontSize: "1.05rem",
          lineHeight: 1.7,
          fontFamily: "'DM Sans', sans-serif"
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
          marginBottom: "24px",
          fontFamily: "'DM Sans', sans-serif"
        }}>
          <div>✓ Free Access for 90 Days</div>
          <div>✓ Automated Bot Traffic Audit</div>
          <div>✓ Real-Time Revenue Loss Insights</div>
          <div>✓ AI-Powered Detection & Reporting</div>
          <div>✓ Locked-In Lifetime Founder Pricing</div>
          <div>✓ No Credit Card Required</div>
        </div>

        <div style={{
          color: "#00ff88",
          fontWeight: 800,
          marginBottom: "24px",
          fontSize: "1rem",
          fontFamily: "'DM Sans', sans-serif"
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
              background: "linear-gradient(90deg, #00ff88 0%, #7dffb2 100%)",
              color: "#03120d",
              padding: "14px 26px",
              borderRadius: "12px",
              textDecoration: "none",
              fontWeight: 800,
              boxShadow: "0 0 24px rgba(0,255,136,0.22)",
              fontFamily: "'DM Sans', sans-serif"
            }}
          >
            Claim Free Beta
          </a>

          <a
            href="#calculator"
            style={{
              display: "inline-block",
              border: "1px solid rgba(0,255,136,0.55)",
              color: "#00ff88",
              padding: "14px 26px",
              borderRadius: "12px",
              textDecoration: "none",
              fontWeight: 800,
              background: "rgba(255,255,255,0.02)",
              fontFamily: "'DM Sans', sans-serif"
            }}
          >
            Run Free Audit
          </a>
        </div>

        <div style={{
          color: "rgba(255,255,255,0.5)",
          fontSize: "0.92rem",
          fontFamily: "'DM Sans', sans-serif"
        }}>
          Setup in under 10 minutes | Cancel anytime
        </div>
      </div>
    </section>
  );
}

"""

if "function FoundersBeta()" in content:
    print("COMPONENT ALREADY EXISTS")
else:
    if marker not in content:
        raise SystemExit("Could not find SocialProof marker. No changes made.")
    content = content.replace(marker, component + marker, 1)
    p.write_text(content, encoding="utf-8")
    print("COMPONENT ADDED:", p)
