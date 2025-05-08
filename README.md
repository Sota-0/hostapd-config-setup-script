# 🛠️ Hostapd Configurator CLI Tool

A terminal-based Python utility for interactively configuring `hostapd.conf` files. This tool allows users to set parameters, save/load presets, and write configuration files using a color-coded command-line interface.

---

## 📖 Features

- Interactive CLI interface for editing `hostapd.conf`
- Color-coded indicators for parameters that need configuration
- Save and load configuration presets from `hostapd_presets/`
- Display current configuration contents
- Write directly to `hostapd.conf`
- Built-in help menus for each section
- Option to configure Wi-Fi settings like interface, SSID, BSSID, channel, and WEP keys

---

## 💻 Example Commands

```bash
SET ssid MyNetwork        # Set SSID
SET interface wlan0       # Set interface
WRITE                     # Write current config to hostapd.conf
PRESET office_ap          # Save current config as a preset
load office_ap            # Load a preset from saved configs
show office_ap            # Display contents of a preset
HELP                      # Show help menu

## 📁 Presets

Presets are stored in the `hostapd_presets/` directory as `.conf` files. These presets represent fully configured `hostapd.conf` files that can be loaded back into the script for reuse. You can save your current configuration as a preset and later load it when needed.

### Preset Commands

- **PRESET <name>**: Save the current `hostapd.conf` configuration as a preset.
  - Example: `PRESET OfficeAP`
  
- **load <preset>**: Load a previously saved preset into `hostapd.conf`.
  - Example: `load OfficeAP`

- **show <preset>**: Display the contents of a preset.
  - Example: `show OfficeAP`

- **back**: Return to the previous menu.

---

## 🖥️ Interactive Setup Flow

The tool is divided into two main options, allowing for both configuration and preset management.

### 1. Hostapd Setup Menu (Option 1)

When selecting the **Setup** option, the following process will unfold:

1. **Display Current Configuration**: The tool will show the current `hostapd.conf` parameters, with color-coded indicators:
   - **Green**: Parameters that have been successfully configured.
   - **Red**: Parameters that are still pending configuration.
   
2. **Set Parameters**: Use the `SET [option] [new_value]` command to modify any parameter, such as SSID, BSSID, channel, etc.
   - Example: `SET ssid MyNetwork`
   
3. **Write to File**: After completing all configurations, use the `WRITE` command to save your settings into the `hostapd.conf` file.
   - Example: `WRITE`

4. **Save as Preset**: You can save your configuration as a preset for future use by typing `PRESET <name>`.
   - Example: `PRESET OfficeAP`

5. **Help Menu**: Access specific help information about the available commands by typing `HELP`.

6. **Exit**: To safely exit the setup process, type `exit`.

### 2. Preset Management (Option 2)

The **Preset** option allows you to manage the saved presets stored in the `hostapd_presets/` directory.

1. **Show Presets**: Type `show` to list all available preset files.

2. **Load Preset**: You can load any preset configuration using the `load <preset_name>` command.
   - Example: `load OfficeAP`
   
3. **Display Preset Content**: Use `show <preset_name>` to view the contents of a saved preset.
   - Example: `show OfficeAP`

4. **Back**: Type `back` to return to the previous menu.

---

## 📜 Example `hostapd.conf`

Once configured, your `hostapd.conf` might look something like this:

```ini
interface=wlan0
driver=nl80211
ssid=MyNetwork
bssid=00:14:22:01:23:45
hw_mode=g
channel=6
auth_algs=1
wep_default_key=0
wep_key0=SuperSecretPassword
