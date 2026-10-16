"""
Group 3: Chinese & Other makes in Australia (20 makes)
"""
from typing import Dict, Any

CHINESE_OTHER_MAKES: Dict[str, Dict[str, Any]] = {
    "byd": {
        "make_slug": "byd",
        "name": "BYD",
        "country_of_origin": "China",
        "years_active_au": {"start": 2022, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Build Your Dreams has rapidly evolved into Australia's second-biggest electric vehicle brand, celebrated for ultra-safe Blade Battery tech, the Atto 3, Seal sports sedan, and the groundbreaking Shark 6 plug-in hybrid ute.",
        "australian_history": "BYD entered the Australian passenger car market in 2022 through local distributor EVDirect. Debuting with the Atto 3 electric compact SUV built on e-Platform 3.0, BYD gained immediate traction with high standard equipment, class-leading Blade Battery (LFP) safety, and competitive pricing. The line-up expanded rapidly with the Dolphin urban hatchback, the aerodynamic Seal performance sedan (rivaling the Tesla Model 3), and the Sealion 6 midsize PHEV SUV. In late 2024, BYD launched the Shark 6 dual-cab ute—a purpose-built plug-in hybrid utility featuring the DMO Super Hybrid platform with 321kW and extensive Australian outback suspension tuning, igniting huge consumer interest.",
        "models_catalog": [
            {
                "model_slug": "shark-6-atto-3",
                "name": "Shark 6 / Atto 3 / Seal",
                "vehicle_type": "Ute / SUV / Sedan",
                "segment": "Electric & PHEV Pioneers",
                "years_sold_au": {"start": 2022, "end": "Present"},
                "locally_built": False,
                "overview": "BYD's trailblazing Australian pillars: the compact Atto 3 electric SUV, dynamic Seal electric sedan, and the muscular 321kW Shark 6 PHEV dual-cab ute.",
                "generations": [
                    {"series_code": "Atto-3", "generation_name": "Atto 3 Electric SUV", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Standard Range (49.9kWh) and Extended Range (60.5kWh Blade Battery), 150kW front motor, rotating touchscreen."},
                    {"series_code": "Seal", "generation_name": "Seal Electric Sports Sedan", "years": {"start": 2023, "end": "Present"}, "body_styles": ["4-door sedan"], "summary": "Dynamic RWD (150kW), Premium RWD (230kW), and Performance AWD (390kW / 670Nm, 0-100 in 3.8s, CTB cell-to-body tech)."},
                    {"series_code": "Shark-6", "generation_name": "Shark 6 DMO Super Hybrid Ute", "years": {"start": 2024, "end": "Present"}, "body_styles": ["Dual-cab ute"], "summary": "DMO ladder-frame platform; 1.5L turbo petrol + dual electric motors producing 321kW/650Nm, 29.58kWh Blade battery, 100km EV range, 2,500kg towing."}
                ]
            },
            {
                "model_slug": "dolphin",
                "name": "Dolphin",
                "vehicle_type": "Hatchback",
                "segment": "Electric Small Car",
                "years_sold_au": {"start": 2023, "end": "Present"},
                "locally_built": False,
                "overview": "One of Australia's most affordable new electric cars, delivering high five-star ANCAP safety and ocean-inspired styling.",
                "generations": [
                    {"series_code": "Dolphin-Gen1", "generation_name": "Dolphin", "years": {"start": 2023, "end": "Present"}, "body_styles": ["5-door hatchback"], "summary": "Dynamic (44.9kWh, 70kW motor) and Premium (60.5kWh, 150kW motor, multi-link rear suspension)."}
                ]
            }
        ]
    },
    "mg": {
        "make_slug": "mg",
        "name": "MG Motor",
        "country_of_origin": "China",
        "years_active_au": {"start": 1950, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "From classic British sports cars assembled at BMC Zetland Sydney (MGA and MGB) to today's SAIC-owned volume powerhouse dominating Australian light cars and the acclaimed MG4 rear-drive EV.",
        "australian_history": "Classic MG had deep manufacturing roots in Australia: Pressed Metal Corporation in Enfield and BMC at Zetland, Sydney assembled thousands of CKD MG sports cars, including the TC, TD, TF, MGA, and over 9,000 Australian-assembled MGB roadsters between 1963 and 1972. Relaunched in Australia in 2016 under Chinese parent SAIC Motor, MG Motor achieved one of the fastest market ascents in Australian history. By 2021, MG had vaulted into the top-10 vehicle brands nationally. The value-priced MG3 hatchback became Australia's undisputed best-selling light car, while the ZS compact SUV led the small SUV category. In 2023, the bespoke rear-wheel-drive MG4 electric hatchback earned unanimous critical acclaim from Australian motoring media, backed by the 320kW dual-motor MG4 XPower and the Cyberster electric roadster.",
        "models_catalog": [
            {
                "model_slug": "zs-mg4",
                "name": "ZS / ZST / MG4",
                "vehicle_type": "SUV / Hatchback",
                "segment": "Small SUV & Electric Hatchback",
                "years_sold_au": {"start": 2017, "end": "Present"},
                "locally_built": False,
                "overview": "MG's modern Australian cornerstones: the chart-topping ZS/ZST compact SUV family, pioneering ZS EV, and the multi-award-winning MG4 rear-wheel-drive electric hatchback.",
                "generations": [
                    {"series_code": "ZS-ZST", "generation_name": "ZS & ZST Petrol SUV", "years": {"start": 2017, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "ZS 1.5L naturally aspirated (84kW), and premium ZST with 1.3L Turbo (115kW), 6-speed auto, and MG Pilot safety suite."},
                    {"series_code": "ZS-EV", "generation_name": "ZS EV", "years": {"start": 2020, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Australia's pioneer sub-$45k EV; 44.5kWh Mk1 upgraded to 50.3kWh Standard Range and 72.6kWh Long Range with grille-less front face."},
                    {"series_code": "MG4", "generation_name": "MG4 EV", "years": {"start": 2023, "end": "Present"}, "body_styles": ["5-door hatchback"], "summary": "MSP modular scalable platform; 51 Excite (51kWh, 125kW), 64 Essence (64kWh, 150kW), 77 Long Range (77kWh, 530km), and 320kW dual-motor AWD XPower."}
                ]
            },
            {
                "model_slug": "mg3",
                "name": "MG3",
                "vehicle_type": "Hatchback",
                "segment": "Light Car",
                "years_sold_au": {"start": 2016, "end": "Present"},
                "locally_built": False,
                "overview": "Australia's best-selling light car for multiple consecutive years, offering unbeatable new-car showroom value, backed by the Gen-2 Hybrid+.",
                "generations": [
                    {"series_code": "MG3-Gen1", "generation_name": "MG3 First Generation", "years": {"start": 2016, "end": "2024"}, "body_styles": ["5-door hatchback"], "summary": "1.5L naturally aspirated petrol engine (82kW), 4-speed automatic, Core and Excite trims, Apple CarPlay."},
                    {"series_code": "MG3-Gen2", "generation_name": "MG3 Second Generation (Hybrid+)", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door hatchback"], "summary": "All-new chassis, 1.5L Hybrid+ producing 155kW combined output, 1.83kWh battery, and comprehensive ADAS."}
                ]
            },
            {
                "model_slug": "classic-mgb",
                "name": "Classic MGB (Australian Assembled)",
                "vehicle_type": "Roadster",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1963, "end": "1972"},
                "locally_built": True,
                "overview": "Over 9,000 MGB roadsters assembled locally at Pressed Metal Corp and BMC Zetland Sydney, etching MG into Australian sports car lore.",
                "generations": [
                    {"series_code": "MGB-Aussie", "generation_name": "MGB Mk I & II", "years": {"start": 1963, "end": 1972}, "body_styles": ["2-door roadster"], "summary": "1798cc B-series four-cylinder with twin SU carbs; locally pressed body panels, banjos and later tube rear axles."}
                ]
            }
        ]
    },
    "gwm-haval": {
        "make_slug": "gwm-haval",
        "name": "GWM / Haval",
        "country_of_origin": "China",
        "years_active_au": {"start": 2009, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "The pioneer of Chinese vehicles in Australia, progressing from the 2009 Great Wall V240 ute to direct factory operations with the GWM Cannon, Haval H6, and Tank 300 off-roaders.",
        "australian_history": "Great Wall Motors (GWM) made Australian automotive history in 2009 when distributor Ateco Automotive launched the V240 and SA220, making Great Wall the very first Chinese brand sold in Australia. In 2016, GWM established a direct factory subsidiary in Melbourne and introduced the Haval SUV brand. In 2020, GWM rebranded under a unified identity, launching the rugged Cannon dual-cab ute, Haval Jolion compact SUV, Haval H6 midsize SUV (including H6 Hybrid and H6 GT coupe-SUV), and the Tank off-road sub-brand (Tank 300 and Tank 500), achieving top-10 monthly sales rankings.",
        "models_catalog": [
            {
                "model_slug": "cannon-h6",
                "name": "Cannon / Haval H6 / Tank 300",
                "vehicle_type": "Ute / SUV / 4WD",
                "segment": "Utes & Medium/Large SUVs",
                "years_sold_au": {"start": 2009, "end": "Present"},
                "locally_built": False,
                "overview": "The backbone of GWM's Australian lineup: early pioneering V200/V240 utes, the best-selling Cannon dual-cab, high-tech Haval H6 hybrid, and heavy-duty Tank 300 4x4.",
                "generations": [
                    {"series_code": "V200-V240", "generation_name": "Great Wall V240 & V200", "years": {"start": 2009, "end": "2016"}, "body_styles": ["Single-cab ute", "Dual-cab ute"], "summary": "First Chinese vehicles in AU; 2.4L 4G69 Mitsubishi petrol (93kW) and 2.0L Turbo Diesel (105kW) with dual-range 4WD."},
                    {"series_code": "Cannon-Ute", "generation_name": "GWM Cannon Ute", "years": {"start": 2020, "end": "Present"}, "body_styles": ["Dual-cab ute"], "summary": "2.0L Turbo Diesel (120kW/400Nm), 8-speed ZF automatic, BorgWarner torque-on-demand 4WD, rear diff lock, and Cannon Alpha hybrid."},
                    {"series_code": "Haval-H6", "generation_name": "Haval H6 Gen 2 & 3", "years": {"start": 2016, "end": "Present"}, "body_styles": ["5-door SUV", "H6 GT coupe-SUV"], "summary": "L.E.M.O.N. modular platform, 2.0L Turbo (150kW), 179kW H6 Dedicated Hybrid Transmission (DHT), and swoopy H6 GT."},
                    {"series_code": "Tank-300", "generation_name": "GWM Tank 300", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door 4WD SUV"], "summary": "Ladder-chassis off-roader, front and rear differential locks, 2.0L Turbo Petrol (162kW) and 258kW/615Nm Tank 300 Hybrid."}
                ]
            },
            {
                "model_slug": "jolion",
                "name": "Haval Jolion",
                "vehicle_type": "SUV",
                "segment": "Small / Medium SUV",
                "years_sold_au": {"start": 2021, "end": "Present"},
                "locally_built": False,
                "overview": "GWM's popular family compact crossover, offering vast rear legroom, 1.5-litre turbo petrol, and punchy Jolion Hybrid.",
                "generations": [
                    {"series_code": "Jolion-Gen1", "generation_name": "Haval Jolion", "years": {"start": 2021, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "1.5L Turbo petrol (110kW/210Nm) with 7-speed DCT, and 139kW Jolion Hybrid with multi-mode transmission."}
                ]
            }
        ]
    },
    "ldv": {
        "make_slug": "ldv",
        "name": "LDV",
        "country_of_origin": "China",
        "years_active_au": {"start": 2013, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "SAIC-owned commercial and utility marque, imported by Ateco Automotive, famous for the T60 dual-cab ute (and Australia's first electric ute, the eT60), G10 and Deliver 9 commercial vans.",
        "australian_history": "Originally the British Leyland DAF Vehicles (LDV) van manufacturer, the brand was acquired by Chinese automotive giant SAIC Motor and launched in Australia in 2013 via independent distributor Ateco Automotive. Beginning with the V80 commercial van, LDV expanded with the G10 van/people mover and scored a major Australian breakthrough with the T60 dual-cab ute in 2017—the first Chinese-manufactured ute to achieve a five-star ANCAP safety rating. LDV introduced the D90 7-seat 4WD SUV, the Deliver 9 large van, and made Australian automotive history in 2022 by releasing the LDV eT60, Australia's very first commercially available all-electric ute.",
        "models_catalog": [
            {
                "model_slug": "t60",
                "name": "T60 / T60 MAX / eT60",
                "vehicle_type": "Ute / Pickup Truck",
                "segment": "Mid-size Ute",
                "years_sold_au": {"start": 2017, "end": "Present"},
                "locally_built": False,
                "overview": "Five-star ANCAP dual-cab ute offered in Pro, Luxe, 160kW bi-turbo diesel MAX, and the ground-breaking pure-electric eT60.",
                "generations": [
                    {"series_code": "SK8C", "generation_name": "T60 & T60 MAX", "years": {"start": 2017, "end": "Present"}, "body_styles": ["Dual-cab ute", "Mega Tub dual-cab"], "summary": "2.8L turbo diesel (110kW), upgraded to 2.0L Bi-Turbo Diesel T60 MAX (160kW/500Nm), and 88.5kWh electric eT60 (130kW RWD)."}
                ]
            },
            {
                "model_slug": "deliver-9",
                "name": "Deliver 9",
                "vehicle_type": "Commercial Van",
                "segment": "Large Van / Cab-Chassis",
                "years_sold_au": {"start": 2020, "end": "Present"},
                "locally_built": False,
                "overview": "One of Australia's top-selling large commercial vans, challenging the Toyota HiAce and Ford Transit on fleet cost-efficiency.",
                "generations": [
                    {"series_code": "Deliver-9-Series", "generation_name": "Deliver 9", "years": {"start": 2020, "end": "Present"}, "body_styles": ["Medium/Long/Extra-long van", "Cab-chassis"], "summary": "2.0L Turbo Diesel (110kW/375Nm) with 6-speed auto/manual, autonomous emergency braking, and pure-electric eDeliver 9."}
                ]
            }
        ]
    },
    "chery": {
        "make_slug": "chery",
        "name": "Chery",
        "country_of_origin": "China",
        "years_active_au": {"start": 2011, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Pioneered early low-cost imports (J1 and J11) via Ateco in 2011, before relaunching in 2023 as a direct factory brand with the stylish Omoda 5 and Tiggo SUV families.",
        "australian_history": "Chery first entered Australia in 2011 under Ateco Automotive with the J1 micro-hatch and J11 compact SUV. Hampered by strict ADR safety regulations and absence of electronic stability control on early models, imports ceased in 2015. In March 2023, Chery made a dramatic return to Australia as a fully owned factory subsidiary (Chery Motor Australia). Debuting with the striking Omoda 5 crossover (which secured a five-star ANCAP safety rating), followed by the Tiggo 7 Pro and 7-seat Tiggo 8 Pro Max, Chery established a national network of over 60 dealerships and launched the Omoda E5 electric SUV.",
        "models_catalog": [
            {
                "model_slug": "omoda-5",
                "name": "Omoda 5 / Omoda E5",
                "vehicle_type": "SUV",
                "segment": "Small SUV",
                "years_sold_au": {"start": 2023, "end": "Present"},
                "locally_built": False,
                "overview": "Chery's comeback hero in Australia, featuring diamond-pattern grille, dual 10.25-inch screens, five-star ANCAP safety, and all-electric E5.",
                "generations": [
                    {"series_code": "T19C", "generation_name": "Omoda 5", "years": {"start": 2023, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "1.5L Turbo (108kW/210Nm) with CVT, 1.6L Turbo GT (137kW/275Nm) with 7-speed DCT, and Omoda E5 (61kWh LFP, 150kW)."}
                ]
            },
            {
                "model_slug": "tiggo-7-8",
                "name": "Tiggo 7 Pro & Tiggo 8 Pro Max",
                "vehicle_type": "SUV",
                "segment": "Medium & Large 7-seat SUV",
                "years_sold_au": {"start": 2023, "end": "Present"},
                "locally_built": False,
                "overview": "Value-packed family SUVs offering panoramic sunroofs, Sony audio, and 2.0-litre turbo all-wheel drive.",
                "generations": [
                    {"series_code": "Tiggo-Family", "generation_name": "Tiggo 7 & 8 Pro", "years": {"start": 2023, "end": "Present"}, "body_styles": ["5-door SUV", "7-door SUV"], "summary": "Tiggo 7 Pro (1.6T 137kW) and Tiggo 8 Pro Max (2.0T 180kW/375Nm with AWD and 7 seats)."}
                ]
            }
        ]
    },
    "geely": {
        "make_slug": "geely",
        "name": "Geely",
        "country_of_origin": "China",
        "years_active_au": {"start": 2011, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Global automotive giant (owner of Volvo, Polestar, Zeekr, and Lotus) that tested Australian waters in 2011 and officially launched direct factory subsidiary operations in 2024-2025 with the EX5 electric SUV.",
        "australian_history": "Geely first tested the Australian market in 2011 through legendary Western Australian dealer John Hughes, selling a small batch of Geely MK sedans in WA. However, national distribution was postponed until 2024, when Geely Auto formally established Geely Auto Australia as a direct factory operation. Leveraging its global platforms and R&D synergies with Volvo and Zeekr, Geely debuted with the EX5 mid-size electric SUV featuring its Short Blade Battery technology and Flyme Auto infotainment.",
        "models_catalog": [
            {
                "model_slug": "ex5",
                "name": "EX5",
                "vehicle_type": "SUV",
                "segment": "Medium Electric SUV",
                "years_sold_au": {"start": 2024, "end": "Present"},
                "locally_built": False,
                "overview": "Geely's global electric SUV launched in Australia, built on the GEA platform with 160kW front motor and 60.2kWh Aegis Short Blade battery.",
                "generations": [
                    {"series_code": "EX5-Gen1", "generation_name": "Geely EX5", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "GEA architecture, 11-in-1 intelligent electric drive, 15.4-inch 2.5K screen, and 430km WLTP range."}
                ]
            }
        ]
    },
    "zeekr": {
        "make_slug": "zeekr",
        "name": "Zeekr",
        "country_of_origin": "China",
        "years_active_au": {"start": 2024, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Geely Holding's premium luxury electric brand, launching in Australia in late 2024 with the Zeekr X compact luxury crossover and Zeekr 009 ultra-luxury electric MPV.",
        "australian_history": "Zeekr officially entered the Australian market in the fourth quarter of 2024 as a dedicated factory-backed premium EV marque. Built on Geely's Sustainable Experience Architecture (SEA), Zeekr vehicles blend Scandinavian design influence with cutting-edge 800V fast-charging silicon-carbide technology. Zeekr Australia launched with the Zeekr X urban crossover (in 200kW RWD and 315kW AWD guise) and the statement-making Zeekr 009—a multi-seat executive electric MPV with reclining captain's chairs and 116kWh battery.",
        "models_catalog": [
            {
                "model_slug": "zeekr-x",
                "name": "Zeekr X",
                "vehicle_type": "Crossover SUV",
                "segment": "Compact Luxury Electric SUV",
                "years_sold_au": {"start": 2024, "end": "Present"},
                "locally_built": False,
                "overview": "Frameless doors, hidden charge port, and 315kW dual-motor acceleration from 0-100 km/h in 3.8 seconds.",
                "generations": [
                    {"series_code": "Zeekr-X", "generation_name": "Zeekr X", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door crossover"], "summary": "66kWh ternary NMC battery, RWD (200kW) and AWD (315kW), Yamaha surround sound, and sliding central display."}
                ]
            },
            {
                "model_slug": "zeekr-009",
                "name": "Zeekr 009",
                "vehicle_type": "People Mover / MPV",
                "segment": "Ultra-Luxury Electric MPV",
                "years_sold_au": {"start": 2024, "end": "Present"},
                "locally_built": False,
                "overview": "Flagship 6-seat and 7-seat ultra-luxury electric transporter with dual-chamber air suspension and 450kW dual motors.",
                "generations": [
                    {"series_code": "Zeekr-009", "generation_name": "Zeekr 009", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door MPV"], "summary": "116kWh/140kWh CATL Qilin battery, 450kW AWD, Sofaro first-class airline seats with massage and entertainment screen."}
                ]
            }
        ]
    },
    "xpeng": {
        "make_slug": "xpeng",
        "name": "XPENG",
        "country_of_origin": "China",
        "years_active_au": {"start": 2024, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "High-tech smart EV manufacturer entering Australia in late 2024 with the 800V silicon carbide G6 coupe-SUV, distributed by TrueEV.",
        "australian_history": "XPENG Motors entered the Australian automotive market in late 2024 through independent distributor TrueEV. Renowned for its advanced autonomous driving algorithms (SEPA 2.0 platform) and ultra-fast 800V Silicon Carbide (SiC) charging architecture, XPENG launched with the G6 coupe-SUV directly targeting the Tesla Model Y. Capable of charging from 10% to 80% in just 20 minutes, the G6 arrived with five-star Euro NCAP safety and comprehensive active driver assistance.",
        "models_catalog": [
            {
                "model_slug": "g6",
                "name": "G6",
                "vehicle_type": "Coupe SUV",
                "segment": "Medium Electric SUV",
                "years_sold_au": {"start": 2024, "end": "Present"},
                "locally_built": False,
                "overview": "800V fast-charging coupe crossover featuring front and rear integrated aluminium die-casting and Xmart OS.",
                "generations": [
                    {"series_code": "G6-Gen1", "generation_name": "XPENG G6", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door coupe-SUV"], "summary": "Standard Range (66kWh LFP, 190kW) and Long Range (87.5kWh NCM, 210kW, 570km WLTP range) with 280kW DC ultra-rapid charging."}
                ]
            }
        ]
    },
    "leapmotor": {
        "make_slug": "leapmotor",
        "name": "Leapmotor",
        "country_of_origin": "China",
        "years_active_au": {"start": 2024, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Innovative EV brand backed by multinational giant Stellantis (Leapmotor International), launching in Australia in late 2024 with the C10 medium SUV and T03 city car.",
        "australian_history": "Leapmotor made its Australian debut in November 2024 under Leapmotor International—a 51:49 joint venture led by Stellantis (the parent company of Jeep, RAM, Fiat, and Alfa Romeo). Utilizing Stellantis' established Australian distribution infrastructure, Leapmotor entered with the C10 midsize electric SUV built on the LEAP 3.0 technology architecture. Featuring cell-to-chassis (CTC 2.0) engineering, a Qualcomm Snapdragon 8155 cockpit, and competitive pricing, Leapmotor targets mainstream family EV buyers.",
        "models_catalog": [
            {
                "model_slug": "c10",
                "name": "C10",
                "vehicle_type": "SUV",
                "segment": "Medium Electric SUV",
                "years_sold_au": {"start": 2024, "end": "Present"},
                "locally_built": False,
                "overview": "Family electric SUV offering 160kW rear-wheel drive, 69.9kWh LFP battery, and five-star Euro NCAP crash safety.",
                "generations": [
                    {"series_code": "C10-Gen1", "generation_name": "Leapmotor C10", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Style and Design trims, 160kW/320Nm rear motor, 420km WLTP range, organic silicone upholstery, and panoramic glass roof."}
                ]
            }
        ]
    },
    "deepal": {
        "make_slug": "deepal",
        "name": "Deepal",
        "country_of_origin": "China",
        "years_active_au": {"start": 2024, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Changan Automobile's dedicated new energy brand, launched in Australia in late 2024 by leading distributor Inchcape with the head-turning Deepal S07 SUV.",
        "australian_history": "Deepal arrived in Australia in late 2024 distributed by Inchcape Australasia (the long-standing Australian distributor for Subaru and Peugeot). Developed by Changan Automobile, Deepal vehicles feature striking angular European styling penned at Changan's Turin design centre in Italy. The debut model, the Deepal S07 midsize electric SUV, features rear-wheel drive, a 66.8kWh battery, frameless doors, augmented reality head-up display, and a 15.6-inch sunflower rotating touchscreen.",
        "models_catalog": [
            {
                "model_slug": "s07",
                "name": "S07",
                "vehicle_type": "SUV",
                "segment": "Medium Electric SUV",
                "years_sold_au": {"start": 2024, "end": "Present"},
                "locally_built": False,
                "overview": "Turin-designed electric midsize SUV featuring rear-wheel drive dynamics, 160kW motor, and high-tech cabin.",
                "generations": [
                    {"series_code": "S07-Gen1", "generation_name": "Deepal S07", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "EPA1 multi-energy platform, 66.8kWh ternary NMC battery, 475km WLTP range, and interactive front lighting."}
                ]
            }
        ]
    },
    "jac": {
        "make_slug": "jac",
        "name": "JAC Motors",
        "country_of_origin": "China",
        "years_active_au": {"start": 2024, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Chinese commercial giant entering Australia's fiercely contested dual-cab ute segment in 2024 with the JAC T9 turbo diesel and electric utilities.",
        "australian_history": "JAC Motors officially entered the Australian light commercial market in early 2024 through independent distributor LTS Auto. JAC launched with the T9 dual-cab ute—a rugged ladder-frame pickup powered by a 2.0-litre turbo diesel engine paired with an 8-speed ZF automatic gearbox and BorgWarner part-time 4WD. The T9 earned a full five-star ANCAP safety rating under the stringent 2023-2025 testing criteria. JAC also previewed an all-electric dual-cab T9 EV with an 88kWh battery.",
        "models_catalog": [
            {
                "model_slug": "t9",
                "name": "T9",
                "vehicle_type": "Ute / Pickup Truck",
                "segment": "Mid-size Dual-Cab Ute",
                "years_sold_au": {"start": 2024, "end": "Present"},
                "locally_built": False,
                "overview": "Boldly styled dual-cab ute with 3,500kg braked towing, five-star ANCAP safety, and 2.0L turbo diesel power.",
                "generations": [
                    {"series_code": "T9-Gen1", "generation_name": "JAC T9", "years": {"start": 2024, "end": "Present"}, "body_styles": ["Dual-cab ute"], "summary": "Oasis and Haven trims; 2.0L Turbo Diesel (125kW/410Nm), 8-speed ZF auto, rear diff lock, and 10.4-inch touchscreen."}
                ]
            }
        ]
    },
    "foton": {
        "make_slug": "foton",
        "name": "Foton",
        "country_of_origin": "China",
        "years_active_au": {"start": 2012, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Commercial vehicle specialist that pioneered Cummins-powered utes (Tunland) and Aumark light trucks in Australia, evolving into the Tunland V9 hybrid.",
        "australian_history": "Foton entered Australia in 2012 through FAA Automotive with the Tunland dual-cab ute, uniquely powered by an authentic American Cummins ISF 2.8-litre turbo diesel engine paired with a Getrag manual gearbox, BorgWarner transfer case, and Dana rear axle. Foton followed with the Sauvana 7-seat 4WD SUV and established a solid position in commercial trucks (Aumark and T5 EV light trucks). In 2024, Foton returned to the consumer passenger market with the large Tunland V9 hybrid ute.",
        "models_catalog": [
            {
                "model_slug": "tunland",
                "name": "Tunland",
                "vehicle_type": "Ute / Pickup Truck",
                "segment": "Mid-size Ute",
                "years_sold_au": {"start": 2012, "end": "Present"},
                "locally_built": False,
                "overview": "Rugged commercial ute featuring Cummins turbo diesel engineering and evolving into the full-size V9 mild-hybrid.",
                "generations": [
                    {"series_code": "Tunland-Classic", "generation_name": "Tunland Cummins 2.8", "years": {"start": 2012, "end": "2019"}, "body_styles": ["Single-cab ute", "Dual-cab ute"], "summary": "Cummins ISF 2.8L turbo diesel (120kW/360Nm), Getrag 5-speed manual, Dana 44 limited slip differential."},
                    {"series_code": "Tunland-V9", "generation_name": "Tunland V7 & V9 Hybrid", "years": {"start": 2024, "end": "Present"}, "body_styles": ["Dual-cab ute"], "summary": "2.0L Turbo Diesel with 48V mild-hybrid system, 8-speed ZF automatic, and multi-link rear coil suspension."}
                ]
            }
        ]
    },
    "jmc": {
        "make_slug": "jmc",
        "name": "JMC",
        "country_of_origin": "China",
        "years_active_au": {"start": 2015, "end": "2018"},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Jiangling Motors Corporation imported the Vigus dual-cab ute into Australia from 2015 to 2018 via JMC Auto Australia.",
        "australian_history": "JMC (Jiangling Motors Corporation, Ford's long-standing joint-venture partner in China) entered the Australian market in early 2015 through independent distributor JMC Auto Australia. Offering the Vigus dual-cab utility in two-wheel drive and four-wheel drive, JMC targeted budget-conscious tradies and farmers. The Vigus offered a 2.4-litre turbo diesel engine and a 2.0-litre turbo petrol engine with rear diff locks. Facing stiff competition from established Japanese brands and fellow Chinese manufacturers GWM and LDV, JMC ceased retail imports to Australia in 2018.",
        "models_catalog": [
            {
                "model_slug": "vigus",
                "name": "Vigus",
                "vehicle_type": "Ute / Pickup Truck",
                "segment": "Mid-size Dual-Cab Ute",
                "years_sold_au": {"start": 2015, "end": "2018"},
                "locally_built": False,
                "overview": "Budget dual-cab ute offered in 4x2 and 4x4, powered by Ford-derived 2.4L turbo diesel or 2.0L turbo petrol.",
                "generations": [
                    {"series_code": "Vigus-Gen1", "generation_name": "JMC Vigus", "years": {"start": 2015, "end": "2018"}, "body_styles": ["Dual-cab ute"], "summary": "2.4L TDCi diesel (90kW/290Nm) and 2.0L Turbo petrol (151kW/325Nm) with 5-speed manual transmission."}
                ]
            }
        ]
    },
    "zx-auto": {
        "make_slug": "zx-auto",
        "name": "ZX Auto",
        "country_of_origin": "China",
        "years_active_au": {"start": 2013, "end": "2016"},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Hebei Zhongxing Automobile sold the GrandTiger dual-cab ute in Australia from 2013 to 2016 via Chinese Automotive Distributors.",
        "australian_history": "ZX Auto entered the Australian market in mid-2013 through Perth-based Chinese Automotive Distributors (CAD). The company imported the GrandTiger dual-cab utility, pitching it as an ultra-low-cost commercial vehicle for rural and regional buyers. The GrandTiger was powered by a 2.4-litre Mitsubishi petrol engine and a 2.5-litre turbo diesel with a five-speed manual transmission. Low sales and stricter ADR safety regulations led to its withdrawal from Australia in 2016.",
        "models_catalog": [
            {
                "model_slug": "grandtiger",
                "name": "GrandTiger",
                "vehicle_type": "Ute / Pickup Truck",
                "segment": "Mid-size Dual-Cab Ute",
                "years_sold_au": {"start": 2013, "end": "2016"},
                "locally_built": False,
                "overview": "Ultra-budget dual-cab work ute sold through regional dealerships in Western Australia, Queensland, and NSW.",
                "generations": [
                    {"series_code": "GrandTiger-Gen1", "generation_name": "ZX Auto GrandTiger", "years": {"start": 2013, "end": "2016"}, "body_styles": ["Dual-cab ute"], "summary": "2.4L Mitsubishi 4G64 petrol (100kW) and 2.5L Turbo Diesel with dual-range 4WD."}
                ]
            }
        ]
    },
    "proton": {
        "make_slug": "proton",
        "name": "Proton",
        "country_of_origin": "Malaysia",
        "years_active_au": {"start": 1995, "end": "2017"},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Malaysian national carmaker that achieved cult Australian status with the Jumbuck compact coupe utility and Lotus-tuned Satria GTi hot hatch.",
        "australian_history": "Proton launched in Australia in 1995 under distributor Proton Cars Australia, initially offering the Wira sedan and hatchback based on the Mitsubishi Lancer. In 1999, Proton made waves with the Satria GTi—a three-door hot hatch tuned by Lotus (which Proton had acquired), featuring stiffened suspension, Recaro seats, and flared bodywork. In 2003, Proton struck an Australian chord with the Proton Jumbuck: an affordable, front-wheel-drive, car-based coupe utility that became a beloved cult work vehicle for Australian couriers and tradespeople. Later models included the CamPro-powered Gen-2, Persona, Preve sedan, and Suprima S turbo hatch before Proton exited Australia in 2017.",
        "models_catalog": [
            {
                "model_slug": "jumbuck",
                "name": "Jumbuck",
                "vehicle_type": "Coupe Utility",
                "segment": "Compact Ute",
                "years_sold_au": {"start": 2003, "end": "2010"},
                "locally_built": False,
                "overview": "A beloved cult favourite in Australia; an affordable, car-based front-wheel-drive 1.5-litre utility with leaf-spring rear payload.",
                "generations": [
                    {"series_code": "Jumbuck-Gen1", "generation_name": "Proton Jumbuck", "years": {"start": 2003, "end": "2010"}, "body_styles": ["Coupe utility (2-door)"], "summary": "1.5L Mitsubishi 4G15 12-valve engine (64kW), 5-speed manual, half-tonne payload, GLi and GLS trims."}
                ]
            },
            {
                "model_slug": "satria-gti",
                "name": "Satria GTi",
                "vehicle_type": "Hatchback",
                "segment": "Hot Hatchback",
                "years_sold_au": {"start": 1999, "end": "2005"},
                "locally_built": False,
                "overview": "Lotus-tuned hot hatch featuring flared rivet arches, 16-inch wheels, Recaro interior, and rev-happy 1.8-litre twin-cam engine.",
                "generations": [
                    {"series_code": "C99", "generation_name": "Satria GTi", "years": {"start": 1999, "end": "2005"}, "body_styles": ["3-door hatchback"], "summary": "1.8L Mitsubishi 4G93 DOHC engine (103kW), Handling by Lotus tuned dampers and anti-roll bars."}
                ]
            }
        ]
    },
    "mahindra": {
        "make_slug": "mahindra",
        "name": "Mahindra",
        "country_of_origin": "India",
        "years_active_au": {"start": 2007, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Indian 4x4 powerhouse renowned in regional Australia for the indestructible Pik-Up commercial ute, rugged Scorpio 4WD, and 7-seat XUV700 family SUV.",
        "australian_history": "Mahindra Automotive entered Australia in 2007 with the rugged Pik-Up commercial utility, establishing direct factory operations with Mahindra Automotive Australia in Brisbane. The Pik-Up, featuring an Eaton automatic locking rear differential and tough ladder chassis, became a staple of Australian farming, agriculture, and mining communities. Mahindra steadily modernized its passenger range with the monocoque XUV500, the luxurious 7-seat XUV700, and the Scorpio ladder-frame off-road 4WD, building a loyal rural dealer network.",
        "models_catalog": [
            {
                "model_slug": "pik-up",
                "name": "Pik-Up",
                "vehicle_type": "Ute / Cab-Chassis",
                "segment": "Mid-size Commercial Ute",
                "years_sold_au": {"start": 2007, "end": "Present"},
                "locally_built": False,
                "overview": "Uncompromising workhorse loved across rural Australia, featuring 2.2L mHawk turbo diesel and standard Eaton MLocker rear differential.",
                "generations": [
                    {"series_code": "Pik-Up-Classic-Modern", "generation_name": "Mahindra Pik-Up", "years": {"start": 2007, "end": "Present"}, "body_styles": ["Single-cab cab-chassis", "Dual-cab ute"], "summary": "2.2L mHawk CRDe Turbo Diesel (103kW/320Nm), 6-speed manual/automatic, 4x4 with low range and steel tray options."}
                ]
            },
            {
                "model_slug": "scorpio-xuv700",
                "name": "Scorpio / XUV700",
                "vehicle_type": "SUV",
                "segment": "Medium / Large 4WD SUV",
                "years_sold_au": {"start": 2022, "end": "Present"},
                "locally_built": False,
                "overview": "Mahindra's modern generation: the body-on-frame Scorpio 4x4 and sophisticated 7-seat XUV700 family SUV.",
                "generations": [
                    {"series_code": "Scorpio-N", "generation_name": "Scorpio", "years": {"start": 2023, "end": "Present"}, "body_styles": ["5-door 4WD SUV"], "summary": "2.2L mHawk diesel (129kW/400Nm), 4XPLOR terrain response, 6-speed auto, and 6-seat captain's chairs."},
                    {"series_code": "XUV700", "generation_name": "XUV700", "years": {"start": 2023, "end": "Present"}, "body_styles": ["5-door 7-seat SUV"], "summary": "2.0L mStallion Turbo Petrol (149kW/380Nm), dual 10.25-inch screens, Level 2 ADAS, and Sony 12-speaker sound."}
                ]
            }
        ]
    },
    "tata": {
        "make_slug": "tata",
        "name": "Tata Motors",
        "country_of_origin": "India",
        "years_active_au": {"start": 1996, "end": "2017"},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Indian industrial giant that sold the Telcoline ute in the late 1990s and relaunched the Xenon commercial utility in Australia from 2013 to 2017.",
        "australian_history": "Tata Motors first entered Australia in 1996 through Premier Automotive, importing the Telcoline single-cab and dual-cab commercial utility with a 2.0-litre turbo diesel engine. In October 2013, Tata relaunched in Australia via distributor Fusion Automotive (part of the Walkinshaw Automotive Group). Fusion established a network of 40 dealers selling the Tata Xenon dual-cab, single-cab, and cab-chassis utility, powered by a 2.2-litre Euro 5 Dicor turbo diesel. Despite strong fleet and farm marketing, low crash-safety scores in an era demanding five-star ratings led Tata to exit the Australian light vehicle market in 2017.",
        "models_catalog": [
            {
                "model_slug": "xenon",
                "name": "Xenon / Telcoline",
                "vehicle_type": "Ute / Cab-Chassis",
                "segment": "Mid-size Commercial Ute",
                "years_sold_au": {"start": 1996, "end": "2017"},
                "locally_built": False,
                "overview": "Heavy-duty commercial utility imported by Walkinshaw's Fusion Automotive, featuring 2.2-litre turbo diesel torque.",
                "generations": [
                    {"series_code": "Telcoline", "generation_name": "Tata Telcoline", "years": {"start": 1996, "end": "2002"}, "body_styles": ["Single-cab", "Dual-cab"], "summary": "2.0L Peugeot-derived turbo diesel engine (66kW) with 5-speed manual and rear-wheel drive / 4WD."},
                    {"series_code": "Xenon", "generation_name": "Tata Xenon", "years": {"start": 2013, "end": "2017"}, "body_styles": ["Cab-chassis", "Single-cab", "Dual-cab"], "summary": "2.2L Dicor Turbo Diesel (110kW/320Nm), 5-speed manual, BorgWarner 4WD, 2,500kg braked towing."}
                ]
            }
        ]
    },
    "lada": {
        "make_slug": "lada",
        "name": "Lada",
        "country_of_origin": "Russia",
        "years_active_au": {"start": 1983, "end": "1996"},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Soviet/Russian automotive manufacturer that captured an Australian cult following with the unbreakable, permanent four-wheel drive Lada Niva.",
        "australian_history": "Lada was introduced to Australia in 1983 by Lada Cars of Australia, headquartered in Queensland. The star of the range was the Lada Niva (VAZ-2121)—a lightweight, monocoque off-roader with permanent four-wheel drive, center differential lock, and coil-spring suspension that could out-climb vehicles three times its price in the Australian bush. Lada also introduced Australian-specific variants like the Niva Bushman cab-chassis and soft-top. Passenger models like the front-wheel-drive Lada Samara, Cevaro sedan, and Sable arrived in the late 1980s. Following the collapse of the Soviet Union, distributor financial troubles, and tightening Australian Design Rules for crash safety and emissions, Lada ceased Australian imports in 1996.",
        "models_catalog": [
            {
                "model_slug": "niva",
                "name": "Niva",
                "vehicle_type": "Off-Road 4WD",
                "segment": "Compact 4WD",
                "years_sold_au": {"start": 1983, "end": "1996"},
                "locally_built": False,
                "overview": "Legendary Russian mountain goat; monocoque permanent 4WD with locking centre differential, beloved by Australian bush adventurers.",
                "generations": [
                    {"series_code": "VAZ-2121", "generation_name": "Lada Niva", "years": {"start": 1983, "end": "1996"}, "body_styles": ["3-door wagon", "Cab-chassis Bushman", "Soft top"], "summary": "1.6L carburettor (56kW) and later 1.7L single-point EFI, dual-range transfer case, and Aussie-built Bushman ute conversions."}
                ]
            },
            {
                "model_slug": "samara-cevaro",
                "name": "Samara / Cevaro / Sable",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Small Car",
                "years_sold_au": {"start": 1988, "end": "1996"},
                "locally_built": False,
                "overview": "Porsche-engineered cylinder head front-wheel-drive budget hatchback and sedan.",
                "generations": [
                    {"series_code": "VAZ-2108-2109", "generation_name": "Lada Samara & Cevaro", "years": {"start": 1988, "end": "1996"}, "body_styles": ["3-door hatch", "5-door hatch", "4-door sedan"], "summary": "1.3L and 1.5L OHC four-cylinder engines with 5-speed manual, Cevaro sedan, and Sable luxury trim."}
                ]
            }
        ]
    },
    "fso": {
        "make_slug": "fso",
        "name": "FSO",
        "country_of_origin": "Poland",
        "years_active_au": {"start": 1988, "end": "1992"},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Polish manufacturer that imported the rugged, budget-priced FSO Polonez hatchback and commercial utility into Australia.",
        "australian_history": "Fabryka Samochodów Osobowych (FSO) of Warsaw, Poland exported vehicles to Australia between 1988 and 1992 through independent importer FSO Motors Australia. Based on Fiat 125 mechanics wrapped in a chunky hatchback body designed by Giorgetto Giugiaro and Walter de Silva, the Polonez offered solid steel gauge construction and simple pushrod mechanics. In addition to the five-door hatchback, the FSO Polonez Truck (a half-tonne pickup utility with separate chassis and leaf springs) found modest use with rural operators looking for the cheapest new ute in Australia. Tightening emissions and crash rules concluded imports in 1992.",
        "models_catalog": [
            {
                "model_slug": "polonez",
                "name": "Polonez & Polonez Truck",
                "vehicle_type": "Hatchback / Ute",
                "segment": "Small / Medium Car & Ute",
                "years_sold_au": {"start": 1988, "end": "1992"},
                "locally_built": False,
                "overview": "Polish utilitarian family hatchback and pickup utility, celebrated for rugged thick steel construction and bargain pricing.",
                "generations": [
                    {"series_code": "Polonez-MR87", "generation_name": "FSO Polonez & Truck", "years": {"start": 1988, "end": "1992"}, "body_styles": ["5-door hatchback", "Single-cab ute"], "summary": "1.5L and 1.6L OHV four-cylinder engines (55kW-64kW), 5-speed manual, live rear axle, and heavy-duty Truck utility."}
                ]
            }
        ]
    },
    "yugo": {
        "make_slug": "yugo",
        "name": "Yugo",
        "country_of_origin": "Yugoslavia",
        "years_active_au": {"start": 1988, "end": "1992"},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Zastava's Yugoslav city car that claimed the title of Australia's cheapest brand-new car in the late 1980s and early 1990s.",
        "australian_history": "Yugo entered the Australian market in late 1988 under Yugo Cars Australia, importing vehicles built by Zastava Automobiles in Kragujevac, Yugoslavia. Derived from the Fiat 127/128, the Yugo was sold in Australia as the Yugo 45 (903cc) and Yugo 55 (1.1-litre) three-door hatchback. Advertised under the slogan 'A whole lot of car for a little bit of money' and priced at just $8,990 drive-away, it was the cheapest new car available in Australia. Approximately 1,200 cars were sold before the Yugoslav civil war, hyperinflation, and United Nations trade sanctions abruptly brought production and exports to a halt in 1992.",
        "models_catalog": [
            {
                "model_slug": "yugo-45-55",
                "name": "Yugo 45 / 55",
                "vehicle_type": "Hatchback",
                "segment": "Micro / City Car",
                "years_sold_au": {"start": 1988, "end": "1992"},
                "locally_built": False,
                "overview": "Australia's bargain-basement three-door runabout of the late 1980s, offering simple Fiat-derived mechanicals and sub-$9k pricing.",
                "generations": [
                    {"series_code": "Yugo-Koral", "generation_name": "Yugo 45 & 55", "years": {"start": 1988, "end": "1992"}, "body_styles": ["3-door hatchback"], "summary": "903cc 4-cylinder OHV (33kW) on Yugo 45; 1116cc SOHC (40kW) with 5-speed manual on Yugo 55."}
                ]
            }
        ]
    }
}
