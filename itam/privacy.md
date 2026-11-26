---
title: CJW-Apps ITAM — Privacy Policy
---

<p class="crumbs"><a href="../business/"><img class="crumb-icon" src="../assets/brand/cjw-business-icon.svg" alt="" width="18" height="18">Business</a> › <a href="./">CJW-Apps ITAM</a> › Privacy policy</p>

# CJW-Apps ITAM — Privacy Policy

*CJW Apps · Last updated 15 November 2026*

CJW-Apps ITAM is an IT asset management program for Windows. It runs on
your own PC and keeps its data there. This policy explains what the
program does with information. In short: **we don't collect anything.**
There is no account with us, no analytics, no advertising and no server
of ours that your data goes to.

## What stays on your PC

Everything ITAM keeps is stored only on the PC it runs on:

- your inventory: assets, their users, departments and locations,
  purchase and warranty details, software licences and hardware models;
- the people who may sign in to ITAM: their names, user names, email
  addresses and roles. Passwords are stored only as salted hashes;
- the change log of who changed what, and when;
- the logins you save for network discovery, and the keys for Microsoft
  Intune and Google Workspace. These are encrypted with Windows' own
  data protection and can only be read on that PC by that Windows user;
- backups, in the folder you choose;
- a small diagnostic log, which never contains passwords or keys.

If you share ITAM with colleagues on your network, their browsers talk
to your PC over an encrypted (HTTPS) connection. Nothing goes outside
your network.

## Who is responsible for the information

ITAM is a tool your organisation runs. The information you put in it,
including the names of your staff, is yours: your organisation decides
what is recorded, who can see it and how long it is kept. CJW Apps never
receives it and cannot see it.

## Services ITAM contacts

ITAM only contacts an outside service when an administrator sets that
feature up. Each one receives what any website receives (such as your IP
address) and the sign-in or request described.

| Service | When | What it is used for |
|---|---|---|
| Microsoft (sign-in) | If you allow signing in to ITAM with Microsoft accounts | The person signs in on Microsoft's own page; ITAM receives their name and email address |
| Microsoft Intune (Microsoft Graph) | If you connect Intune | ITAM **reads** your managed devices, to add them to the inventory. It changes nothing in Intune |
| Google (sign-in) | If you allow signing in to ITAM with Google accounts | The person signs in on Google's own page; ITAM receives their name and email address |
| Google Workspace | If you connect Google Workspace | ITAM **reads** your organisation's devices and licence counts, to add them to the inventory. It changes nothing in Google Workspace |
| Microsoft Store | In the copy installed from the Microsoft Store | Checks whether ITAM Pro is active. Microsoft handles the subscription and payment; ITAM never sees payment details |
| Devices on your own network | When you run network discovery | ITAM asks the devices in the ranges you choose what they are, using the logins you saved |

The information read from Microsoft and Google is stored only in ITAM on
your PC. It is not sent to CJW Apps or to anybody else. You can
disconnect either service in ITAM at any time, and remove ITAM's access
in your Microsoft or Google administrator settings. Microsoft's and
Google's own privacy policies apply to your accounts with them.

ITAM's use of information received from Google APIs adheres to the
[Google API Services User Data
Policy](https://developers.google.com/terms/api-services-user-data-policy),
including the Limited Use requirements.

## Removing your information

- Delete assets, licences and users in ITAM itself; **Reset** in
  Settings returns it to an empty state.
- Uninstalling the Microsoft Store copy removes ITAM's data from that
  PC, including backups left in the default folder. Make a backup to
  another folder first if you want to keep it.
- The folder and portable copies keep their data in their own folder:
  delete the folder to remove it.

## Children

ITAM is a business tool and is not directed at children.

## Changes

If this policy changes, the new version is published on this page with
a new date.

## Contact

CJW Apps · [{{ site.email }}](mailto:{{ site.email }})
