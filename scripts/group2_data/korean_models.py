"""Deep-dive model data for South Korea: Hyundai i30 and Kia Stinger."""

I30_MODEL = {
    "make_slug": "hyundai",
    "model_slug": "i30",
    "name": "i30",
    "vehicle_type": "Hatchback / Sedan / Fastback",
    "segment": "Small Car",
    "years_sold_au": {"start": 2007, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Hyundai i30 is the vehicle that transformed Australian perceptions of the brand from budget-oriented to class-leading. Winner of the 2007 Wheels Car of the Year, it has been an Australian small car benchmark and gave rise to the sensational Albert Biermann-developed i30 N hot hatch.",
    "australian_market_notes": "First launched in 2007 with standard multi-link rear suspension and punchy diesel options, the i30 shocked the establishment by beating European and Japanese rivals to win Wheels COTY. From 2011 onward, Hyundai Australia tailored spring rates, sway bars, and damper valving specifically for Australia's corrugated country roads. In 2018, the i30 N arrived, instantly cementing itself as one of the finest front-wheel-drive performance hatchbacks ever sold in Australia.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "FD",
            "generation_name": "i30 1st Generation",
            "years": {"start": 2007, "end": "2012"},
            "body_styles": ["5-door Hatchback", "cw Wagon"],
            "platform": "Hyundai-Kia J4",
            "ancap_rating": "5 Stars",
            "summary": "Designed in Germany with multi-link rear suspension, winning Wheels Car of the Year 2007 and proving that affordable Korean hatchbacks could match European vehicle dynamics.",
            "engines": [
                {
                    "engine_code": "G4GC",
                    "name": "Hyundai Beta II 2.0L",
                    "displacement_cc": 1975,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 105.0,
                    "power_rpm": "6000",
                    "torque_nm": 186.0,
                    "torque_rpm": "4500",
                    "compression_ratio": "10.1:1",
                    "valvetrain": "DOHC 16-valve CVVT",
                    "notes": "Standard 2.0L petrol engine across SX, SLX, and Sport."
                },
                {
                    "engine_code": "D4FB",
                    "name": "Hyundai U 1.6L CRDi Turbo-Diesel",
                    "displacement_cc": 1582,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 85.0,
                    "power_rpm": "4000",
                    "torque_nm": 255.0,
                    "torque_rpm": "1900-2750",
                    "compression_ratio": "17.3:1",
                    "valvetrain": "DOHC 16-valve Variable Geometry Turbo (VGT)",
                    "notes": "Benchmark 4.7L/100km fuel economy in manual trim."
                }
            ],
            "badges": [
                {
                    "badge_name": "SX",
                    "years": {"start": 2007, "end": "2012"},
                    "body_styles": ["5-door Hatch", "cw Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed auto"],
                    "msrp_aud_min": 18990,
                    "msrp_aud_max": 23490,
                    "fuel_consumption_l_100km": 7.2,
                    "kerb_weight_kg": 1260,
                    "standard_features": ["Electronic Stability Control (ESC)", "Multi-link rear suspension", "Air conditioning", "USB/iPod connectivity", "ABS with EBD"],
                    "notes": "Wheels Car of the Year 2007 winner."
                },
                {
                    "badge_name": "SLX CRDi",
                    "years": {"start": 2007, "end": "2012"},
                    "body_styles": ["5-door Hatch", "cw Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed auto"],
                    "msrp_aud_min": 25490,
                    "msrp_aud_max": 28990,
                    "fuel_consumption_l_100km": 4.7,
                    "kerb_weight_kg": 1340,
                    "standard_features": ["16-inch alloy wheels", "Climate control air conditioning", "Cruise control", "Leather-wrapped steering wheel", "Front fog lights"],
                    "notes": "Long-range fuel economy champion."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SX 2.0",
                    "body_style": "5-door Hatch",
                    "engine_code": "G4GC",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2007,
                    "years_end": "2012",
                    "msrp_aud": 18990,
                    "power_kw": 105.0,
                    "torque_nm": 186.0,
                    "fuel_l_100km": 7.2,
                    "towing_braked_kg": 1200,
                    "notes": "2007 Wheels COTY winner."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "GD",
            "generation_name": "i30 2nd Generation",
            "years": {"start": 2012, "end": "2017"},
            "body_styles": ["5-door Hatch", "Tourer Wagon"],
            "platform": "Hyundai-Kia J5",
            "ancap_rating": "5 Stars",
            "summary": "Fluidic Sculpture design language, debut of the in-house Australian ride and handling suspension program, and the sporty 2.0L GDi SR warm hatch.",
            "engines": [
                {
                    "engine_code": "G4NC",
                    "name": "Hyundai Nu 2.0L GDi",
                    "displacement_cc": 1999,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 124.0,
                    "power_rpm": "6500",
                    "torque_nm": 201.0,
                    "torque_rpm": "4700",
                    "compression_ratio": "11.5:1",
                    "valvetrain": "DOHC 16-valve Gasoline Direct Injection (GDI)",
                    "notes": "Punchy 124kW direct-injected engine developed for the Australian-market i30 SR."
                }
            ],
            "badges": [
                {
                    "badge_name": "Active",
                    "years": {"start": 2012, "end": "2017"},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 20990,
                    "msrp_aud_max": 24500,
                    "fuel_consumption_l_100km": 6.8,
                    "kerb_weight_kg": 1265,
                    "standard_features": ["5-inch touchscreen", "7 airbags", "Flex Steer adjustable steering weights", "Reverse sensors", "Cruise control"],
                    "notes": "Australia's default fleet and private hatchback."
                },
                {
                    "badge_name": "SR",
                    "years": {"start": 2013, "end": "2017"},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 27990,
                    "msrp_aud_max": 31990,
                    "fuel_consumption_l_100km": 7.2,
                    "kerb_weight_kg": 1320,
                    "standard_features": ["124kW 2.0L GDi engine", "Aussie-tuned sports suspension", "17-inch machined alloy wheels", "Sports front grille and rear diffuser", "Alloy sports pedals", "7-inch sat-nav"],
                    "notes": "Australian engineering team development benchmark."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SR",
                    "body_style": "5-door Hatch",
                    "engine_code": "G4NC",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2013,
                    "years_end": "2017",
                    "msrp_aud": 27990,
                    "power_kw": 124.0,
                    "torque_nm": 201.0,
                    "fuel_l_100km": 7.2,
                    "towing_braked_kg": 1300,
                    "notes": "GD i30 SR."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "PD",
            "generation_name": "i30 3rd Generation (and i30 N)",
            "years": {"start": 2017, "end": "Present"},
            "body_styles": ["5-door Hatch", "Fastback", "Sedan (CN7)"],
            "platform": "Hyundai-Kia J6 / K3",
            "ancap_rating": "5 Stars",
            "summary": "Masterpiece generation featuring the 150kW N Line, and the world-renowned i30 N hot hatch developed by Albert Biermann with 206kW, electronically controlled LSD, and rev-matching manual/N DCT.",
            "engines": [
                {
                    "engine_code": "G4FJ",
                    "name": "Hyundai 1.6L T-GDI Turbo",
                    "displacement_cc": 1591,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 150.0,
                    "power_rpm": "6000",
                    "torque_nm": 265.0,
                    "torque_rpm": "1500-4500",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16-valve Dual CVVT",
                    "notes": "Powers the i30 N Line with multi-link rear suspension."
                },
                {
                    "engine_code": "G4KH",
                    "name": "Hyundai Theta II 2.0L T-GDI (i30 N)",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 206.0,
                    "power_rpm": "6000",
                    "torque_nm": 392.0,
                    "torque_rpm": "2100-4700",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve Dual CVVT Direct Injection",
                    "notes": "Albert Biermann-engineered track beast; 202kW in Series 1, upgraded to 206kW and 392Nm in Series 2."
                }
            ],
            "badges": [
                {
                    "badge_name": "N Line",
                    "years": {"start": 2018, "end": "Present"},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "7-speed dual-clutch (DCT)"],
                    "msrp_aud_min": 29490,
                    "msrp_aud_max": 37500,
                    "fuel_consumption_l_100km": 7.1,
                    "kerb_weight_kg": 1345,
                    "standard_features": ["150kW 1.6L turbo engine", "Independent multi-link rear suspension", "18-inch alloy wheels with Michelin Pilot Sport 4 tyres", "Sports bucket seats with red contrast stitching", "10.25-inch infotainment touchscreen with Apple CarPlay/Android Auto"],
                    "notes": "Australia's top-value warm performance hatchback."
                },
                {
                    "badge_name": "i30 N Performance",
                    "years": {"start": 2018, "end": "Present"},
                    "body_styles": ["5-door Hatch", "Fastback", "Sedan (i30 Sedan N)"],
                    "drivetrain": "FWD with Electronic Limited Slip Differential (e-LSD)",
                    "transmissions": ["6-speed manual with rev matching", "8-speed wet dual-clutch (N DCT)"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 52000,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 1429,
                    "standard_features": ["206kW/392Nm 2.0L Turbo engine", "N Corner Carving Differential (e-LSD)", "Electronically controlled adaptive suspension", "Active variable twin exhaust with overrun crackles", "19-inch forged alloy wheels with Pirelli P-Zero HN tyres", "N Grin Control System with custom drive modes", "Launch control"],
                    "notes": "Critically acclaimed hot hatch sensation."
                }
            ],
            "configurations": [
                {
                    "badge_name": "i30 N Performance",
                    "body_style": "5-door Hatch",
                    "engine_code": "G4KH",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD with e-LSD",
                    "years_start": 2021,
                    "years_end": "Present",
                    "msrp_aud": 44500,
                    "power_kw": 206.0,
                    "torque_nm": 392.0,
                    "fuel_l_100km": 8.5,
                    "towing_braked_kg": 0,
                    "notes": "Series 2 i30 N Hatch manual."
                },
                {
                    "badge_name": "i30 N DCT",
                    "body_style": "5-door Hatch",
                    "engine_code": "G4KH",
                    "transmission": "8-speed wet dual-clutch (N DCT)",
                    "drivetrain": "FWD with e-LSD",
                    "years_start": 2021,
                    "years_end": "Present",
                    "msrp_aud": 47500,
                    "power_kw": 206.0,
                    "torque_nm": 392.0,
                    "fuel_l_100km": 8.5,
                    "towing_braked_kg": 0,
                    "notes": "Series 2 i30 N with N Grin Shift (NGS) overboost."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

STINGER_MODEL = {
    "make_slug": "kia",
    "model_slug": "stinger",
    "name": "Stinger",
    "vehicle_type": "Sports Fastback Liftback",
    "segment": "Large Sports Sedan",
    "years_sold_au": {"start": 2017, "end": "2023"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Kia Stinger arrived in Australia in late 2017 just as Holden and Ford ceased local manufacturing, instantly becoming the spiritual successor to the rear-wheel-drive Falcon and Commodore. Powered by a 272kW twin-turbo V6, it was adopted by Australian police forces as a high-speed pursuit interceptor.",
    "australian_market_notes": "Engineered under Albert Biermann and tuned extensively by Kia Australia's suspension team on regional Australian roads, the Stinger GT won praise for incredible highway overtaking thrust and rear-drive balance. The Queensland Police Service (QPS) and Northern Territory Police selected the 3.3L twin-turbo V6 Stinger as their primary highway patrol vehicles.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "CK",
            "generation_name": "Stinger 1st Generation",
            "years": {"start": 2017, "end": "2023"},
            "body_styles": ["5-door Liftback Fastback"],
            "platform": "Hyundai-Kia M2",
            "ancap_rating": "5 Stars",
            "summary": "Rear-wheel-drive grand tourer featuring the 272kW 3.3L Twin-Turbo Lambda II V6, mechanical limited-slip differential, Brembo brakes, and Australian police highway patrol duty.",
            "engines": [
                {
                    "engine_code": "G4KL",
                    "name": "Kia Theta II 2.0L Turbo",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Twin-Scroll Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 182.0,
                    "power_rpm": "6200",
                    "torque_nm": 353.0,
                    "torque_rpm": "1400-4000",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16-valve Dual CVVT Direct Injection",
                    "notes": "Fitted to 200S and GT-Line models."
                },
                {
                    "engine_code": "G6DP",
                    "name": "Kia Lambda II 3.3L Twin-Turbo V6",
                    "displacement_cc": 3342,
                    "displacement_litres": 3.3,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Twin-Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 272.0,
                    "power_rpm": "6000",
                    "torque_nm": 510.0,
                    "torque_rpm": "1300-4500",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 24-valve Dual CVVT Direct Injection",
                    "notes": "272kW and 510Nm (upgraded to 274kW with factory bi-modal variable exhaust in 2021); 0-100 km/h in 4.9 seconds."
                }
            ],
            "badges": [
                {
                    "badge_name": "330S",
                    "years": {"start": 2017, "end": "2023"},
                    "body_styles": ["5-door Fastback"],
                    "drivetrain": "Rear-Wheel Drive (RWD) with LSD",
                    "transmissions": ["8-speed automatic"],
                    "msrp_aud_min": 48990,
                    "msrp_aud_max": 53500,
                    "fuel_consumption_l_100km": 10.2,
                    "kerb_weight_kg": 1780,
                    "standard_features": ["3.3L Twin-Turbo V6 (272kW)", "Brembo 4-piston front / 2-piston rear performance brakes", "Mechanical Limited Slip Differential (LSD)", "18-inch alloy wheels", "Autonomous Emergency Braking (AEB)", "7-inch touchscreen audio"],
                    "notes": "Budget muscle car; foundation vehicle for Australian police fleets."
                },
                {
                    "badge_name": "GT",
                    "years": {"start": 2017, "end": "2023"},
                    "body_styles": ["5-door Fastback"],
                    "drivetrain": "Rear-Wheel Drive (RWD) with LSD",
                    "transmissions": ["8-speed automatic"],
                    "msrp_aud_min": 59990,
                    "msrp_aud_max": 64990,
                    "fuel_consumption_l_100km": 10.2,
                    "kerb_weight_kg": 1834,
                    "standard_features": ["Electronically Controlled Suspension (ECS)", "Brembo brakes", "Mechanical LSD", "Nappa leather heated and ventilated sports seats", "15-speaker harman/kardon audio", "Head-up display", "19-inch alloy wheels with Michelin Pilot Sport 4 tyres", "Factory active bi-modal variable exhaust"],
                    "notes": "The defining Korean sports sedan in Australia."
                },
                {
                    "badge_name": "Tribute Edition",
                    "years": {"start": 2023, "end": "2023"},
                    "body_styles": ["5-door Fastback"],
                    "drivetrain": "Rear-Wheel Drive (RWD) with LSD",
                    "transmissions": ["8-speed automatic"],
                    "msrp_aud_min": 70390,
                    "msrp_aud_max": 70390,
                    "fuel_consumption_l_100km": 10.2,
                    "kerb_weight_kg": 1834,
                    "standard_features": ["Moonscape matte grey paint option", "Terracotta brown Nappa leather upholstery", "Carbon-finish interior trim", "Numbered door sill plates (#1-1000 worldwide)", "Brembo black brake calipers"],
                    "notes": "Celebrated the farewell of the Stinger; final model run."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GT 3.3L Twin-Turbo V6",
                    "body_style": "5-door Fastback",
                    "engine_code": "G6DP",
                    "transmission": "8-speed automatic",
                    "drivetrain": "RWD with LSD",
                    "years_start": 2017,
                    "years_end": "2023",
                    "msrp_aud": 63290,
                    "power_kw": 274.0,
                    "torque_nm": 510.0,
                    "fuel_l_100km": 10.2,
                    "towing_braked_kg": 1500,
                    "notes": "Stinger GT V6 with factory bi-modal exhaust."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

KOREAN_DEEP_DIVES = [I30_MODEL, STINGER_MODEL]
