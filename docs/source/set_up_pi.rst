.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _set_up_pi:

Setting Up Your Raspberry Pi
============================

The operating system is on the card. Now you need a way to talk to the Pi. There are two
routes, and you only need one of them:

* **With a screen** — connect a monitor, keyboard and mouse and use the desktop directly.
* **Headless (no screen)** — log in over Wi-Fi from your own computer.

.. note::
    On a Zero 2 W the **headless route is usually the easier one**: the board has a single
    USB data port, so a keyboard and mouse need a powered hub, and the ports are small and
    close together. You do not need a monitor at all if you complete the Raspberry Pi Imager
    settings described in :ref:`imager_custom`.

If You Have a Screen
--------------------

**Required Components**

* The Raspberry Pi Zero 2 W with the microSD card inserted
* 5 V / 2 A Micro USB power supply (not included)
* Monitor with an HDMI input
* The **Mini HDMI adapter** from the kit, plus a standard HDMI cable
* Keyboard — and a mouse if you want one
* The **Micro USB adapter** from the kit, and a **powered USB hub** to connect more than
  one USB device

**Steps**

#. With the power **disconnected**, fit the Mini HDMI adapter to the board's **HDMI**
   port, then run a standard HDMI cable to the monitor. Select the matching input on the
   monitor.

#. Fit the Micro USB adapter to the **USB** (data) port — **not** to **PWR IN** — and plug
   the keyboard in. For a keyboard *and* a mouse, put both on a powered hub and the hub on
   the adapter.

#. Insert the microSD card into the slot on the **underside** of the board.

#. **Finally**, connect the power supply to **PWR IN**. The Pi has no power switch;
   connecting power is how you switch it on.

#. After 30–60 seconds the Raspberry Pi OS desktop appears. The very first boot is slower,
   because the filesystem is being expanded to fill the card.

   .. image:: img/connect_pc.jpg
      :width: 80%
      :align: center
      :alt: The Zero 2 W in its case, connected to a monitor through the Mini HDMI adapter,
            with the USB data cable and the Micro USB power cable attached

   This is the whole assembly: **Mini HDMI adapter** to the monitor, the **Micro USB
   adapter** carrying the keyboard, and the power supply on **PWR IN**. Nothing plugs into
   the 40-pin header.

#. Open a **Terminal** from the taskbar, or press ``Ctrl`` + ``Alt`` + ``T``.

   .. image:: /_shared/pi_start/img/open_terminal.png
      :width: 80%
      :align: center

If You Have No Screen (Headless)
--------------------------------

Without a monitor you configure the Pi from your own computer and never connect a screen.
This is the recommended route for this kit.

**Required Components**

* The Raspberry Pi Zero 2 W with the microSD card inserted
* 5 V / 2 A Micro USB power supply (not included)
* Your own computer, on the **same network** as the Pi

**Before you power on, check that you completed these in Raspberry Pi Imager**

* Hostname set — you will reach the Pi as ``<hostname>.local``. Any name works; there is no
  default, so remember what you type.
* Username and password set
* Wireless LAN SSID, password and **country** set
* SSH enabled, with password authentication

**Tips**

* Ensure that the Pi and your computer are on the same local network.
* The Zero 2 W radio is **2.4 GHz only** — it cannot see a 5 GHz-only network.

**Connect via SSH**

#. Open a terminal on your computer (Windows: **PowerShell**; macOS/Linux: **Terminal**)
   and connect to your Raspberry Pi:

   .. code-block:: bash

      ssh <username>@<hostname>.local
      # Example, if you set the hostname to "zero2w" and the user to "pi":
      ssh pi@zero2w.local

#. Alternatively, locate your Pi's IP address in your router's DHCP list and connect with:

   .. code-block:: bash

      ssh <username>@<IP address>
      # Example:
      ssh pi@192.168.1.42

#. On first login, type ``yes`` to confirm the SSH host key.

#. Enter the password you configured in Raspberry Pi Imager. Nothing appears on screen while
   you type; that is normal, not a frozen terminal.

#. You now have a full command line on the Pi.

   .. image:: /_shared/pi_start/img/ssh_login.png
      :align: center

Troubleshooting
---------------

* **``ssh: Could not resolve hostname ...``**

  * Check the hostname is exactly the one you set in Imager.
  * Try connecting to the Pi's IP address instead.

* **``The term 'ssh' is not recognized...`` (Windows)**

  * OpenSSH is not installed.
  * See :ref:`openssh_powershell` or :ref:`login_windows`.

* **``Permission denied (publickey,password)``**

  * The username or password is not the one you created in Raspberry Pi Imager. Both are
    case-sensitive.

* **``Connection refused``**

  * Wait 1–2 minutes after powering on.
  * Confirm SSH was enabled in Raspberry Pi Imager before the card was written.

Graphical Remote Access
-----------------------

If you prefer a desktop rather than a command line:

* :ref:`remote_desktop` — enable **VNC** for a full desktop in a window on your computer.
* `Raspberry Pi Connect <https://www.raspberrypi.com/documentation/services/connect.html>`_ —
  reach the Pi's desktop in a browser, from any network. Documented by Raspberry Pi.

Either way you can now use the Pi without ever attaching a monitor.
