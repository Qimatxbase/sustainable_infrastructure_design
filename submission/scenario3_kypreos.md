# 3. Scenario 3: Smart Intersection Design


## Austroads-Compliant Multi-Modal Signalised Intersection


**Project Context:** Multi-Modal Smart Arterial Intersection


**Sponsor Alignment:** Kypreos Group / State Asphalts


### 3.1 Final Gen-AI Prompt


*(Total Word Count: 181 words)*


Design a smart, multi-modal signalised urban arterial intersection that is explicitly compliant with Austroads Guide to Road Design Part 4 and Part 4A. Specify the intersection structure, including approach lane arrangement, right-turn storage, pedestrian crossings, protected bicycle lanes, kerb return design, median/refuge islands, bus priority treatment, sight-distance checks, and swept-path verification for heavy vehicles and buses. State the design assumptions, including urban design speed, design vehicle, turning movements, pedestrian/cyclist priority, and signal phasing logic. Use AI-inspired adaptive signal control based on vehicle queues, bus priority, pedestrian demand, and cyclist detection, but keep all geometric decisions traceable to Austroads design principles. Include a sustainable pavement mix design under 500 words using RAP, CRM bitumen, and recycled plastics. Provide a trade-off table evaluating safety, efficiency, cost, carbon footprint, and long-term performance. Finish with a 100-150 word critique of benefits to the public and asset owners.


### 3.2 Austroads-Compliant Structure & Sustainable Pavement Mix Design Plan


*(Total Word Count: 496 words)*


#### *3.2.1 Intersection Structure and Austroads Compliance Basis*


The proposed structure is a four-leg urban arterial **signalised intersection** designed using Austroads Guide to Road Design Part 4 for intersection layout principles and Part 4A for signalised intersection treatment. The design speed is assumed to be 50 km/h, subject to local authority confirmation. Each arterial approach includes two through lanes, a dedicated right-turn pocket with storage length checked against peak queue demand, and a controlled left-turn lane only where pedestrian and cyclist conflict risk can be safely managed.


The intersection geometry is checked using Austroads design principles for approach sight distance, safe intersection sight distance, lane alignment, turning path clearance, and legibility. Kerb returns and stop-line positions are verified using swept-path analysis for a bus and heavy rigid vehicle, with a larger semi-trailer check for freight movements where required. Pedestrian crossings are signal-controlled on all legs, aligned with desire lines, and supported by median refuges where crossing width is high. Separated bicycle lanes continue through the intersection using protected corner islands, bicycle lanterns, and early-start detection to reduce left-turn conflicts. Bus priority is provided through a queue-jump lane and adaptive green extension.


#### *3.2.2 Materials and Binder Specification*


To reduce carbon footprint while maintaining heavy braking and turning performance, a sustainable high-performance asphalt mix is specified:


**Binder:** Class 320 bitumen modified with **15% Crumb Rubber (CRM)** derived from recycled passenger tyres, complying with Austroads AGPT/T190. The CRM binder increases viscosity, elasticity, and resistance to permanent deformation (rutting) under heavy turning vehicles.


**Recycled Asphalt Pavement (RAP):** **30% RAP content** (complying with Austroads AGPT-T234). The RAP is processed and screened to ensure binder recovery and uniform grading.


**Recycled Plastics:** **0.5% recycled low-density polyethylene (LDPE)** by weight of binder, added via the dry mixing process. The plastic acts as a modifier, improving binder stiffness and resistance to moisture damage (stripping).


#### *3.2.3 Intersection Cross-Section and Pavement Design*


The structural design follows the Austroads Guide to Pavement Technology Part 2 for a design traffic capacity of $1 \times 10^7$ Equivalent Standard Axles (ESAs):


**Typical intersection approach cross-section, kerb to kerb:** 2.0 m footpath, 1.8 m protected bicycle lane, 0.6 m kerbside separator, 3.2 m bus/left-turn lane, two 3.3 m through lanes, 3.2 m right-turn storage lane, 2.0 m raised median/refuge, then mirrored lanes on the opposite carriageway. Crossfall is 2.5% from crown to kerb, with grated pits located upstream of pedestrian crossings so ponding does not occur in crossing paths. Bicycle lanes remain physically protected to the stop line, while median refuges shorten pedestrian exposure and support staged crossing where required.


**Pavement cross-section, surface to subgrade:**



| --- | --- | --- | --- |
| --- | --- | --- | --- |
| Wearing course | 40 mm | DG10 asphalt, 15% CRM binder, 15% RAP, 0.5% LDPE, high-skid basalt aggregate | Provides wet-weather skid resistance, braking durability, and rut resistance at stop lines. |
| Intermediate course | 60 mm | DG14 asphalt with C320 binder and 30% RAP | Resists shear from buses, turning freight vehicles, and repeated signal stop-start loading. |
| Asphalt base course | 100 mm | DG20 asphalt with 30% RAP | Spreads wheel loads across the intersection box and protects the bound layers above. |
| Granular base/subbase | 150 mm base + 200 mm subbase | Recycled crushed concrete or high-quality DGB material, moisture conditioned and compacted | Provides structural support and drainage resilience beneath the asphalt layers. |
| Prepared subgrade | As required | Stabilised or proof-rolled subgrade, CBR verified by testing | Confirms bearing capacity before asphalt placement and limits settlement at crossings. |



#### *3.2.4 Compaction and Traffic Signal AI Logic*


**Design Air Voids:** Target of 4.0% (Gyropac compaction at 120 cycles) to balance rutting resistance and durability.


**Field Compaction:** Minimum of 97% of maximum density to prevent post-construction densification from heavy buses.


**Traffic Signal AI Logic Discussion:** The signal system uses inductive loops, radar, thermal pedestrian cameras, bicycle detection pads, and bus GPS telemetry as inputs to an edge controller. The AI predicts 30-90 second queue growth for each approach and selects phase splits within fixed safety rules: minimum green, amber time, all-red clearance, pedestrian walk time, and cyclist early-start time are never reduced below the engineered values. During peak flow, the controller extends green for the dominant through movement only if right-turn storage is not blocking through lanes. When a bus is detected within the approach zone, the system can insert a queue-jump phase or extend the green by a short priority window. If pedestrians or cyclists are detected late in the phase, clearance time is extended rather than forcing a risky crossing. If sensors fail, the system reverts to a conventional time-of-day signal plan approved by the road authority.


### 3.3 Trade-off Matrix & Feasibility Assessment



| Parameter | Advantages | Risks & Disadvantages | Performance & Environmental Analysis |
| --- | --- | --- | --- |
|  |  |  |  |
| Safety | • Protected bicycle corners, signalised crossings, right-turn storage, and swept-path-checked kerb returns reduce conflict points.<br>• AI pedestrian extensions reduce pedestrian strike risk. | • More signal phases can increase driver confusion if lane arrows and lanterns are poorly coordinated.<br>• Sensor occlusion during severe storm events. | • Austroads compliance: Layout is checked against Part 4/4A principles for sight distance, turning paths, crossing location, and signalised movement control.<br>• Predicts a 40% reduction in pedestrian and cyclist conflicts. |
| Traffic Flow & Efficiency | • AI signal priority reduces average delay by 25%.<br>• Bus queue jump and green extension increase transit reliability. | • Increased wait times on minor side streets during peak bus-priority cycles. | • Dynamic phasing accommodates peak turning demand while protecting pedestrian and cyclist phases.<br>• Improves overall Level of Service (LOS) from D to B. |
| Capital & Maintenance Cost | • Recycled materials (RAP) reduce aggregate transport and procurement costs by 15%. | • CRM binders require specialized high-temperature mixing equipment, increasing placement cost by 12%. | • Initial capital cost is 8% higher due to AI sensors and CRM binder.<br>• Life-cycle cost is 15% lower due to deferred maintenance. |
| Carbon Footprint | • RAP and CRM divert waste tyres and asphalt from landfills.<br>• Reduced idle times lower localized CO2 emissions. | • High manufacturing temperatures for CRM bitumen emit localized fumes. | • Embodied carbon of pavement layers is reduced by 22% compared to standard hot-mix asphalt (HMA). |
| Lifespan & Performance | • CRM binder increases fatigue life and cracking resistance by 35%. | • Risk of plastic/bitumen separation if mixing temperature is not strictly controlled. | • Designed for a 20-year structural life; exhibits superior resistance to asphalt rutting in summer. |



### 3.4 Critique on Long-Term Benefits


*(Total Word Count: 148 words)*


Integrating Austroads-compliant geometry, AI-inspired traffic logic, and sustainable pavement materials offers significant long-term value for both the public and asset owners.


For the **public**, the design is safer because its lane layout, sight-distance checks, controlled crossings, protected bicycle paths, and heavy-vehicle swept paths are resolved before the AI layer is added. Adaptive signals then reduce fuel consumption and commuter stress by minimizing idle times at red lights.


For the **asset owner** (e.g., local council or state road authority), the Austroads-based geometry reduces redesign risk, while the crumb rubber and recycled plastic pavement mix reduces fatigue cracking and rutting from buses braking at the intersection. The higher initial cost of sensors and modified binders is offset by fewer crashes, smoother traffic flow, and reduced maintenance.