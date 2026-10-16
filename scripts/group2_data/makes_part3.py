"""Catalog data for Hyundai, Kia, Genesis, SsangYong/KGM, and Daewoo in Australia."""

MAKES_PART3 = [
    {
        "make_slug": "hyundai",
        "name": "Hyundai",
        "country_of_origin": "South Korea",
        "years_active_au": {"start": 1986, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "From Alan Bond's initial budget import of the Excel in 1986 to a permanent top-3 market contender renowned for Australian-tuned dynamics, Tucson, Santa Fe, and the i30 N hot hatch.",
        "australian_history": """Hyundai's entry into Australia is one of the most colourful chapters in local automotive history. In late 1985, Western Australian entrepreneur Alan Bond's Bond Motor Corporation unveiled the front-wheel-drive Hyundai Excel at the Perth Motor Show, officially beginning sales in February 1986. Priced aggressively with standard equipment that undercut Japanese rivals, the Excel quickly expanded nationally.

In the 1990s, under Hyundai Automotive Distributors Australia (HADA), the second and third-generation Excel (X2 and X3) became a sales phenomenon. The 1994-2000 X3 Excel, offered for years at $13,990 driveaway with free air-conditioning, became Australia's best-selling car outright in individual monthly sales runs and the default first car for a generation of Australians (later forming the basis for the national Excel Cup circuit racing series).

In 2003, Hyundai Motor Company Australia (HMCA) was formed as a direct factory subsidiary. A turning point arrived in 2007 with the launch of the first-generation i30 hatchback. Designed in Germany with a sophisticated multi-link rear suspension, the i30 won the 2007 Wheels Car of the Year award and marked Hyundai's transition from a cheap alternative to a class benchmark.

In 2011, HMCA pioneered an in-house Australian suspension and steering tuning program led by chassis engineer Graeme Gambold. Every Hyundai sold in Australia was tested over thousands of kilometres of coarse-chip bitumen, corrugated gravel, and off-camber country roads, custom-valving dampers and matching spring rates for Australia's unique topography. In 2017, Hyundai launched the high-performance N division in Australia with the i30 N, developed under former BMW M engineering chief Albert Biermann. Today, Hyundai stands as a technology leader with the Ioniq 5 and 6 electric vehicles, Palisade, Santa Fe, Tucson, and Kona.""",
        "models_catalog": [
            {
                "model_slug": "excel",
                "name": "Excel",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Light / Small Car",
                "years_sold_au": {"start": 1986, "end": "2000"},
                "locally_built": False,
                "overview": "The car that launched Hyundai in Australia, a runaway sales record-breaker and affordable motoring legend.",
                "generations": [
                    {"series_code": "X1", "generation_name": "Excel 1st Gen", "years": {"start": 1986, "end": 1989}, "body_styles": ["3-door Hatch", "5-door Hatch"], "summary": "1.5L Mitsubishi-derived Orion engine, 5-speed manual, Alan Bond Perth launch."},
                    {"series_code": "X2", "generation_name": "Excel 2nd Gen", "years": {"start": 1990, "end": 1994}, "body_styles": ["Hatchback", "Sedan"], "summary": "1.5L multi-point EFI, rounded aerodynamic styling; GL, GLS, Sprint."},
                    {"series_code": "X3", "generation_name": "Excel 3rd Gen", "years": {"start": 1994, "end": 2000}, "body_styles": ["3-door Hatch", "5-door Hatch", "Sedan"], "summary": "1.5L Alpha DOHC engine, $13,990 driveaway pioneer, Australia's top-selling small car; GX, Sprint, GLX."}
                ]
            },
            {
                "model_slug": "getz",
                "name": "Getz",
                "vehicle_type": "Hatchback",
                "segment": "Light Car",
                "years_sold_au": {"start": 2002, "end": "2011"},
                "locally_built": False,
                "overview": "Immensely popular European-styled budget city hatch, succeeding the Excel as Australia's value champion.",
                "generations": [
                    {"series_code": "TB", "generation_name": "Getz", "years": {"start": 2002, "end": 2011}, "body_styles": ["3-door Hatch", "5-door Hatch"], "summary": "1.3L, 1.4L, 1.5L, and 1.6L Alpha engines, exceptional interior packaging; XL, GL, S, SX."}
                ]
            },
            {
                "model_slug": "i30",
                "name": "i30",
                "vehicle_type": "Hatchback / Sedan / Fastback",
                "segment": "Small Car",
                "years_sold_au": {"start": 2007, "end": "Present"},
                "locally_built": False,
                "overview": "The car that transformed Hyundai's reputation in Australia, winner of Wheels COTY 2007 and home to the acclaimed i30 N hot hatch.",
                "generations": [
                    {"series_code": "FD", "generation_name": "i30 1st Gen", "years": {"start": 2007, "end": 2012}, "body_styles": ["5-door Hatch", "cw Wagon"], "summary": "2.0L Beta II petrol and 1.6L CRDi turbo-diesel, multi-link rear suspension; Wheels COTY 2007."},
                    {"series_code": "GD", "generation_name": "i30 2nd Gen", "years": {"start": 2012, "end": 2017}, "body_styles": ["5-door Hatch", "Tourer Wagon"], "summary": "Fluidic Sculpture design, 1.8L Nu and 2.0L GDi petrol, 1.6L CRDi; Australian suspension tune."},
                    {"series_code": "PD", "generation_name": "i30 3rd Gen", "years": {"start": 2017, "end": "Present"}, "body_styles": ["5-door Hatch", "Fastback", "Sedan (CN7)"], "summary": "2.0L petrol, 1.6L Turbo N Line (150kW), and Albert Biermann-engineered i30 N 2.0L Turbo (206kW/392Nm)."}
                ]
            },
            {
                "model_slug": "tucson",
                "name": "Tucson / ix35",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 2004, "end": "Present"},
                "locally_built": False,
                "overview": "High-volume family SUV that spearheaded Hyundai's SUV growth in Australia across four generations.",
                "generations": [
                    {"series_code": "JM", "generation_name": "Tucson 1st Gen", "years": {"start": 2004, "end": 2010}, "body_styles": ["5-door SUV"], "summary": "2.0L 4-cylinder and 2.7L Delta V6 petrol, 4WD lock system; City and Elite."},
                    {"series_code": "LM", "generation_name": "ix35 2nd Gen", "years": {"start": 2010, "end": 2015}, "body_styles": ["5-door SUV"], "summary": "Badged ix35 in Australia, 2.0L/2.4L Theta II and 2.0L R-Series turbo-diesel (135kW/392Nm); Active, Elite, Highlander."},
                    {"series_code": "TL", "generation_name": "Tucson 3rd Gen", "years": {"start": 2015, "end": 2021}, "body_styles": ["5-door SUV"], "summary": "Reverted to Tucson badge, 2.0L GDi, 1.6L Turbo (7-speed DCT), 2.0L diesel; local suspension tuning."},
                    {"series_code": "NX4", "generation_name": "Tucson 4th Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Parametric Jewel design, 2.0L petrol, 1.6L Turbo AWD, 2.0L Diesel, and 1.6L Turbo Hybrid (HEV)."}
                ]
            },
            {
                "model_slug": "santa-fe",
                "name": "Santa Fe",
                "vehicle_type": "SUV",
                "segment": "Large SUV",
                "years_sold_au": {"start": 2000, "end": "Present"},
                "locally_built": False,
                "overview": "Long-running 7-seat family touring SUV, celebrated for punchy R-Series turbo-diesel torque and towing capability.",
                "generations": [
                    {"series_code": "SM", "generation_name": "Santa Fe 1st Gen", "years": {"start": 2000, "end": 2006}, "body_styles": ["5-door SUV"], "summary": "2.7L Delta V6 and 3.5L Sigma V6, full-time AWD, wide muscular body."},
                    {"series_code": "CM", "generation_name": "Santa Fe 2nd Gen", "years": {"start": 2006, "end": 2012}, "body_styles": ["5-door SUV (7 seats)"], "summary": "Introduced 7-passenger capability, 2.2L CRDi diesel and 3.3L/3.5L Lambda V6 petrol."},
                    {"series_code": "DM", "generation_name": "Santa Fe 3rd Gen", "years": {"start": 2012, "end": 2018}, "body_styles": ["5-door SUV (7 seats)"], "summary": "Storm Edge design, 2.2L R-series diesel (147kW/440Nm), local Australian chassis tune."},
                    {"series_code": "TM", "generation_name": "Santa Fe 4th Gen", "years": {"start": 2018, "end": 2024}, "body_styles": ["5-door SUV (7 seats)"], "summary": "3.5L V6 FWD, 2.2L Diesel AWD, and 1.6L Turbo Hybrid AWD; HTRAC AWD."},
                    {"series_code": "MX5", "generation_name": "Santa Fe 5th Gen", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door SUV (7 seats)"], "summary": "Bold geometric retro-futuristic boxy styling, 1.6L Turbo Hybrid and 2.5L Turbo petrol."}
                ]
            },
            {
                "model_slug": "ioniq-5",
                "name": "Ioniq 5",
                "vehicle_type": "Electric Crossover",
                "segment": "Medium EV",
                "years_sold_au": {"start": 2021, "end": "Present"},
                "locally_built": False,
                "overview": "Retro-futuristic EV on the 800V E-GMP platform, featuring ultra-fast charging and the 478kW Ioniq 5 N performance hero.",
                "generations": [
                    {"series_code": "NE", "generation_name": "Ioniq 5 1st Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["5-door EV Crossover"], "summary": "58kWh/72.6kWh/77.4kWh/84kWh batteries, 800V architecture (10-80% in 18 min); Ioniq 5 N 478kW AWD."}
                ]
            }
        ]
    },
    {
        "make_slug": "kia",
        "name": "Kia",
        "country_of_origin": "South Korea",
        "years_active_au": {"start": 1996, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "From value entry to a top-4 Australian automotive powerhouse, renowned for local suspension tuning, an industry-first 7-year warranty, Carnival, Sportage, and the twin-turbo V6 Stinger.",
        "australian_history": """Kia entered the Australian market in 1996 through independent distributor Inchcape, launching with the budget Mentor sedan and the compact body-on-frame Sportage 4x4. In 1999, Kia changed the Australian family transport landscape with the Carnival people mover. Seating seven with dual sliding doors and V6 power for the price of a small hatchback, the Carnival became Australia's dominant people mover for decades.

In 2006, Kia Motors Australia (KMAu) was formed as a factory-owned subsidiary. That same year, German designer Peter Schreyer was appointed Chief Design Officer, giving Kia an instantly recognizable global design identity anchored by the 'Tiger Nose' grille.

Recognizing the distinct challenges of Australian roads, Kia launched an extensive local ride and handling tuning program. Every new model underwent rigorous suspension calibration on regional Victorian and New South Wales roads, tailoring spring rates, sway bars, and damper valving to tame undulating country highways. In 2014, Kia revolutionized the Australian automotive industry by introducing an unprecedented 7-Year Unlimited Kilometre Warranty with 7 years of capped-price servicing and roadside assist.

In 2017, Kia stunned the performance car market with the rear-wheel-drive Stinger fastback. Powered by a 272kW 3.3L twin-turbo Lambda II V6, the Stinger was enthusiastically adopted by Australian driving enthusiasts and chosen by the Queensland and Northern Territory Police as high-speed highway pursuit interceptors following the departure of the Holden Commodore and Ford Falcon. In 2022, the electric EV6 won Wheels Car of the Year. In 2024-2025, Kia announced the Tasman dual-cab ute, torture-tested across the Australian outback. Today, Kia consistently ranks as one of Australia's top four automotive brands.""",
        "models_catalog": [
            {
                "model_slug": "stinger",
                "name": "Stinger",
                "vehicle_type": "Sports Fastback Liftback",
                "segment": "Large Sports Sedan",
                "years_sold_au": {"start": 2017, "end": "2023"},
                "locally_built": False,
                "overview": "Albert Biermann-engineered rear-wheel-drive performance fastback that became Australia's spiritual V8 Commodore/Falcon replacement and police highway patrol interceptor.",
                "generations": [
                    {"series_code": "CK", "generation_name": "Stinger (AU)", "years": {"start": 2017, "end": 2023}, "body_styles": ["5-door Liftback Fastback"], "summary": "2.0L Turbo Theta II (182kW) and 3.3L Twin-Turbo V6 Lambda II (272kW/510Nm); Brembo brakes, mechanical LSD; 200S, 330S, GT-Line, GT, Tribute Edition."}
                ]
            },
            {
                "model_slug": "carnival",
                "name": "Carnival",
                "vehicle_type": "People Mover",
                "segment": "People Mover",
                "years_sold_au": {"start": 1999, "end": "Present"},
                "locally_built": False,
                "overview": "The absolute king of Australian family people movers, holding over 70% market share in its segment across four generations.",
                "generations": [
                    {"series_code": "KV-II", "generation_name": "Carnival 1st Gen", "years": {"start": 1999, "end": 2006}, "body_styles": ["People Mover (7 seats)"], "summary": "2.5L Rover KV6 petrol engine, dual sliding doors, unbeatable space-for-money value."},
                    {"series_code": "VQ", "generation_name": "Grand Carnival 2nd Gen", "years": {"start": 2006, "end": 2014}, "body_styles": ["People Mover (8 seats)"], "summary": "3.8L V6 petrol and 2.9L/2.2L R-series turbo-diesel, in-floor folding rear seats."},
                    {"series_code": "YP", "generation_name": "Carnival 3rd Gen", "years": {"start": 2015, "end": 2020}, "body_styles": ["People Mover (8 seats)"], "summary": "Peter Schreyer styling, 3.3L Lambda V6 and 2.2L CRDi diesel (147kW/440Nm); S, Si, SLi, Platinum."},
                    {"series_code": "KA4", "generation_name": "Carnival 4th Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["People Mover (8 seats)"], "summary": "SUV-inspired styling, 3.5L V6, 2.2L Smartstream diesel, and 1.6L Turbo Hybrid (HEV)."}
                ]
            },
            {
                "model_slug": "sportage",
                "name": "Sportage",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 1997, "end": "Present"},
                "locally_built": False,
                "overview": "Kia's global cornerstone SUV, transformed by Peter Schreyer design and Australian ride and handling tuning.",
                "generations": [
                    {"series_code": "JA", "generation_name": "Sportage 1st Gen", "years": {"start": 1997, "end": 2003}, "body_styles": ["5-door 4WD Wagon"], "summary": "Body-on-frame chassis, 2.0L Mazda-derived petrol, dual-range 4WD."},
                    {"series_code": "KM", "generation_name": "Sportage 2nd Gen", "years": {"start": 2005, "end": 2010}, "body_styles": ["5-door SUV"], "summary": "Monocoque crossover, 2.0L 4-cylinder and 2.7L Delta V6; front-wheel drive and AWD."},
                    {"series_code": "SL", "generation_name": "Sportage 3rd Gen", "years": {"start": 2010, "end": 2015}, "body_styles": ["5-door SUV"], "summary": "Design breakthrough by Peter Schreyer, 2.0L/2.4L petrol and 2.0L R-series diesel; local suspension tune."},
                    {"series_code": "QL", "generation_name": "Sportage 4th Gen", "years": {"start": 2015, "end": 2021}, "body_styles": ["5-door SUV"], "summary": "Ice-cube fog lights, 2.0L petrol, 2.4L petrol, 2.0L turbo-diesel AWD; S, Si, GT-Line."},
                    {"series_code": "NQ5", "generation_name": "Sportage 5th Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Boomerang LED DRLs, 2.0L petrol, 1.6L Turbo AWD, 2.0L Diesel AWD, and 1.6L Turbo Hybrid."}
                ]
            },
            {
                "model_slug": "cerato",
                "name": "Cerato",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Small Car",
                "years_sold_au": {"start": 2004, "end": "Present"},
                "locally_built": False,
                "overview": "Consistently one of Australia's highest-selling small passenger cars, backed by strong value and 7-year warranty.",
                "generations": [
                    {"series_code": "LD", "generation_name": "Cerato 1st Gen", "years": {"start": 2004, "end": 2009}, "body_styles": ["Hatchback", "Sedan"], "summary": "2.0L Beta II petrol 105kW, practical roomy compact transport."},
                    {"series_code": "TD", "generation_name": "Cerato 2nd Gen", "years": {"start": 2009, "end": 2013}, "body_styles": ["Sedan", "Hatchback", "Koup 2-door"], "summary": "Sharp modern styling, 2.0L Theta II, 2.4L in Cerato Koup sports coupe."},
                    {"series_code": "YD", "generation_name": "Cerato 3rd Gen", "years": {"start": 2013, "end": 2018}, "body_styles": ["Hatchback", "Sedan", "Koup"], "summary": "1.8L Nu and 2.0L Nu GDI, 1.6L Turbo (150kW in Koup/GT), local suspension calibration."},
                    {"series_code": "BD", "generation_name": "Cerato 4th Gen", "years": {"start": 2018, "end": "Present"}, "body_styles": ["Hatchback", "Sedan"], "summary": "2.0L MPI petrol and 1.6L Turbo GT (150kW with multi-link rear); S, Sport, Sport+, GT."}
                ]
            },
            {
                "model_slug": "sorento",
                "name": "Sorento",
                "vehicle_type": "SUV",
                "segment": "Large SUV",
                "years_sold_au": {"start": 2003, "end": "Present"},
                "locally_built": False,
                "overview": "From heavy-duty ladder-chassis 4WD to award-winning family 7-seater luxury crossover.",
                "generations": [
                    {"series_code": "BL", "generation_name": "Sorento 1st Gen", "years": {"start": 2003, "end": 2009}, "body_styles": ["5-door 4WD"], "summary": "Ladder frame, dual-range 4WD, 3.5L/3.8L V6 petrol and 2.5L CRDi diesel."},
                    {"series_code": "XM", "generation_name": "Sorento 2nd Gen", "years": {"start": 2009, "end": 2015}, "body_styles": ["5-door SUV (7 seats)"], "summary": "Monocoque chassis, 2.2L R-series diesel (145kW/436Nm) and 3.5L V6; local suspension tune."},
                    {"series_code": "UM", "generation_name": "Sorento 3rd Gen", "years": {"start": 2015, "end": 2020}, "body_styles": ["5-door SUV (7 seats)"], "summary": "Refined executive cabin, 3.5L V6 FWD and 2.2L Diesel AWD; Si, SLi, GT-Line."},
                    {"series_code": "MQ4", "generation_name": "Sorento 4th Gen", "years": {"start": 2020, "end": "Present"}, "body_styles": ["5-door SUV (7 seats)"], "summary": "N3 platform, 3.5L V6, 2.2L Smartstream diesel, 1.6L Turbo Hybrid, and 1.6L Plug-in Hybrid (PHEV)."}
                ]
            },
            {
                "model_slug": "ev6",
                "name": "EV6",
                "vehicle_type": "Electric Crossover",
                "segment": "Medium EV",
                "years_sold_au": {"start": 2022, "end": "Present"},
                "locally_built": False,
                "overview": "800V electric crossover that won Wheels Car of the Year 2022, culminating in the 430kW EV6 GT.",
                "generations": [
                    {"series_code": "CV", "generation_name": "EV6", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door EV Crossover"], "summary": "77.4kWh/84kWh battery, 800V charging, Air RWD, GT-Line AWD (239kW), and EV6 GT (430kW/740Nm supercar accelerator)."}
                ]
            }
        ]
    },
    {
        "make_slug": "genesis",
        "name": "Genesis",
        "country_of_origin": "South Korea",
        "years_active_au": {"start": 2019, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Hyundai Motor Group's standalone luxury brand, operating an agency model with luxury studios in Sydney, Melbourne, Brisbane, and Perth.",
        "australian_history": """Genesis originally debuted in Australia in 2014 as a single model under the Hyundai banner: the Hyundai Genesis sedan (DH series). Praised for its 3.8L V6 powertrain, whisper-quiet cabin, and a then-record ANCAP safety score of 36.88 out of 37, it served as an executive limousine and government hire car.

In June 2019, Genesis officially launched as an independent luxury brand in Australia, opening its first opulent 'Genesis Studio' in Sydney's Pitt Street Mall. Genesis adopted an innovative fixed-price direct-to-consumer agency model, eliminating dealership price haggling and offering the 'Genesis Difference'—a 5-year warranty, complimentary scheduled servicing, and valet pick-up with loan cars.

The standalone rollout began with the G70 rear-wheel-drive sports sedan and G80 executive sedan. In 2020, Genesis introduced the GV80 luxury SUV, featuring 3.0L inline-6 turbo-diesel and 3.5L twin-turbo V6 power. The mid-size GV70 arrived in 2021, swiftly becoming the brand's top seller in Australia. In 2022, Genesis launched its dedicated electric vehicles: the GV60 on the 800V E-GMP platform, alongside electrified versions of the G80 and GV70.""",
        "models_catalog": [
            {
                "model_slug": "g70",
                "name": "G70",
                "vehicle_type": "Sedan / Shooting Brake",
                "segment": "Medium Luxury Sedan",
                "years_sold_au": {"start": 2019, "end": "Present"},
                "locally_built": False,
                "overview": "Rear-wheel-drive sports sedan and Shooting Brake wagon taking on the BMW 3 Series with 3.3L twin-turbo V6 power.",
                "generations": [
                    {"series_code": "IK", "generation_name": "G70", "years": {"start": 2019, "end": "Present"}, "body_styles": ["Sedan", "Shooting Brake"], "summary": "2.0L Turbo (179kW) and 3.3L Twin-Turbo V6 (274kW/510Nm); Brembo brakes, mechanical LSD."}
                ]
            },
            {
                "model_slug": "gv70",
                "name": "GV70",
                "vehicle_type": "SUV",
                "segment": "Medium Luxury SUV",
                "years_sold_au": {"start": 2021, "end": "Present"},
                "locally_built": False,
                "overview": "Genesis's best-selling model in Australia, combining athletic design with 280kW V6 turbo and Electrified twin-motor EV options.",
                "generations": [
                    {"series_code": "JK1", "generation_name": "GV70", "years": {"start": 2021, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "2.5L Turbo petrol (224kW), 3.5L Twin-Turbo V6 (280kW), 2.2L diesel, and Electrified GV70 EV (360kW)."}
                ]
            },
            {
                "model_slug": "gv80",
                "name": "GV80",
                "vehicle_type": "SUV",
                "segment": "Large Luxury SUV",
                "years_sold_au": {"start": 2020, "end": "Present"},
                "locally_built": False,
                "overview": "Full-size flagship luxury SUV offering 7 seats, rear-drive architecture, and Road Preview electronic suspension.",
                "generations": [
                    {"series_code": "JX1", "generation_name": "GV80", "years": {"start": 2020, "end": "Present"}, "body_styles": ["5-door SUV", "Coupe"], "summary": "2.5L Turbo petrol, 3.0L Inline-6 Turbo-diesel (204kW/588Nm), and 3.5L Twin-Turbo V6 (280kW/530Nm)."}
                ]
            }
        ]
    },
    {
        "make_slug": "ssangyong-kgm",
        "name": "SsangYong / KGM",
        "country_of_origin": "South Korea",
        "years_active_au": {"start": 1997, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Specialists in rugged ladder-frame utes and heavy-duty 4x4 wagons, originally powered by Mercedes-Benz-derived drivetrains and rebranded to KGM in 2024.",
        "australian_history": """SsangYong's Australian journey began in 1995-1997 when the Musso 4x4 wagon was imported by independent distributors and Mercedes-Benz dealerships. Boasting styling by British designer Ken Greenley and Mercedes-Benz-licensed engines (notably the OM662 2.9L 5-cylinder diesel and M104 3.2L inline-6), the Musso offered European diesel reliability at an accessible price.

In 1998, the short-wheelbase Korando 3-door 4x4 arrived, followed in 2003 by the Rexton, a body-on-frame 7-seat SUV utilizing Mercedes-Benz W163 M-Class underpinnings. In 2005, SsangYong introduced the controversial Stavic people mover, powered by a 2.7L 5-cylinder common-rail turbo-diesel. In 2006, the Actyon SUV and Actyon Sports dual-cab ute arrived, making SsangYong an early pioneer in the sub-$30k lifestyle diesel ute segment.

In late 2018, SsangYong Motor Australia established a direct factory-owned subsidiary headquartered in Melbourne, relaunching the brand with the Musso dual-cab ute, Rexton SUV, and Tivoli compact crossover, backed by a 7-year unlimited-kilometre warranty. In 2022-2024, following the acquisition of SsangYong by South Korean industrial giant KG Group, the brand began transitioning its global and Australian identity to KGM (KG Mobility). KGM launched the adventure-oriented Torres SUV and refreshed Musso ute, maintaining strong demand among trades and rural towing buyers.""",
        "models_catalog": [
            {
                "model_slug": "musso",
                "name": "Musso",
                "vehicle_type": "4WD Wagon / Dual Cab Ute",
                "segment": "Large 4WD / Light Commercial",
                "years_sold_au": {"start": 1995, "end": "Present"},
                "locally_built": False,
                "overview": "Originally a Mercedes-Benz-powered 4WD wagon in the 1990s, revived in 2018 as a value-packed dual-cab ute with coil-spring and leaf-spring rear options.",
                "generations": [
                    {"series_code": "FJ", "generation_name": "Musso 1st Gen (Wagon)", "years": {"start": 1995, "end": 2006}, "body_styles": ["5-door Wagon"], "summary": "Mercedes-Benz licensed 2.9L 5-cylinder diesel and 3.2L inline-6 petrol engines, dual-range 4WD."},
                    {"series_code": "Q200", "generation_name": "Musso 2nd Gen (Ute)", "years": {"start": 2018, "end": "Present"}, "body_styles": ["Dual Cab Ute", "Musso XLV Long-Bed"], "summary": "2.2L e-XDi turbo-diesel (133kW/420Nm), 3500kg towing, coil-spring or leaf-spring rear; ELX, Ultimate."}
                ]
            },
            {
                "model_slug": "rexton",
                "name": "Rexton",
                "vehicle_type": "SUV",
                "segment": "Large 4WD SUV",
                "years_sold_au": {"start": 2003, "end": "Present"},
                "locally_built": False,
                "overview": "Heavy-duty 7-seat body-on-frame 4WD wagon offering 3.5-tonne towing and luxury equipment.",
                "generations": [
                    {"series_code": "Y200/Y250", "generation_name": "Rexton 1st Gen", "years": {"start": 2003, "end": 2017}, "body_styles": ["5-door Wagon (7 seats)"], "summary": "2.7L 5-cylinder common-rail diesel and 3.2L petrol, Mercedes-Benz 5-speed Tiptronic auto."},
                    {"series_code": "Y400", "generation_name": "Rexton 2nd Gen", "years": {"start": 2018, "end": "Present"}, "body_styles": ["5-door Wagon (7 seats)"], "summary": "High-strength steel quad-frame, 2.2L e-XDi diesel (148kW/441Nm), 8-speed automatic, 3500kg towing; ELX, Ultimate."}
                ]
            },
            {
                "model_slug": "korando",
                "name": "Korando",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 1998, "end": "Present"},
                "locally_built": False,
                "overview": "From a quirky 3-door body-on-frame off-roader to a modern monocoque compact family SUV.",
                "generations": [
                    {"series_code": "KJ", "generation_name": "Korando 2nd Gen", "years": {"start": 1998, "end": 2006}, "body_styles": ["3-door SWB 4WD"], "summary": "Mercedes-Benz 2.3L/2.9L diesel and 3.2L petrol, dual-range 4WD, distinctive retro styling."},
                    {"series_code": "C200/C300", "generation_name": "Korando 3rd/4th Gen", "years": {"start": 2011, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Monocoque crossover, 2.0L diesel then 1.5L Turbo petrol (120kW), front-wheel drive and AWD."}
                ]
            }
        ]
    },
    {
        "make_slug": "daewoo",
        "name": "Daewoo",
        "country_of_origin": "South Korea",
        "years_active_au": {"start": 1994, "end": 2004},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Popular 1990s and early-2000s Korean value brand in Australia, known for 'Free Care' 3-year servicing before its models were absorbed into Holden.",
        "australian_history": """Daewoo Automotive Australia was established in 1994 by South Korea's massive industrial chaebol, Daewoo Corporation. Entering the market with the 1.5i hatchback and Espero mid-size sedan (featuring Bertone styling), Daewoo quickly made headlines with the 'Free Care' program, which included 3 years or 100,000 km of free scheduled maintenance, parts, and labour—an Australian industry first that drastically lowered barriers to entry for budget car buyers.

In 1995, Daewoo introduced the Cielo (an evolution of the 1.5i/Opel Kadett). In 1997, Daewoo launched its second-generation lineup with styling commissioned from legendary Italian design houses: the compact Lanos (styled by Giorgetto Giugiaro / Italdesign), the Nubira small car (I.DE.A Institute), and the Leganza executive sedan (Giugiaro). In 1999, the Matiz micro-car joined the range, becoming one of Australia's cheapest city runabouts.

Following the collapse of the Daewoo Group during the late-1990s Asian financial crisis, General Motors acquired Daewoo's core automotive assets in 2002 to form GM Daewoo (GMDAT). In Australia, General Motors-Holden began leveraging GM Daewoo's cost-effective manufacturing. By late 2004, the standalone Daewoo brand was officially retired in Australia. Subsequent GM Daewoo vehicles were re-engineered by Holden in Melbourne and sold under the Holden lion badge: the Daewoo Kalos became the Holden Barina (TK), the Lacetti and Tacuma became the Holden Viva (JF), the Magnus became the Holden Epica (EP), and the Winstorm became the popular Holden Captiva (CG).""",
        "models_catalog": [
            {
                "model_slug": "lanos",
                "name": "Lanos",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Light Car",
                "years_sold_au": {"start": 1997, "end": "2003"},
                "locally_built": False,
                "overview": "Giugiaro-styled light car, a top-selling budget runabout with Daewoo's 3-year Free Care package.",
                "generations": [
                    {"series_code": "T100", "generation_name": "Lanos", "years": {"start": 1997, "end": 2003}, "body_styles": ["3-door Hatch", "5-door Hatch", "4-door Sedan"], "summary": "1.5L SOHC (63kW) and 1.6L DOHC (78kW) engines; SE, SX, and Sport trims."}
                ]
            },
            {
                "model_slug": "matiz",
                "name": "Matiz",
                "vehicle_type": "Hatchback",
                "segment": "Micro Car",
                "years_sold_au": {"start": 1999, "end": "2004"},
                "locally_built": False,
                "overview": "Tiny 5-door city runabout styled by Italdesign Giugiaro, offering 5-door versatility in a sub-3.5m length.",
                "generations": [
                    {"series_code": "M100/M150", "generation_name": "Matiz", "years": {"start": 1999, "end": 2004}, "body_styles": ["5-door Hatch"], "summary": "796cc 3-cylinder engine (38kW), 5-speed manual, air conditioning and power steering standard."}
                ]
            },
            {
                "model_slug": "nubira",
                "name": "Nubira",
                "vehicle_type": "Sedan / Hatchback / Wagon",
                "segment": "Small Car",
                "years_sold_au": {"start": 1997, "end": "2003"},
                "locally_built": False,
                "overview": "Spacious compact car engineered in the UK and styled by I.DE.A Institute in Italy.",
                "generations": [
                    {"series_code": "J100/J150", "generation_name": "Nubira", "years": {"start": 1997, "end": 2003}, "body_styles": ["Sedan", "Hatchback", "Wagon"], "summary": "1.6L and 2.0L DOHC engines, SE and CDX grades, exceptional wagon load volume."}
                ]
            },
            {
                "model_slug": "leganza",
                "name": "Leganza",
                "vehicle_type": "Sedan",
                "segment": "Mid-size Car",
                "years_sold_au": {"start": 1997, "end": "2004"},
                "locally_built": False,
                "overview": "Daewoo's flagship luxury sedan, styled by Giugiaro with Lotus-assisted suspension tuning.",
                "generations": [
                    {"series_code": "V100", "generation_name": "Leganza", "years": {"start": 1997, "end": 2004}, "body_styles": ["Sedan"], "summary": "2.0L and 2.2L DOHC engines (100kW), leather interior, woodgrain trim; SX and CDX."}
                ]
            }
        ]
    }
]
