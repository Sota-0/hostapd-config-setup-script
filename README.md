# 🧰 Hostapd Configuration Assistant

A terminal-based interactive assistant for configuring and managing `hostapd.conf` files. This Python tool streamlines the process of setting up Wi-Fi access points by allowing you to dynamically modify settings, save/load presets, and write valid `hostapd` configurations with a clean, color-coded interface.

---

## ✨ Features

- 🎨 Color-coded terminal UI using `colorama`
- ⚙️ Dynamic `SET <option> <value>` commands to update `hostapd.conf` settings
- 💾 Save and load presets from the `hostapd_presets/` folder
- 👁️ Live preview of your configuration
- 🆘 Built-in help menus with usage examples
- 📁 Easily export and apply changes to `hostapd.conf`

---

## ⚙️ Supported Configuration Options

You can edit the following `hostapd.conf` parameters:
- `interface` — Network interface (e.g., wlan0)
- `driver` — Wireless driver (e.g., nl80211)
- `ssid` — Network SSID
- `bssid` — MAC address of the access point
- `hw_mode` — Band: `g` for 2.4GHz, `a` for 5GHz
- `channel` — Wi-Fi channel
- `auth_algs` — Authentication mode
- `wep_default_key` — WEP key index (0–3)
- `wep_key0` — WEP encryption key

Changes are reflected in real time via the color-coded interface.

---

## 🗂️ Preset Management

Presets are saved in the `hostapd_presets/` directory and can be:
- 🔄 **Loaded** using: `load <preset>`
- 👁️ **Viewed** using: `show <preset>`
- 💾 **Saved** with: `PRESET <name>`

Example:

```
$> PRESET office_ap
$> load office_ap
$> show office_ap
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/yourusername/hostapd-config-assistant.git
cd hostapd-config-assistant
```

### 2. Install Required Packages

```
pip install colorama
```

### 3. Run the Tool

```
python3 hostapd_setup.py
```

---

## 🖥️ Example Session

```
Hostapd : 1.SETUP  or  2.PRESET
$> 1
$> SET ssid MyNetwork
$> SET bssid 00:11:22:33:44:55
$> SET channel 6
$> WRITE
$> PRESET home_ap
```

---

## 📋 Notes

- This tool **does not** start `hostapd`; it only manages the configuration file.
- Ensure the interface and driver are valid and supported on your system.
- Presets are stored as `.conf` files and can be reused or edited manually.

---

## 📁 Project Structure

```
hostapd-config-assistant/
├── hostapd_setup.py
├── hostapd.conf
└── hostapd_presets/
    └── example_preset.conf
```

---

## 🛠 Built With

- Python 3.x
- [colorama](https://pypi.org/project/colorama/)

Install dependencies with:

```
pip install colorama
```
or 
```
pip install -r requirements.txt
```

---

## 📝 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🤝 Contributions

PRs, issues, and suggestions are welcome! If you’d like to improve or extend the tool, feel free to fork and submit a pull request.
