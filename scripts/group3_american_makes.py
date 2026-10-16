"""
Group 3: American makes in Australia (10 makes)
"""
from typing import Dict, Any

AMERICAN_MAKES: Dict[str, Dict[str, Any]] = {
    "tesla": {
        "make_slug": "tesla",
        "name": "Tesla",
        "country_of_origin": "United States",
        "years_active_au": {"start": 2014, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "The pioneer and market leader of electric vehicles in Australia, transforming the automotive landscape with the top-selling Model 3 and Model Y and an extensive nationwide Supercharger network.",
        "australian_history": "Tesla officially entered the Australian market in December 2014, delivering its first Model S sedans at a gala event in Sydney. Model X followed in 2016. However, the true Australian EV tipping point occurred in August 2019 with the launch of the Model 3. Built in Shanghai for the Australian market, the Model 3 delivered sharp pricing, class-leading range, and high-performance dual-motor capability. In June 2022, Tesla launched the Model Y SUV in Australia, which immediately surged to become Australia's best-selling electric vehicle and frequently ranked among the top three best-selling vehicles outright in national monthly sales charts. Tesla's proprietary Supercharger network spans coast to coast across Australia, from Cairns to Perth and across regional highways, driving mass-market EV adoption.",
        "models_catalog": [
            {
                "model_slug": "model-3",
                "name": "Model 3",
                "vehicle_type": "Sedan",
                "segment": "Medium Electric Car",
                "years_sold_au": {"start": 2019, "end": "Present"},
                "locally_built": False,
                "overview": "Australia's landmark electric sports sedan, progressing from original Standard Range Plus to the refined Highland update and 460hp Performance.",
                "generations": [
                    {"series_code": "Model-3-Original", "generation_name": "Model 3 (Pre-Highland)", "years": {"start": 2019, "end": 2023}, "body_styles": ["4-door sedan"], "summary": "RWD (LFP battery), Long Range AWD (82kWh ternary NMC), and Performance (357kW, 0-100 in 3.3s, Track Mode)."},
                    {"series_code": "Model-3-Highland", "generation_name": "Model 3 (Highland Facelift)", "years": {"start": 2023, "end": "Present"}, "body_styles": ["4-door sedan"], "summary": "Sleeker front/rear lighting, rear 8-inch screen, acoustic glass, ventilated seats, and 343kW Highland Performance."}
                ]
            },
            {
                "model_slug": "model-y",
                "name": "Model Y",
                "vehicle_type": "SUV",
                "segment": "Medium Electric SUV",
                "years_sold_au": {"start": 2022, "end": "Present"},
                "locally_built": False,
                "overview": "Australia's top-selling electric SUV, offering expansive panoramic glass roof, cavernous cargo room, and class-leading energy efficiency.",
                "generations": [
                    {"series_code": "Model-Y-Gen1", "generation_name": "Model Y", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Single-motor RWD (60kWh LFP, 455km WLTP), Long Range AWD (75kWh, 533km), and Performance AWD (357kW, 21-inch Uberturbines, 0-100 in 3.7s)."}
                ]
            },
            {
                "model_slug": "model-s",
                "name": "Model S",
                "vehicle_type": "Liftback Sedan",
                "segment": "Large Luxury Electric Car",
                "years_sold_au": {"start": 2014, "end": "2020"},
                "locally_built": False,
                "overview": "Tesla's flagship sedan that introduced Australia to ludicrous electric acceleration and over-the-air software updates.",
                "generations": [
                    {"series_code": "Model-S-Gen1", "generation_name": "Model S", "years": {"start": 2014, "end": "2020"}, "body_styles": ["5-door liftback"], "summary": "60, 75D, 85, 90D, 100D, and P100D with Ludicrous Mode delivering 0-100 km/h in 2.6 seconds."}
                ]
            }
        ]
    },
    "jeep": {
        "make_slug": "jeep",
        "name": "Jeep",
        "country_of_origin": "United States",
        "years_active_au": {"start": 1946, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "The original 4x4 brand, with rich Australian heritage including post-war CKD assembly of Willys and CJ Jeeps in Sydney and Brisbane, through to modern Wrangler, Cherokee, and Grand Cherokee.",
        "australian_history": "Willys-Overland Jeeps first arrived in Australia during the Second World War with Allied forces. In the post-war era, Willys Motors Australia and Pressed Metal Corporation in Enfield, Sydney assembled CKD kits of the CJ-3B, CJ-5, and Willys utility wagons. In the 1960s and 1970s, Kaiser Jeep and AMC assembled Jeep CJ-6, CJ-7, and Gladiator pickups in Rocklea, Brisbane. The modern retail resurgence began in 1994 when Chrysler Jeep Australia reintroduced the Cherokee (XJ), offering unbeatable value 4.0-litre inline-six capability. The Wrangler (TJ, JK, JL) became Australia's ultimate lifestyle off-roader, while the Grand Cherokee (WJ, WK2) achieved massive towing popularity across the nation.",
        "models_catalog": [
            {
                "model_slug": "wrangler",
                "name": "Wrangler",
                "vehicle_type": "4WD Convertible SUV",
                "segment": "Off-Road 4WD",
                "years_sold_au": {"start": 1996, "end": "Present"},
                "locally_built": False,
                "overview": "The quintessential open-air 4x4, offering removable doors, fold-down windscreen, live Dana 44 axles, and legendary Rubicon rock-crawling prowess.",
                "generations": [
                    {"series_code": "TJ", "generation_name": "Wrangler TJ", "years": {"start": 1996, "end": 2006}, "body_styles": ["2-door soft top", "2-door hard top"], "summary": "Quadra-Coil all-coil suspension, AMC 4.0L High Output inline-six, Sport, Renegade, and first Rubicon with Rock-Trac 4:1."},
                    {"series_code": "JK", "generation_name": "Wrangler JK", "years": {"start": 2007, "end": 2018}, "body_styles": ["2-door soft top", "4-door Unlimited"], "summary": "Introduced the four-door Unlimited; 3.8L V6, 3.6L Pentastar V6 (209kW), and 2.8 CRD turbo diesel."},
                    {"series_code": "JL", "generation_name": "Wrangler JL", "years": {"start": 2018, "end": "Present"}, "body_styles": ["2-door", "4-door Unlimited"], "summary": "Aluminium doors/tailgate, 8-speed automatic, 3.6L Pentastar, 2.0L Turbo, forward-facing TrailCam, and electronic sway-bar disconnect."}
                ]
            },
            {
                "model_slug": "grand-cherokee",
                "name": "Grand Cherokee",
                "vehicle_type": "SUV",
                "segment": "Large 4WD SUV",
                "years_sold_au": {"start": 1996, "end": "Present"},
                "locally_built": False,
                "overview": "Jeep's flagship luxury 4WD in Australia, renowned for 3,500kg towing capacity, Quadra-Lift air suspension, and thundering 6.4L SRT and 527kW Trackhawk models.",
                "generations": [
                    {"series_code": "ZJ-WJ", "generation_name": "Grand Cherokee ZJ & WJ", "years": {"start": 1996, "end": "2005"}, "body_styles": ["5-door 4WD"], "summary": "4.0L inline-six, 4.7L PowerTech V8, Quadra-Drive with Vari-Lok progressive axles, and Laredo/Limited trims."},
                    {"series_code": "WK2", "generation_name": "Grand Cherokee WK2", "years": {"start": 2011, "end": "2021"}, "body_styles": ["5-door SUV"], "summary": "3.0L V6 EcoDiesel, 5.7L HEMI V8, 6.4L SRT V8 (344kW), and supercharged 527kW 6.2L Hellcat Trackhawk."},
                    {"series_code": "WL", "generation_name": "Grand Cherokee WL", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door SUV", "7-seat Grand Cherokee L"], "summary": "All-new Giorgio-derived platform, 3.6L Pentastar V6, 4xe Plug-in Hybrid, and McIntosh premium audio."}
                ]
            }
        ]
    },
    "ram": {
        "make_slug": "ram",
        "name": "RAM Trucks",
        "country_of_origin": "United States",
        "years_active_au": {"start": 2015, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "The pioneer of full-size American pickup trucks in Australia, re-engineered and remanufactured to OEM right-hand drive standards by Walkinshaw Automotive in Clayton, Victoria.",
        "australian_history": "RAM Trucks Australia revolutionized the Australian light commercial market. In 2015, American Special Vehicles (a partnership between Walkinshaw Automotive Group and Ateco) established a full-scale OEM-standard right-hand drive remanufacturing facility at Walkinshaw's headquarters in Clayton, Victoria. Employing hundreds of Australian engineers and automotive tradespeople, the facility disassembles imported RAM 1500 and 2500/3500 trucks and rebuilds them with a bespoke Australian-engineered RHD steering box, RHD dashboard, heating/air-conditioning unit, and ADR-compliant wiring harnesses. Over 25,000 trucks have rolled off the Clayton line. RAM trucks dominate Australia's heavy caravan, boat, and horse-float towing community thanks to their 4.5-tonne towing rating, 5.7L HEMI V8, and the 523kW supercharged TRX monster.",
        "models_catalog": [
            {
                "model_slug": "ram-1500",
                "name": "RAM 1500",
                "vehicle_type": "Full-size Pickup Truck",
                "segment": "Full-size American Ute",
                "years_sold_au": {"start": 2018, "end": "Present"},
                "locally_built": True,
                "overview": "Locally remanufactured at Clayton VIC, offering 4.5-tonne towing, spacious crew cab luxury, 5.7L HEMI V8 rumble, and the 523kW supercharged TRX.",
                "generations": [
                    {"series_code": "DS", "generation_name": "RAM 1500 DS Classic", "years": {"start": 2018, "end": "2023"}, "body_styles": ["Quad Cab", "Crew Cab"], "summary": "5.7L HEMI V8 (291kW/556Nm), 8-speed automatic, 4.5-tonne braked towing, Express and Warlock editions."},
                    {"series_code": "DT", "generation_name": "RAM 1500 DT", "years": {"start": 2021, "end": "Present"}, "body_styles": ["Crew Cab"], "summary": "Redesigned high-strength steel chassis, eTorque mild-hybrid 5.7L HEMI V8, Laramie, Limited, and RamBox cargo management."},
                    {"series_code": "DT-TRX", "generation_name": "RAM 1500 TRX", "years": {"start": 2022, "end": "2024"}, "body_styles": ["Crew Cab"], "summary": "6.2L Supercharged Hellcat V8 (523kW / 882Nm), Bilstein Black Hawk e2 adaptive dampers, 35-inch tyres, 0-100 in 4.5s."},
                    {"series_code": "DT-Hurricane", "generation_name": "RAM 1500 Hurricane", "years": {"start": 2025, "end": "Present"}, "body_styles": ["Crew Cab"], "summary": "All-new 3.0L Twin-Turbo Hurricane inline-six producing 313kW (Standard Output) or 403kW (High Output)."}
                ]
            },
            {
                "model_slug": "ram-2500-3500",
                "name": "RAM 2500 / 3500 Heavy Duty",
                "vehicle_type": "Heavy Duty Pickup Truck",
                "segment": "Heavy Commercial / Hauler",
                "years_sold_au": {"start": 2015, "end": "Present"},
                "locally_built": True,
                "overview": "Commercial-grade haulers remanufactured at Clayton VIC, powered by the 6.7-litre Cummins inline-six turbo diesel with up to 8-tonne towing ratings.",
                "generations": [
                    {"series_code": "HD-Series", "generation_name": "RAM 2500 & 3500 HD", "years": {"start": 2015, "end": "Present"}, "body_styles": ["Crew Cab", "Mega Cab"], "summary": "6.7L Cummins High Output Turbo Diesel (276kW / 1152Nm), solid beam axles, dual rear wheels on 3500."}
                ]
            }
        ]
    },
    "chevrolet-gmsv": {
        "make_slug": "chevrolet-gmsv",
        "name": "Chevrolet / GMSV",
        "country_of_origin": "United States",
        "years_active_au": {"start": 1926, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "Historically assembled by General Motors-Holden across four decades, and reborn through GM Specialty Vehicles (GMSV) with Clayton-remanufactured Silverado trucks and factory RHD Corvette C8.",
        "australian_history": "Chevrolet has a profound place in Australian automotive history. In 1926, General Motors (Australia) was formed, partnering with Holden's Motor Body Builders to build Australian-bodied Chevrolets at Woodville, South Australia. The Chevrolet Stylemaster, Fleetline, Bel Air, and Impala were assembled in Australia through 1968, revered for rugged 'Stovebolt' sixes and small-block V8s. Following the closure of Holden in 2020, GM established GM Specialty Vehicles (GMSV). GMSV partners with Walkinshaw Automotive at Clayton, Victoria to remanufacture the Chevrolet Silverado 1500 and 2500HD to factory RHD standards. GMSV also imports the mid-engine Chevrolet Corvette C8 built in factory right-hand drive at Bowling Green, Kentucky.",
        "models_catalog": [
            {
                "model_slug": "silverado-1500",
                "name": "Silverado 1500",
                "vehicle_type": "Full-size Pickup Truck",
                "segment": "Full-size American Ute",
                "years_sold_au": {"start": 2020, "end": "Present"},
                "locally_built": True,
                "overview": "Full-size pickup remanufactured by Walkinshaw at Clayton VIC, powered by a 6.2-litre EcoTec3 V8 with 10-speed automatic and 4.5-tonne towing.",
                "generations": [
                    {"series_code": "T1XX", "generation_name": "Silverado 1500", "years": {"start": 2020, "end": "Present"}, "body_styles": ["Crew Cab"], "summary": "6.2L V8 (313kW / 624Nm), Dynamic Fuel Management, LTZ Premium, Trail Boss, and off-road flagship ZR2 with Multimatic DSSV spool-valve dampers."}
                ]
            },
            {
                "model_slug": "corvette",
                "name": "Corvette C8",
                "vehicle_type": "Coupe / Convertible",
                "segment": "Mid-Engine Supercar",
                "years_sold_au": {"start": 2021, "end": "Present"},
                "locally_built": False,
                "overview": "The first factory right-hand drive Corvette in history, bringing mid-engine exotic performance and naturally aspirated V8 roar to Australian dealerships.",
                "generations": [
                    {"series_code": "C8", "generation_name": "Corvette C8", "years": {"start": 2021, "end": "Present"}, "body_styles": ["2-door coupe (targa)", "Hardtop convertible"], "summary": "6.2L LT2 naturally aspirated V8 (369kW / 637Nm) in Stingray; 5.5L flat-plane crank LT6 V8 (500kW / 670hp) in screaming Z06."}
                ]
            }
        ]
    },
    "cadillac": {
        "make_slug": "cadillac",
        "name": "Cadillac",
        "country_of_origin": "United States",
        "years_active_au": {"start": 2024, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "General Motors' flagship luxury brand, officially entering Australia in 2024 as an all-electric prestige brand led by the Lyriq SUV.",
        "australian_history": "Cadillac originally planned to launch in Australia in late 2008 with the CTS sedan under GM Holden. Dozens of ADR-compliant right-hand drive cars were shipped to Melbourne and dealer agreements were signed, but the 2008 Global Financial Crisis and GM's subsequent chapter 11 restructuring forced an abrupt cancellation. In late 2023, GM announced that Cadillac would officially launch in Australia in 2024 as an all-electric luxury brand. Operating direct-to-consumer Cadillac Experience Centres in Sydney, Melbourne, and Brisbane, the brand debuted with the Lyriq mid-size luxury EV SUV built on GM's Ultium platform in factory right-hand drive.",
        "models_catalog": [
            {
                "model_slug": "lyriq",
                "name": "Lyriq",
                "vehicle_type": "SUV",
                "segment": "Large Luxury Electric SUV",
                "years_sold_au": {"start": 2024, "end": "Present"},
                "locally_built": False,
                "overview": "Cadillac's debut electric SUV in Australia, featuring 102kWh Ultium battery, 373kW dual-motor AWD, and a 33-inch curved LED 9K display.",
                "generations": [
                    {"series_code": "Lyriq-Gen1", "generation_name": "Lyriq", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Luxury and Sport trims, 373kW / 610Nm dual motors, 530km range, 19-speaker AKG audio, and illuminated black crystal shield grille."}
                ]
            }
        ]
    },
    "dodge": {
        "make_slug": "dodge",
        "name": "Dodge",
        "country_of_origin": "United States",
        "years_active_au": {"start": 1930, "end": "2016"},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Historic American marque manufactured in Adelaide by Chrysler Australia (including the iconic Dodge Phoenix), and reintroduced in the 2000s with the Caliber, Nitro, and Journey.",
        "australian_history": "Chrysler Australia assembled Dodge cars and commercial trucks for decades in South Australia at Mile End and Tonsley Park. The most famous Australian Dodge was the Dodge Phoenix, assembled in Adelaide from 1960 to 1972 from Plymouth fury/Dodge CKD packs with right-hand drive dashboards and high local content. Modern Dodge returned to Australia in 2006 under DaimlerChrysler, selling the Caliber hatchback, Nitro SUV, Avenger sedan, and Journey family crossover. The Dodge Journey was a steady family seller until Chrysler withdrew the brand from Australia in 2016 to focus on Jeep.",
        "models_catalog": [
            {
                "model_slug": "phoenix",
                "name": "Phoenix",
                "vehicle_type": "Sedan / Hardtop",
                "segment": "Large Luxury Car",
                "years_sold_au": {"start": 1960, "end": "1972"},
                "locally_built": True,
                "overview": "Assembled at Chrysler Australia's Tonsley Park plant in South Australia, offering full-size luxury, V8 power, and flamboyant American styling.",
                "generations": [
                    {"series_code": "PD-PF", "generation_name": "Dodge Phoenix", "years": {"start": 1960, "end": "1972"}, "body_styles": ["4-door sedan", "2-door hardtop", "4-door hardtop"], "summary": "Slant-six 225, 318 V8, 383 Big Block V8, Torqueflite automatic, and unique RHD instrument panel."}
                ]
            },
            {
                "model_slug": "journey",
                "name": "Journey",
                "vehicle_type": "Crossover / People Mover",
                "segment": "Large 7-seat Crossover",
                "years_sold_au": {"start": 2008, "end": "2016"},
                "locally_built": False,
                "overview": "Popular family 7-seater crossover featuring flexible Tilt 'n Slide seating and Pentastar V6 engine.",
                "generations": [
                    {"series_code": "JC49", "generation_name": "Dodge Journey", "years": {"start": 2008, "end": "2016"}, "body_styles": ["5-door 7-seat crossover"], "summary": "2.7L V6 and 2.0 CRD diesel, later upgraded to 206kW 3.6L Pentastar V6 and 8.4-inch Uconnect touchscreen."}
                ]
            }
        ]
    },
    "pontiac": {
        "make_slug": "pontiac",
        "name": "Pontiac",
        "country_of_origin": "United States",
        "years_active_au": {"start": 1930, "end": "1968"},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "GM-H manufactured Pontiac Laurentians and Parisiennes in Melbourne, Sydney, and Adelaide, before Australia exported Holden Monaros and Commodores back to America as the Pontiac GTO and G8.",
        "australian_history": "Pontiac has a reciprocal Australian legacy. From the 1930s until 1968, General Motors-Holden assembled Pontiacs in Australia (Silver Streak, Chieftain, Star Chief, Laurentian, and Parisienne). Using Canadian CKD packs, GM-H fitted local Australian-pressed bodies and Chevrolet running gear with factory right-hand drive. Four decades later, the relationship reversed: in 2004-2006, Holden exported over 40,000 Australian-designed and built Holden Monaro coupes from Elizabeth, South Australia to the United States as the Pontiac GTO (5.7L LS1 and 6.0L LS2). In 2008-2009, Holden exported the VE Commodore sedan as the critically acclaimed Pontiac G8 and G8 GXP before GM dissolved the Pontiac brand during the GFC.",
        "models_catalog": [
            {
                "model_slug": "laurentian-parisienne",
                "name": "Laurentian / Parisienne",
                "vehicle_type": "Sedan / Hardtop",
                "segment": "Large Luxury Car",
                "years_sold_au": {"start": 1958, "end": "1968"},
                "locally_built": True,
                "overview": "Assembled by General Motors-Holden at Fishermans Bend and Elizabeth, representing the height of GM prestige in Australia.",
                "generations": [
                    {"series_code": "GMH-Pontiac", "generation_name": "Pontiac Laurentian & Parisienne", "years": {"start": 1958, "end": "1968"}, "body_styles": ["4-door sedan", "4-door hardtop"], "summary": "Chevrolet 283 and 327 small-block V8 engines, Powerglide automatic, and Australian GM-H assembly."}
                ]
            },
            {
                "model_slug": "gto-g8-export",
                "name": "GTO / G8 (Australian Exports)",
                "vehicle_type": "Coupe / Sedan",
                "segment": "Performance Muscle Car",
                "years_sold_au": {"start": 2004, "end": "2009"},
                "locally_built": True,
                "overview": "Holden's export triumphs: Elizabeth-built Monaro and VE Commodore rebadged as Pontiac muscle icons for the North American market.",
                "generations": [
                    {"series_code": "V2-VE", "generation_name": "Pontiac GTO & G8", "years": {"start": 2004, "end": "2009"}, "body_styles": ["2-door coupe", "4-door sedan"], "summary": "Monaro-based GTO (LS1/LS2) and Commodore-based G8 (3.6 V6, 6.0 V8 GT, and 302kW 6.2L LS3 GXP with Tremec manual)."}
                ]
            }
        ]
    },
    "rambler-amc": {
        "make_slug": "rambler-amc",
        "name": "Rambler / AMC",
        "country_of_origin": "United States",
        "years_active_au": {"start": 1960, "end": "1977"},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Manufactured at Port Melbourne by Australian Motor Industries (AMI) from 1960 to 1977, producing right-hand drive Classic, Rebel, Matador, Hornet, and rare Javelin muscle cars.",
        "australian_history": "American Motors Corporation (AMC) partnered with Australian Motor Industries (AMI) in Port Melbourne, Victoria in 1960 to assemble Rambler passenger cars from CKD kits. AMI assembled the Rambler Classic, American, Rebel, and Matador sedans and wagons with right-hand drive, heavy-duty suspension, and Australian local content. In 1969-70, AMI assembled the sleek AMC Javelin muscle car—building 24 rare factory RHD Javelins with 343 and 390 V8 engines, which are today among the most valuable Australian collector muscle cars. AMI also assembled the compact AMC Hornet sedan with 258 inline-six and 304 V8 engines before AMC operations concluded in 1977.",
        "models_catalog": [
            {
                "model_slug": "rebel-matador",
                "name": "Rebel / Matador",
                "vehicle_type": "Sedan / Wagon / Coupe",
                "segment": "Large Luxury Car",
                "years_sold_au": {"start": 1967, "end": "1977"},
                "locally_built": True,
                "overview": "Assembled at AMI Port Melbourne, offering smooth American V8 luxury and robust towing capability for Australian conditions.",
                "generations": [
                    {"series_code": "Rebel-Matador-Series", "generation_name": "Rambler Rebel & Matador", "years": {"start": 1967, "end": "1977"}, "body_styles": ["4-door sedan", "Station wagon", "Matador X coupe"], "summary": "AMI-assembled; 343ci and 360ci V8, Borg-Warner Shift-Command automatic, and distinctive Matador X fastback coupe."}
                ]
            },
            {
                "model_slug": "javelin",
                "name": "Javelin",
                "vehicle_type": "Coupe",
                "segment": "Muscle Car",
                "years_sold_au": {"start": 1969, "end": "1974"},
                "locally_built": True,
                "overview": "Ultra-rare Australian muscle car assembled at Port Melbourne from CKD packs, featuring bulging wheel arches and high-output AMC V8s.",
                "generations": [
                    {"series_code": "Javelin-AMI", "generation_name": "AMC Javelin (Australian Assembled)", "years": {"start": 1969, "end": "1974"}, "body_styles": ["2-door coupe"], "summary": "Assembled by AMI in Port Melbourne; 343ci, 360ci, and 401ci V8 engines; highly prized Australian collector car."}
                ]
            }
        ]
    },
    "studebaker": {
        "make_slug": "studebaker",
        "name": "Studebaker",
        "country_of_origin": "United States",
        "years_active_au": {"start": 1960, "end": "1966"},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Manufactured locally at Canada Bay (Sydney) and Motor Producers (Clayton), Studebaker was celebrated for the Lark V8, which served as Australia's first purpose-built high-speed police pursuit vehicle.",
        "australian_history": "Studebaker vehicles were assembled in Australia from 1960 to 1966 by York Motors at Canada Bay in Sydney and by Motor Producers Limited in Clayton, Melbourne. The compact Studebaker Lark—fitted with the 259ci and 289ci V8 engines—became an Australian automotive sensation. In 1961, the Victoria Police and New South Wales Police selected the Studebaker Lark V8 as Australia's very first high-speed highway patrol pursuit car. The Lark could reach 105 mph (170 km/h) and outrun almost anything on Australian highways at the time. When Studebaker ceased car production in Canada in 1966, Australian assembly came to an end.",
        "models_catalog": [
            {
                "model_slug": "lark",
                "name": "Lark / Cruiser",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Medium / Large Car",
                "years_sold_au": {"start": 1960, "end": "1966"},
                "locally_built": True,
                "overview": "Locally assembled in Sydney and Melbourne; legendary as Australia's premier high-speed police pursuit special of the 1960s.",
                "generations": [
                    {"series_code": "Lark-Series", "generation_name": "Studebaker Lark", "years": {"start": 1960, "end": "1966"}, "body_styles": ["4-door sedan", "Cruiser sedan", "Wagon"], "summary": "259ci and 289ci Studebaker V8, Borg-Warner automatic, disc front brakes, and Police Pursuit Special packages."}
                ]
            }
        ]
    },
    "hummer": {
        "make_slug": "hummer",
        "name": "Hummer",
        "country_of_origin": "United States",
        "years_active_au": {"start": 2007, "end": "2010"},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "General Motors' military-styled 4x4 brand sold through GM Holden dealerships from 2007 to 2010 with the factory RHD Hummer H3.",
        "australian_history": "In mid-2007, GM Holden launched the Hummer brand in Australia, selling the right-hand drive Hummer H3 built at GM's Struandale assembly plant in Port Elizabeth, South Africa. Sold through premium Holden dealer franchises, the H3 offered unmistakable military styling, full-time four-wheel drive with low-range transfer case, and 33-inch all-terrain tyres. It was available with a 3.7-litre Vortec inline-five engine and later the 5.3-litre V8 H3 Alpha. Over 2,000 H3s were sold in Australia before GM wound down the Hummer brand globally following its 2009-2010 restructuring.",
        "models_catalog": [
            {
                "model_slug": "h3",
                "name": "H3",
                "vehicle_type": "SUV",
                "segment": "Mid-size 4WD SUV",
                "years_sold_au": {"start": 2007, "end": "2010"},
                "locally_built": False,
                "overview": "Factory right-hand drive midsize 4WD with aggressive broad-shouldered styling, skid plates, and full-time 4WD.",
                "generations": [
                    {"series_code": "GMT345", "generation_name": "Hummer H3", "years": {"start": 2007, "end": "2010"}, "body_styles": ["5-door SUV"], "summary": "3.7L Vortec inline-five (180kW) and 5.3L V8 Alpha (224kW / 434Nm), Adventure Pack with locking rear differential."}
                ]
            }
        ]
    }
}
