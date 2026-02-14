# 💊 Smart Pill Dispenser

An intelligent healthcare appliance designed to assist elderly patients or those on complex medication schedules by automating pill dispensing and tracking adherence.

## 🚀 Features
- **Precision Timing:** Internal RTC (Real-Time Clock) triggers dispensing at exact intervals.
- **Compliance Tracking:** Logs every time a pill is taken or if a dose is missed.
- **Remote Caregiver Alerts:** Pings the dashboard if the patient fails to retrieve medication.
- **Secure Telemetry:** Leverages the MKR 1010's crypto-chip for secure data transmission.

## ⚙️ Engineering Logic
- **Hardware:** Arduino MKR 1010 controls a 360-degree continuous rotation servo to rotate a multi-compartment pill tray.
- **Software:** Python processes "Retrieval" events and generates a weekly compliance percentage chart.
