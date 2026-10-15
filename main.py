import streamlit as st
import re

st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🛡️",
    layout="centered")
st.title("🛡️ Password Strength Checker")
st.write(
    "Analyze the strength of your password against standard security benchmarks in real time.")
show_password = st.checkbox("Show password characters")
password = st.text_input(
    label="Enter Password",
    type="text" if show_password else "password",
    placeholder="Type a password to test...",
    help="Notice: Do not use real personal credentials. Use sample test passwords only.")

if password:
    c_length = len(password) >= 8
    c_upper = bool(re.search(r"[A-Z]", password))
    c_lower = bool(re.search(r"[a-z]", password))
    c_digit = bool(re.search(r"\d", password))
    c_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    criteria_list = [
        ("Minimum length (8+ characters)", c_length, "Make your password at least 8 characters long."),
        ("At least one uppercase letter (A-Z)", c_upper, "Include at least one uppercase letter (e.g., A, B, C)."),
        ("At least one lowercase letter (a-z)", c_lower, "Include at least one lowercase letter (e.g., a, b, c)."),
        ("At least one numeric digit (0-9)", c_digit, "Include at least one digit (e.g., 0-9)."),
        ("At least one special character (!@#$%...)", c_special, "Include at least one special symbol (!, @, #, $, etc.).")]
    score = sum(passed for _, passed, _ in criteria_list)
    progress_val = score / 5.0
    st.divider()
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric(label="Strength Score", value=f"{score} / 5")
    with col2:
        st.write("**Overall Security Meter**")
        st.progress(progress_val)
    if score <= 2:
        st.error("🔴 **Strength Level: WEAK** (Meets 0–2 criteria)")
    elif score in (3, 4):
        st.warning("🟡 **Strength Level: MODERATE** (Meets 3–4 criteria)")
    else:
        st.success("🟢 **Strength Level: STRONG** (Meets all 5 criteria)")
    st.subheader("📋 Evaluation Checklist")
    for title, passed, _ in criteria_list:
        if passed:
            st.markdown(f"- ✅ **Passed:** {title}")
        else:
            st.markdown(f"- ❌ **Failed:** {title}")
    st.subheader("💡 Suggestions for Improvement")
    unmet = [advice for _, passed, advice in criteria_list if not passed]
    if unmet:
        for item in unmet:
            st.info(f"👉 {item}")
    else:
        st.balloons()
        st.success("🎉 Excellent! Your password meets all security criteria.")
    st.caption(f"Total Character Count: **{len(password)}**")
else:
    st.info("👆 Enter a test password above to view the analysis, checklist, and suggestions.")
