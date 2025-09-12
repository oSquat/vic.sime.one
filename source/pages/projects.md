Title: projects
Date: 1000-01-01 00:00


### Licensed Software Products
Unless otherwise noted, I was the primary or sole person in charge of design, development, documentation and support of the following companion products for Tigerpaw CRM.

* **QBTrak - accounting data export** | *VB6 / .NET; Microsoft SQL Server; QuickBooks SDK*

> An accounting data export from Tigerpaw to QuickBooks (an Intuit product). Written in VB6 and .NET.

* **Ignite - database automation & enhancement with triggers & functions** | *VB.NET; Microsoft SQL Server*

> A collection of database triggers & functions with accompanying utility for managing options that automated & enhanced Tigerpaw. The main reason for purchasing Ignite was to automatically applying General Ledger Cost & Income codes to individual line items on invoices to apply accounting values with added precision over what was available natively in Tigerpaw. 

* **Tantivy - scheduled reporting** | *VB.NET; Window Service; Microsoft SQL Server; Crystal Reports*

> A Windows service and accompanying GUI for configuration that leveraged existing reports available natively in Tigerpaw, allowing administrators & supervisors to schedule the generation & delivery of such reports. This all freed up time from employees that might otherwise be tasked with sending out reports in perpetuity or company leaders having to find and run a series of reports manually.

* **QBWizard - a "wizard" for configuring Tigerpaw from QuickBooks** | *VB.NET; Microsoft SQL Server; QuickBooks  SDK*

> An accounting-focused setup wizard for Tigerpaw pulled insights from a customer's existing QuickBooks company file. The QBWizard would create GL Accounts and apply settings necessary to tie Tigerpaw with QuickBooks for accounting exports or ask questions about how to proceed.

* **ReportsTiger.com** | *Python; OpenCart; Microsoft SQL Server; NSIS*

> ReportsTiger.com was an e-commerce website running OpenCart with added customization. After a sale, the purchased reports would be dynamically compiled into an installation package and distributed to the customer while the invoice and customer inventory was imported into our on-site database.

* **Barcode - hardware for taking physical inventory in Tigerpaw** | *Embedded VB3/VB6; Winsock TCP/IP; Microsoft SQL Server*

> Mobile development on the Symbol MC50 running Microsoft Pocket PC using VB6 / Embedded VB3.0. The device augmented the process of taking a physical inventory. Inventory counts were syncronize back counts by cradling the device on the PC or through a Winsock TCP/IP connection. The best thing I can say about this project was that it was mobile development that preceeded Android, iPhone, YouTube and was released the same year that Gmail debuted. 
	
* **Peachtrack - accounting data export** | *VB6; Microsoft SQL Server; Sage SDK*

> Designed and assisted with development of + maintained a Tigerpaw to Peachtree (a Peachtree product) accounting link. Written in VB6.
	
* **Avalara AvaTax - tax as a service integration**; *VB6; Microsoft SQL Server; AvaTax REST API*

> Designed and assisted with development of + maintained an integration between Tigerpaw and AvaTax, a service that returns tax rate details, line-by-line on an invoice, down to the street address of a customer. This provided our customers with precise tax values, saving money directly while also eliminating the need to manually maintain tax rate tables between Tigerpaw and their accounting system.
	
---

### Projects Related to Software Development
Additional projects or scripting related to the software development, but not sellable licensed software.

* **License Registration & Rights Management** - A SOAP-based Web Service for license registration allowing us to track usage, provide fully functional demos, and enforce licensing. This also opened the opportunity to sell under leasing agreements creating ongoing revenue streams.
* **Build System** - Scripted software builds with a batch files: compile from source, documentation, installation files, then zip & push installation packages to the webserver.
* **Revision Control** - Setup Subversion and later git for revision control.

---

### Telephony Projects
Projects under direction of the telecommunications division.

* **LANTA bus route IVR** | *VB.NET; UCConnect; Availtec API*

> Designed & developed an Interactive Voice Response (IVR) system allowing Lehigh & Northampton Transportation Authority (LANTA) customers to call in, enter their bus stop station ID and receive up-to-the-minute schedule details or delay notices. Developed on AVST's UCConnect platform with VB.NET, bus route data was pulled from an Avaltec API.

* **Telephony Appliance** | *Linux; Python; Flask; Postgres; DHCP; SNMP*

> I installed Linux on a single board computer configured to support telephony deployments at customer sites. These appliances provided:
>
> * DHCP to phones and wireless AP's, ran a TFTP service for distributing firmware updates, and had a web interface that provided details about DHCP leases and ARP scan results which aided technicians deploying or troubleshooting a system.
> * "Eyes in the network" to facilitate troubleshooting, allowing us to ping or port scan endpoints to validate availability.
> * An SNMP sink to receive messages from the phone system. These messages were analyzed and email alerts were sent out when problems were detected. We were often able to notify the customer that we had identified and were investigating an issue before they even knew about it.

* **Call Accounting** | *Flask; Microsoft SQL; VB.NET; NEC / Zultys*

> Developed an in-house call accounting system to collect call records (metadata) from customer sites for analysis and reporting. 
> 
> Phone systems were configured output Station Message Detail Recording (SMDR) records. A TCP-based cloud collector or on-site Scannex "ip.buffer" collected record streams from the phone system. Records were then sent to a web service for collection and saved to database. I assisted in integrating the database to an existing in-house web portal so customers could view reports or schedule delivery via e-mail. A Windows service I wrote in VB.NET generated and sent scheduled reports.
>
> Supported NEC phone systems 2000 IPS, NEAX 2400, SV8100/9100, SV8300/9300, SV8500/9500 and Zultys systems MX30, MX250, MX-SE, MX-E, and MXvirtual with a Nortel SL-1 compatible record format.
>
> Results:
>
> * Send e-mail and SMS (via Twilio) alerts when 911 was dialed. Management, loss prevention, or security guards could be alerted to emergency activity immediately after a call ended.
> * Traffic studies (see TrueTrunk) to reduce costs and estimate SIP migration pricing
> * Assist with investigations (e.g. human resources, loss prevention or threats)

* **Automated voicemail backups for the NEC UM8700 platform** | *Flask; NEC; bash*

> The UM8700 ran a trim, embedded version of Linux. The platform supported scheduling backups on-device but only to a single defined file which was constantly overwritten. I created a series of bash scripts and secure method of delivery on this system without trusted root certificates. The scripts bootstraped a chain of trust then setup a cron script to rotate on-device backups, deleting old backups after N days, and uploaded the latest backup to the "File Uploader" (see Misc Development & Scripting > "File Uploader").

---

### Video Management Systems

* **Video Management System (VMS)** - physically building servers & installing VMS software on Ubuntu for maybe $1,000 and 2,000 when comparable systems from the vendor were starting at $8,000 or $10,000. Hanwha Wave VMS installed on Ubuntu and I utilized MDADM to setup software RAID arrays.
* **VMS monitors** - for Hanwha and Uniview allowed us to identify and take action to correct problems with the video systems.

---

### Miscellaneous Python stuff
Various other mentions.

* **Truetrunk** - Call Accounting SMDR record analysis to calculate precise peak call volumes for a period of time. We used this to cut back on over provisioning, saving the customer money. We could determine exactly how many phone lines were needed, or project the number of calls or duration of time callers would have been unable to connect if they had fewer lines than required. If we
* **Various Integrations & API's** - Paychex, Paylocity, StarShip, QuickBooks, Peachtree, Twilio, Avalara
