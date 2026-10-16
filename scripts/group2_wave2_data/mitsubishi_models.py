"""Wave 2 Mitsubishi deep-dive models: Lancer Evolution, Outlander, 380, Starion & Cordia Turbo."""

EVO_MODEL = {
    "make_slug": "mitsubishi",
    "model_slug": "lancer-evolution",
    "name": "Lancer Evolution & Ralliart",
    "vehicle_type": "Sports Sedan / Hatchback",
    "segment": "Rally Performance / Sports Car",
    "years_sold_au": {"start": 1992, "end": 2015},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mitsubishi Lancer Evolution and Ralliart models represent one of the greatest chapters in modern Australian performance car folklore. Born directly from World Rally Championship battles where Tommi Mäkinen claimed four consecutive WRC drivers' titles, the Evo delivered staggering turbocharged all-wheel-drive grip, Active Yaw Control (AYC), and giant-killing cross-country pace.",
    "australian_market_notes": "Australian enthusiasts first tasted this formula with the 1992-1996 Lancer GSR 4WD (CC). In 2001, Team Mitsubishi Ralliart officially imported 100 numbered examples of the iconic Evo 6.5 Tommi Mäkinen Edition (TME). From the Evo VIII in 2004, Mitsubishi Australia officially retailed Evolution models through selected Ralliart dealerships. The story culminated in the high-tech aluminium 4B11T-powered Evo X and the 226kW Final Edition in 2015.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "CC GSR",
            "generation_name": "Lancer GSR 4WD (The Pre-Evo Blueprint)",
            "years": {"start": 1992, "end": 1996},
            "body_styles": ["4-door Sedan", "5-door Hatchback"],
            "platform": "Mitsubishi CC",
            "ancap_rating": "Untested",
            "summary": "Pioneered the turbocharged all-wheel-drive rally-replica formula in Australia. Powered by the 141kW 1.8L 4G93T DOHC 16-valve intercooled turbo engine with permanent AWD.",
            "engines": [
                {
                    "engine_code": "4G93T",
                    "name": "Mitsubishi 4G93T 1.8L DOHC Turbo",
                    "displacement_cc": 1834,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled (TD04)",
                    "fuel_type": "Petrol",
                    "power_kw": 141.0,
                    "power_rpm": "6000",
                    "torque_nm": 249.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Top-mount intercooler with twin bonnet vents."
                }
            ],
            "badges": [
                {
                    "badge_name": "GSR 4WD",
                    "years": {"start": 1992, "end": 1996},
                    "body_styles": ["4-door Sedan", "5-door Hatch"],
                    "drivetrain": "Full-Time AWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 29990,
                    "msrp_aud_max": 33500,
                    "fuel_consumption_l_100km": 9.8,
                    "kerb_weight_kg": 1210,
                    "standard_features": ["Full-time AWD with viscous centre and rear LSD", "Recaro front bucket seats", "14-inch alloy wheels", "Four-wheel disc brakes", "Bonnet vents"],
                    "notes": "Predecessor to Australian Evo culture."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Lancer GSR 4WD Sedan",
                    "body_style": "4-door Sedan",
                    "engine_code": "4G93T",
                    "transmission": "5-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 1992,
                    "years_end": 1996,
                    "msrp_aud": 29990,
                    "power_kw": 141.0,
                    "torque_nm": 249.0,
                    "fuel_l_100km": 9.8,
                    "towing_braked_kg": 1000,
                    "notes": "Affordable 141kW AWD performance weapon."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "CP9A",
            "generation_name": "Evolution VI & Tommi Makinen Edition (TME)",
            "years": {"start": 1999, "end": 2001},
            "body_styles": ["4-door Sedan"],
            "platform": "Mitsubishi CP9A",
            "ancap_rating": "Untested",
            "summary": "100 official Australian-delivered TME models imported by Ralliart Australia. 206kW 4G63T with titanium turbine wheel, lowered tarmac suspension, and Active Yaw Control.",
            "engines": [
                {
                    "engine_code": "4G63T-TME",
                    "name": "Mitsubishi 4G63T 2.0L Turbo (Tommi Makinen)",
                    "displacement_cc": 1997,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Twin-Scroll Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 206.0,
                    "power_rpm": "6500",
                    "torque_nm": 373.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Titanium-aluminide turbine wheel providing instant spool."
                }
            ],
            "badges": [
                {
                    "badge_name": "Evo 6.5 Tommi Makinen Edition (TME)",
                    "years": {"start": 2000, "end": 2001},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "AWD with Active Yaw Control",
                    "transmissions": ["5-speed close-ratio manual"],
                    "msrp_aud_min": 79990,
                    "msrp_aud_max": 79990,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1360,
                    "standard_features": ["100 Australian-delivered numbered cars", "Enkei 17-inch WRC rally replica wheels", "Brembo 4-piston brakes", "Recaro seats with red Tommi Makinen embroidery", "Momo steering wheel"],
                    "notes": "Holy grail Australian rally homologation hero."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Lancer Evolution VI TME",
                    "body_style": "4-door Sedan",
                    "engine_code": "4G63T-TME",
                    "transmission": "5-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 2000,
                    "years_end": 2001,
                    "msrp_aud": 79990,
                    "power_kw": 206.0,
                    "torque_nm": 373.0,
                    "fuel_l_100km": 11.2,
                    "towing_braked_kg": 0,
                    "notes": "0-100 km/h in 4.8 seconds; peak WRC road car."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "CT9A",
            "generation_name": "Evolution VIII & IX",
            "years": {"start": 2004, "end": 2007},
            "body_styles": ["4-door Sedan"],
            "platform": "Mitsubishi CT9A",
            "ancap_rating": "Untested",
            "summary": "First full-scale official Australian dealer distribution. Super Active Yaw Control (S-AYC), Active Centre Differential (ACD), 6-speed manual, and MIVEC variable valve timing in Evo IX.",
            "engines": [
                {
                    "engine_code": "4G63T-MIVEC",
                    "name": "Mitsubishi 4G63T 2.0L MIVEC Turbo",
                    "displacement_cc": 1997,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Twin-Scroll Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 206.0,
                    "power_rpm": "6500",
                    "torque_nm": 400.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "DOHC 16-valve MIVEC",
                    "notes": "MIVEC variable intake valve timing in Evo IX with 400Nm of torque."
                }
            ],
            "badges": [
                {
                    "badge_name": "Evo VIII",
                    "years": {"start": 2004, "end": 2005},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "AWD with ACD & Super AYC",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 61990,
                    "msrp_aud_max": 61990,
                    "fuel_consumption_l_100km": 10.9,
                    "kerb_weight_kg": 1410,
                    "standard_features": ["ACD & Super AYC", "Brembo 4-pot brakes", "Carbon fiber rear wing", "17-inch Enkei alloys", "Recaro bucket seats"],
                    "notes": "First officially imported mass production Evo in Australia."
                },
                {
                    "badge_name": "Evo IX",
                    "years": {"start": 2005, "end": 2007},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "AWD with ACD & Super AYC",
                    "transmissions": ["6-speed manual"],
                    "msrp_aud_min": 56789,
                    "msrp_aud_max": 65990,
                    "fuel_consumption_l_100km": 10.7,
                    "kerb_weight_kg": 1410,
                    "standard_features": ["MIVEC engine", "BBS forged alloy wheels", "Bilstein inverted shock absorbers", "Aluminium roof and bonnet", "Xenon headlamps"],
                    "notes": "Peak of the cast-iron 4G63 engine era."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Lancer Evolution IX 6-speed",
                    "body_style": "4-door Sedan",
                    "engine_code": "4G63T-MIVEC",
                    "transmission": "6-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 2005,
                    "years_end": 2007,
                    "msrp_aud": 56789,
                    "power_kw": 206.0,
                    "torque_nm": 400.0,
                    "fuel_l_100km": 10.7,
                    "towing_braked_kg": 0,
                    "notes": "0-100 km/h in 4.7 seconds with 400Nm torque."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "CZ4A",
            "generation_name": "Evolution X & Ralliart",
            "years": {"start": 2008, "end": 2015},
            "body_styles": ["4-door Sedan", "5-door Sportback (Ralliart)"],
            "platform": "Mitsubishi GS platform",
            "ancap_rating": "5 stars",
            "summary": "All-aluminium 4B11T turbocharged engine, Super All-Wheel Control (S-AWC), 6-speed Twin Clutch SST transmission or 5-speed manual, alongside the accessible Lancer Ralliart AWD.",
            "engines": [
                {
                    "engine_code": "4B11T-Evo",
                    "name": "Mitsubishi 4B11T 2.0L MIVEC Turbo",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Twin-Scroll Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 217.0,
                    "power_rpm": "6500",
                    "torque_nm": 366.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "DOHC 16-valve MIVEC",
                    "notes": "Die-cast aluminium cylinder block; Final Edition tuned to 226kW/414Nm."
                },
                {
                    "engine_code": "4B11T-Ralliart",
                    "name": "Mitsubishi 4B11T 2.0L Turbo (Ralliart)",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Single-Scroll Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 177.0,
                    "power_rpm": "6000",
                    "torque_nm": 343.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "DOHC 16-valve MIVEC",
                    "notes": "Fitted to Lancer Ralliart sedan and Sportback hatch."
                }
            ],
            "badges": [
                {
                    "badge_name": "Lancer Ralliart",
                    "years": {"start": 2008, "end": 2015},
                    "body_styles": ["Sedan", "Sportback Hatch"],
                    "drivetrain": "AWD with ACD & mechanical rear LSD",
                    "transmissions": ["6-speed TC-SST dual-clutch"],
                    "msrp_aud_min": 42490,
                    "msrp_aud_max": 44490,
                    "fuel_consumption_l_100km": 10.2,
                    "kerb_weight_kg": 1555,
                    "standard_features": ["177kW turbo engine", "Aluminium vented bonnet", "Dual exhaust", "18-inch alloys", "Automatic paddle-shift dual clutch"],
                    "notes": "WRX fighter with Evo DNA."
                },
                {
                    "badge_name": "Evo X GSR & MR",
                    "years": {"start": 2008, "end": 2015},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "S-AWC (Super All-Wheel Control)",
                    "transmissions": ["5-speed manual", "6-speed TC-SST dual clutch"],
                    "msrp_aud_min": 59490,
                    "msrp_aud_max": 74390,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1565,
                    "standard_features": ["S-AWC with active center diff, active yaw control, active stability control", "Brembo brakes", "BBS wheels (MR)", "Bilstein dampers & Eibach springs (MR)", "Recaro leather seats"],
                    "notes": "Advanced AWD handling technology."
                },
                {
                    "badge_name": "Evo X Final Edition",
                    "years": {"start": 2015, "end": 2015},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "S-AWC",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 53700,
                    "msrp_aud_max": 53700,
                    "fuel_consumption_l_100km": 10.7,
                    "kerb_weight_kg": 1545,
                    "standard_features": ["226kW upgraded engine", "Numbered plaque (150 Australian cars)", "BBS satin platinum 18-inch wheels", "Black painted roof", "Red stitched Recaro sports seats"],
                    "notes": "Final 150 production units for Australia concluding 23 years of Evo history."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Lancer Evolution X MR",
                    "body_style": "4-door Sedan",
                    "engine_code": "4B11T-Evo",
                    "transmission": "6-speed TC-SST dual-clutch",
                    "drivetrain": "AWD",
                    "years_start": 2008,
                    "years_end": 2015,
                    "msrp_aud": 71690,
                    "power_kw": 217.0,
                    "torque_nm": 366.0,
                    "fuel_l_100km": 10.5,
                    "towing_braked_kg": 0,
                    "notes": "S-AWC all-wheel drive with BBS wheels and Bilstein suspension."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

OUTLANDER_MODEL = {
    "make_slug": "mitsubishi",
    "model_slug": "outlander",
    "name": "Outlander",
    "vehicle_type": "Medium SUV",
    "segment": "Medium SUV",
    "years_sold_au": {"start": 2003, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mitsubishi Outlander is one of Australia's most enduring family SUVs and a pioneer of plug-in hybrid electric vehicle (PHEV) technology. Known for offering 7-seat practicality in a medium SUV footprint, robust all-wheel drive systems derived from the Lancer Evolution, and exceptional value, the Outlander is a mainstay on Australian roads.",
    "australian_market_notes": "First introduced in 2003 as the Airtrek-based ZE, the second-generation ZG introduced a split-folding tailgate and punchy 3.0L V6. In 2014, Mitsubishi pioneered the Australian mass-market plug-in hybrid landscape with the Outlander PHEV, providing EV commuting with long-range petrol backup. The fourth-generation ZM, built on the CMF-CD platform with Super All-Wheel Control (S-AWC), continues as one of Australia's top-selling SUVs.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "ZE/ZF",
            "generation_name": "Outlander 1st Generation",
            "years": {"start": 2003, "end": 2006},
            "body_styles": ["5-door SUV"],
            "platform": "Mitsubishi CU",
            "ancap_rating": "4 stars",
            "summary": "Original Airtrek crossover styling with full-time AWD and 2.4L MIVEC engine, combining raised ride height with car-like unibody handling.",
            "engines": [
                {
                    "engine_code": "4G69",
                    "name": "Mitsubishi 4G69 2.4L MIVEC",
                    "displacement_cc": 2378,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 118.0,
                    "power_rpm": "5750",
                    "torque_nm": 220.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "SOHC 16-valve MIVEC",
                    "notes": "Smooth four-cylinder with variable valve lift."
                }
            ],
            "badges": [
                {
                    "badge_name": "LS / XLS",
                    "years": {"start": 2003, "end": 2006},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "Full-Time AWD",
                    "transmissions": ["4-speed INVECS-II automatic"],
                    "msrp_aud_min": 31990,
                    "msrp_aud_max": 38990,
                    "fuel_consumption_l_100km": 10.4,
                    "kerb_weight_kg": 1540,
                    "standard_features": ["Full-time AWD with viscous coupling", "16-inch alloy wheels", "Dual front airbags", "ABS with EBD", "Roof rails"],
                    "notes": "First generation crossover."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Outlander XLS AWD",
                    "body_style": "5-door SUV",
                    "engine_code": "4G69",
                    "transmission": "4-speed automatic",
                    "drivetrain": "AWD",
                    "years_start": 2003,
                    "years_end": 2006,
                    "msrp_aud": 37990,
                    "power_kw": 118.0,
                    "torque_nm": 220.0,
                    "fuel_l_100km": 10.4,
                    "towing_braked_kg": 1500,
                    "notes": "Original first-gen Australian specification."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "ZG/ZH",
            "generation_name": "Outlander 2nd Generation",
            "years": {"start": 2006, "end": 2012},
            "body_styles": ["5-door SUV"],
            "platform": "Mitsubishi GS platform",
            "ancap_rating": "5 stars (facelift)",
            "summary": "Shared platform with Lancer. Introduced 7-seat capability, split 'flap-fold' 200kg-rated tailgate, and a powerful 3.0L MIVEC V6 with paddle-shift 6-speed auto.",
            "engines": [
                {
                    "engine_code": "4B12",
                    "name": "Mitsubishi 4B12 2.4L DOHC MIVEC",
                    "displacement_cc": 2359,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 125.0,
                    "power_rpm": "6000",
                    "torque_nm": 226.0,
                    "torque_rpm": "4100",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16-valve MIVEC",
                    "notes": "Aluminium engine block paired with CVT."
                },
                {
                    "engine_code": "6B31",
                    "name": "Mitsubishi 6B31 3.0L SOHC MIVEC V6",
                    "displacement_cc": 2998,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 169.0,
                    "power_rpm": "6250",
                    "torque_nm": 291.0,
                    "torque_rpm": "3750",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "SOHC 24-valve MIVEC",
                    "notes": "High performance V6 paired with 6-speed torque-converter automatic."
                }
            ],
            "badges": [
                {
                    "badge_name": "LS",
                    "years": {"start": 2006, "end": 2012},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["5-speed manual", "CVT automatic"],
                    "msrp_aud_min": 31990,
                    "msrp_aud_max": 37500,
                    "fuel_consumption_l_100km": 9.3,
                    "kerb_weight_kg": 1530,
                    "standard_features": ["Flap-fold tailgate", "Air conditioning", "Cruise control", "Stability control", "Hill start assist"],
                    "notes": "5-seater entry trim."
                },
                {
                    "badge_name": "VR / VR-X V6",
                    "years": {"start": 2006, "end": 2012},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "All-Wheel Control (AWC)",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 43990,
                    "msrp_aud_max": 51990,
                    "fuel_consumption_l_100km": 10.4,
                    "kerb_weight_kg": 1720,
                    "standard_features": ["3.0L V6 169kW engine", "7 seats (underfloor stowable 3rd row)", "18-inch alloys", "Paddle shifters", "Rockford Fosgate 650W sound system with subwoofer", "Sunroof"],
                    "notes": "Popular V6 family hauler."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Outlander VR-X 3.0 V6 AWD",
                    "body_style": "5-door SUV",
                    "engine_code": "6B31",
                    "transmission": "6-speed automatic",
                    "drivetrain": "AWD",
                    "years_start": 2007,
                    "years_end": 2012,
                    "msrp_aud": 47990,
                    "power_kw": 169.0,
                    "torque_nm": 291.0,
                    "fuel_l_100km": 10.4,
                    "towing_braked_kg": 1600,
                    "notes": "7 seats with 3.0L V6 and Rockford Fosgate premium audio."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "ZJ/ZK/ZL",
            "generation_name": "Outlander 3rd Generation & PHEV",
            "years": {"start": 2012, "end": 2021},
            "body_styles": ["5-door SUV"],
            "platform": "Mitsubishi GS/GF platform",
            "ancap_rating": "5 stars",
            "summary": "Pioneered mass-market plug-in hybrid motoring in Australia in 2014. Combines 7 seats, lightweight body, 5-star safety, and twin electric motor PHEV AWD.",
            "engines": [
                {
                    "engine_code": "4J12",
                    "name": "Mitsubishi 4J12 2.4L MIVEC",
                    "displacement_cc": 2359,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 124.0,
                    "power_rpm": "6000",
                    "torque_nm": 220.0,
                    "torque_rpm": "4200",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "SOHC 16-valve MIVEC",
                    "notes": "Standard petrol engine in AWD models."
                },
                {
                    "engine_code": "4B11-PHEV",
                    "name": "Mitsubishi 4B11 2.0L + Twin Electric Motors (PHEV)",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4 + Dual Electric Motors",
                    "aspiration": "Naturally Aspirated + EV",
                    "fuel_type": "Plug-in Hybrid Petrol",
                    "power_kw": 147.0,
                    "power_rpm": "4500",
                    "torque_nm": 332.0,
                    "torque_rpm": "4500",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "12kWh lithium-ion battery delivering 52km of pure EV range and 1.9L/100km ADR rating."
                }
            ],
            "badges": [
                {
                    "badge_name": "ES / LS",
                    "years": {"start": 2012, "end": 2021},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["5-speed manual", "CVT automatic"],
                    "msrp_aud_min": 28990,
                    "msrp_aud_max": 38990,
                    "fuel_consumption_l_100km": 7.2,
                    "kerb_weight_kg": 1495,
                    "standard_features": ["7 seats (from LS)", "7 airbags", "Touchscreen audio with Apple CarPlay", "Dual-zone climate control", "Rear camera"],
                    "notes": "High value family workhorse."
                },
                {
                    "badge_name": "PHEV (Plug-in Hybrid)",
                    "years": {"start": 2014, "end": 2021},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "Super-All Wheel Control (S-AWC)",
                    "transmissions": ["Single-speed reduction transaxle"],
                    "msrp_aud_min": 47490,
                    "msrp_aud_max": 56490,
                    "fuel_consumption_l_100km": 1.9,
                    "kerb_weight_kg": 1810,
                    "standard_features": ["Twin 60kW electric motors (front and rear)", "CHAdeMO DC rapid charging port", "Regenerative braking paddles", "EV drive modes"],
                    "notes": "Australia's top-selling plug-in hybrid SUV for seven consecutive years."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Outlander PHEV Exceed",
                    "body_style": "5-door SUV",
                    "engine_code": "4B11-PHEV",
                    "transmission": "Single-speed reduction",
                    "drivetrain": "AWD",
                    "years_start": 2014,
                    "years_end": 2021,
                    "msrp_aud": 56490,
                    "power_kw": 147.0,
                    "torque_nm": 332.0,
                    "fuel_l_100km": 1.9,
                    "towing_braked_kg": 1500,
                    "notes": "Trailblazing plug-in hybrid in Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "ZM",
            "generation_name": "Outlander 4th Generation & Next-Gen PHEV",
            "years": {"start": 2021, "end": "Present"},
            "body_styles": ["5-door SUV"],
            "platform": "Renault-Nissan-Mitsubishi CMF-CD",
            "ancap_rating": "5 stars",
            "summary": "Built on the CMF-CD platform with bold Dynamic Shield styling, standard 7 seats, upgraded 20kWh PHEV with 84km EV range, and Super-All Wheel Control (S-AWC).",
            "engines": [
                {
                    "engine_code": "PR25DD",
                    "name": "Nissan/Mitsubishi PR25DD 2.5L Direct Injection",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 135.0,
                    "power_rpm": "6000",
                    "torque_nm": 245.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "12.0:1",
                    "valvetrain": "DOHC 16-valve direct injection",
                    "notes": "Smooth direct injection engine paired with 8-step CVT."
                },
                {
                    "engine_code": "4B12-PHEV2",
                    "name": "Mitsubishi 4B12 2.4L + Twin High-Output Motors (PHEV)",
                    "displacement_cc": 2360,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4 + Dual Electric Motors",
                    "aspiration": "Naturally Aspirated + EV",
                    "fuel_type": "Plug-in Hybrid Petrol",
                    "power_kw": 185.0,
                    "power_rpm": "6000",
                    "torque_nm": 450.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "11.7:1",
                    "valvetrain": "DOHC 16-valve MIVEC",
                    "notes": "Combined 185kW / 450Nm with 20kWh battery delivering 84km pure EV range."
                }
            ],
            "badges": [
                {
                    "badge_name": "ES / LS",
                    "years": {"start": 2021, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["CVT automatic"],
                    "msrp_aud_min": 37240,
                    "msrp_aud_max": 44490,
                    "fuel_consumption_l_100km": 7.7,
                    "kerb_weight_kg": 1640,
                    "standard_features": ["7 seats (from LS)", "18-inch alloys", "Wireless Apple CarPlay", "Emergency lane assist", "Adaptive cruise control"],
                    "notes": "Core family transport."
                },
                {
                    "badge_name": "Exceed / Exceed Tourer PHEV",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "Super-All Wheel Control (S-AWC)",
                    "transmissions": ["Single-speed automatic transaxle"],
                    "msrp_aud_min": 68490,
                    "msrp_aud_max": 73790,
                    "fuel_consumption_l_100km": 1.5,
                    "kerb_weight_kg": 2145,
                    "standard_features": ["20-inch two-tone alloy wheels", "Semi-aniline leather massage front seats", "12.3-inch digital instrument cluster", "Bose 10-speaker audio", "V2L/V2H vehicle-to-load bidirectional charging"],
                    "notes": "Equipped with bidirectional vehicle-to-grid power export."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Outlander Exceed Tourer PHEV AWD",
                    "body_style": "5-door SUV",
                    "engine_code": "4B12-PHEV2",
                    "transmission": "Single-speed reduction",
                    "drivetrain": "AWD",
                    "years_start": 2022,
                    "years_end": "Present",
                    "msrp_aud": 73790,
                    "power_kw": 185.0,
                    "torque_nm": 450.0,
                    "fuel_l_100km": 1.5,
                    "towing_braked_kg": 1600,
                    "notes": "185kW / 450Nm dual electric motor PHEV with 84km EV range."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

MITSUBISHI_380_MODEL = {
    "make_slug": "mitsubishi",
    "model_slug": "380",
    "name": "380",
    "vehicle_type": "Large Sedan",
    "segment": "Large Car",
    "years_sold_au": {"start": 2005, "end": 2008},
    "locally_built": True,
    "assembly_plants_au": ["Tonsley Park, South Australia (Mitsubishi Motors Australia Limited)"],
    "overview": "The Mitsubishi 380 was the final passenger car designed, engineered, and manufactured by Mitsubishi Motors Australia at its Tonsley Park plant in Adelaide. Backed by a $600-million investment and over 2.4 million kilometres of Australian testing, the 380 was powered by a punchy 3.8-litre 6G75 V6 with 175kW and 343Nm, praised by critics for its exceptionally stiff body structure and European-grade chassis dynamics.",
    "australian_market_notes": "Launched in October 2005 to replace the Magna and Verada, the 380 went toe-to-toe with the Holden Commodore and Ford Falcon. While acclaimed by Wheels and Motor for chassis rigidity and refined ride quality, intense fleet competition and soaring fuel prices hampered sales volumes. Series II and III introduced revised equipment and competitive pricing. The final Mitsubishi 380 rolled off the Tonsley Park production line on 27 March 2008, bringing to an end 43 years of vehicle assembly at the Adelaide factory.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "DB Series I",
            "generation_name": "380 Series I",
            "years": {"start": 2005, "end": 2006},
            "body_styles": ["4-door Sedan"],
            "platform": "Mitsubishi PS41",
            "ancap_rating": "4 stars",
            "summary": "The culmination of a $600M investment at Tonsley Park. Powered exclusively by the 3.8L 6G75 SOHC 24-valve V6 producing 175kW and 343Nm, with 5-speed manual or 5-speed INVECS-II Sports Mode automatic.",
            "engines": [
                {
                    "engine_code": "6G75",
                    "name": "Mitsubishi 6G75 3.8L SOHC 24V V6",
                    "displacement_cc": 3828,
                    "displacement_litres": 3.8,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 175.0,
                    "power_rpm": "5250",
                    "torque_nm": 343.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "SOHC 24-valve",
                    "notes": "South Australian assembled 3.8L V6 with broad torque spread (over 300Nm from 1,500rpm)."
                }
            ],
            "badges": [
                {
                    "badge_name": "380 (Base) / LS / LX",
                    "years": {"start": 2005, "end": 2006},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "5-speed INVECS-II automatic"],
                    "msrp_aud_min": 34490,
                    "msrp_aud_max": 41990,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1625,
                    "standard_features": ["Four airbags", "ABS with EBD", "Climate control", "Trip computer", "Cruise control", "Power driver seat"],
                    "notes": "Adelaide-built large sedan."
                },
                {
                    "badge_name": "VRX",
                    "years": {"start": 2005, "end": 2006},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "5-speed INVECS-II automatic"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 41990,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1660,
                    "standard_features": ["Sports suspension tuning", "17-inch 6-spoke alloy wheels", "Sports body kit with rear boot spoiler", "Sports mesh front grille", "Sports cloth bucket seats"],
                    "notes": "Rival to Falcon XR6 and Commodore SV6."
                },
                {
                    "badge_name": "GT",
                    "years": {"start": 2005, "end": 2006},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed INVECS-II automatic"],
                    "msrp_aud_min": 47990,
                    "msrp_aud_max": 47990,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1690,
                    "standard_features": ["Plush leather upholstery", "Sunroof", "Electrochromic rear-view mirror", "17-inch luxury alloys", "8-speaker premium audio with 6-disc in-dash CD"],
                    "notes": "Luxury flagship replacing the Verada."
                }
            ],
            "configurations": [
                {
                    "badge_name": "380 VRX Sports Auto",
                    "body_style": "4-door Sedan",
                    "engine_code": "6G75",
                    "transmission": "5-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 2005,
                    "years_end": 2006,
                    "msrp_aud": 41990,
                    "power_kw": 175.0,
                    "torque_nm": 343.0,
                    "fuel_l_100km": 10.8,
                    "towing_braked_kg": 1600,
                    "notes": "Tonsley Park built sports sedan; 0-100 km/h in 7.6 seconds."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "DB Series II",
            "generation_name": "380 Series II",
            "years": {"start": 2006, "end": 2007},
            "body_styles": ["4-door Sedan"],
            "platform": "Mitsubishi PS41",
            "ancap_rating": "4 stars",
            "summary": "Major price repositioning to boost showroom traction, introduction of the popular mid-spec 380 SX, Euro III emissions compliance, and factory dual-fuel LPG availability.",
            "engines": [
                {
                    "engine_code": "6G75-S2",
                    "name": "Mitsubishi 6G75 3.8L V6 (Euro III)",
                    "displacement_cc": 3828,
                    "displacement_litres": 3.8,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 175.0,
                    "power_rpm": "5250",
                    "torque_nm": 343.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "SOHC 24-valve",
                    "notes": "Euro III compliant calibration."
                }
            ],
            "badges": [
                {
                    "badge_name": "SX",
                    "years": {"start": 2006, "end": 2007},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed automatic"],
                    "msrp_aud_min": 32990,
                    "msrp_aud_max": 34990,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1640,
                    "standard_features": ["17-inch alloy wheels", "Sports front bumper insert", "Traction control standard", "Cruise control", "Four airbags"],
                    "notes": "Added to offer VRX looks at an attractive price."
                },
                {
                    "badge_name": "VRX",
                    "years": {"start": 2006, "end": 2007},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "5-speed automatic"],
                    "msrp_aud_min": 36990,
                    "msrp_aud_max": 38990,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1660,
                    "standard_features": ["Sports suspension", "17-inch sports alloys", "Lip spoiler", "Sports seats", "Silver dash accents"],
                    "notes": "Aggressive $3,000 price reduction."
                }
            ],
            "configurations": [
                {
                    "badge_name": "380 SX Auto",
                    "body_style": "4-door Sedan",
                    "engine_code": "6G75-S2",
                    "transmission": "5-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 2006,
                    "years_end": 2007,
                    "msrp_aud": 34990,
                    "power_kw": 175.0,
                    "torque_nm": 343.0,
                    "fuel_l_100km": 10.8,
                    "towing_braked_kg": 1600,
                    "notes": "South Australian built large sedan."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "DB Series III",
            "generation_name": "380 Series III (Final Adelaide Production)",
            "years": {"start": 2007, "end": 2008},
            "body_styles": ["4-door Sedan"],
            "platform": "Mitsubishi PS41",
            "ancap_rating": "4 stars",
            "summary": "Final model year of Australian Mitsubishi manufacturing. Featured standard alloy wheels and traction control across all models, subtle exterior styling revisions, and the limited Platinum Edition.",
            "engines": [
                {
                    "engine_code": "6G75-S3",
                    "name": "Mitsubishi 6G75 3.8L V6",
                    "displacement_cc": 3828,
                    "displacement_litres": 3.8,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 175.0,
                    "power_rpm": "5250",
                    "torque_nm": 343.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "SOHC 24-valve",
                    "notes": "Final engine manufactured at the Lonsdale engine plant in Adelaide."
                }
            ],
            "badges": [
                {
                    "badge_name": "ES / SX / VRX / Platinum",
                    "years": {"start": 2007, "end": 2008},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "5-speed automatic"],
                    "msrp_aud_min": 29990,
                    "msrp_aud_max": 38990,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1645,
                    "standard_features": ["Standard 16 or 17-inch alloys", "Traction control standard across range", "Revised front air dam", "Leather seats (Platinum)", "Sunroof (Platinum)"],
                    "notes": "Final production vehicle produced on 27 March 2008."
                }
            ],
            "configurations": [
                {
                    "badge_name": "380 Series III VRX",
                    "body_style": "4-door Sedan",
                    "engine_code": "6G75-S3",
                    "transmission": "5-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 2007,
                    "years_end": 2008,
                    "msrp_aud": 36990,
                    "power_kw": 175.0,
                    "torque_nm": 343.0,
                    "fuel_l_100km": 10.8,
                    "towing_braked_kg": 1600,
                    "notes": "The last Mitsubishi car ever manufactured in Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

STARION_CORDIA_MODEL = {
    "make_slug": "mitsubishi",
    "model_slug": "starion-cordia",
    "name": "Starion & Cordia Turbo",
    "vehicle_type": "Sports Coupe / Liftback",
    "segment": "Sports Coupe",
    "years_sold_au": {"start": 1982, "end": 1989},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mitsubishi Starion Turbo and Cordia GSR Turbo were the trailblazers of Japanese factory turbocharging in 1980s Australia. From the front-wheel drive Cordia GSR with its mind-bending 'Super Shift' 4x2 twin-stick dual-range transmission to the widebody, rear-wheel drive Starion Turbo that battled Australian Touring Cars in Group E and Group A, these coupes created Australia's turbo street-racing legend.",
    "australian_market_notes": "Released in 1982 (Starion) and 1983 (Cordia), Mitsubishi brought boost to Australian showrooms years before it became mainstream. The lightweight Cordia GSR Turbo with digital instrumentation became a 1980s street-racer folklore hero, while the Starion was famously campaigned by rally ace Colin Bond in the Australian Production Car Championship and Bathurst 1000 with factory Ralliart backing.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "AA/AB/AC",
            "generation_name": "Cordia GSR Turbo",
            "years": {"start": 1983, "end": 1989},
            "body_styles": ["3-door Hatchback Coupe"],
            "platform": "Mitsubishi Cordia",
            "ancap_rating": "Untested",
            "summary": "1980s cult icon. AA series (1.6L 4G32T Turbo 75kW with 4x2 Super Shift twin-stick transmission), upgraded in AB and AC series to 1.8L 4G62T Turbo (110kW/210Nm) and digital instrument cluster.",
            "engines": [
                {
                    "engine_code": "4G32T",
                    "name": "Mitsubishi 4G32T 1.6L Saturn Turbo",
                    "displacement_cc": 1597,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged (TC05)",
                    "fuel_type": "Petrol",
                    "power_kw": 75.0,
                    "power_rpm": "5500",
                    "torque_nm": 147.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Fitted to early AA Cordia GSR with carburetted turbo setup."
                },
                {
                    "engine_code": "4G62T",
                    "name": "Mitsubishi 4G62T 1.8L Sirius Turbo (ECI)",
                    "displacement_cc": 1795,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged (TC06)",
                    "fuel_type": "Petrol",
                    "power_kw": 110.0,
                    "power_rpm": "5800",
                    "torque_nm": 210.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "8.2:1",
                    "valvetrain": "SOHC 8-valve ECI",
                    "notes": "Electronically Controlled Injection delivering blisteringly quick acceleration."
                }
            ],
            "badges": [
                {
                    "badge_name": "Cordia GSR Turbo (AA)",
                    "years": {"start": 1983, "end": 1984},
                    "body_styles": ["3-door Hatchback Coupe"],
                    "drivetrain": "FWD",
                    "transmissions": ["4x2 Super Shift dual-range manual (8 forward ratios)"],
                    "msrp_aud_min": 13990,
                    "msrp_aud_max": 14990,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 990,
                    "standard_features": ["Twin-stick Super Shift transmission (Economy & Power modes)", "Bonnet scoop", "Turbo boost gauge", "Checkered sports bucket seats", "14-inch steel wheels"],
                    "notes": "Lightweight sub-tonne turbo pioneer."
                },
                {
                    "badge_name": "Cordia GSR Turbo (AB / AC)",
                    "years": {"start": 1984, "end": 1989},
                    "body_styles": ["3-door Hatchback Coupe"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 17990,
                    "msrp_aud_max": 22500,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 1045,
                    "standard_features": ["110kW 1.8L turbo engine", "Digital electronic instrument cluster with bar-graph boost gauge", "14-inch alloy wheels", "Rear spoiler", "Four-wheel disc brakes"],
                    "notes": "Street-racing legend in Australian enthusiast circles."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Cordia GSR Turbo 1.8",
                    "body_style": "3-door Hatchback Coupe",
                    "engine_code": "4G62T",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1985,
                    "years_end": 1989,
                    "msrp_aud": 18990,
                    "power_kw": 110.0,
                    "torque_nm": 210.0,
                    "fuel_l_100km": 9.5,
                    "towing_braked_kg": 800,
                    "notes": "0-100 km/h in under 8 seconds; 1980s boost legend."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "JA/JB/JD",
            "generation_name": "Starion Turbo",
            "years": {"start": 1982, "end": 1989},
            "body_styles": ["2-door Coupe"],
            "platform": "Mitsubishi Starion",
            "ancap_rating": "Untested",
            "summary": "Rear-wheel drive grand touring sports coupe. JA series (2.0L 4G63T Sirius Turbo 125kW), JB (unleaded), and final widebody JD with flared guards, 132kW intercooled engine, and limited-slip differential.",
            "engines": [
                {
                    "engine_code": "4G63T-Starion",
                    "name": "Mitsubishi 4G63T 2.0L Sirius Turbo",
                    "displacement_cc": 1997,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged (TC06)",
                    "fuel_type": "Petrol",
                    "power_kw": 125.0,
                    "power_rpm": "5500",
                    "torque_nm": 245.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "7.6:1",
                    "valvetrain": "SOHC 8-valve ECI",
                    "notes": "Lead petrol JA series engine."
                },
                {
                    "engine_code": "4G63T-JD",
                    "name": "Mitsubishi 4G63T 2.0L Intercooled Turbo (JD)",
                    "displacement_cc": 1997,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled (TC05-12A)",
                    "fuel_type": "Unleaded Petrol",
                    "power_kw": 132.0,
                    "power_rpm": "5500",
                    "torque_nm": 245.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "8.0:1",
                    "valvetrain": "SOHC 8-valve ECI",
                    "notes": "Intercooled widebody specification."
                }
            ],
            "badges": [
                {
                    "badge_name": "Starion Turbo (JA / JB)",
                    "years": {"start": 1982, "end": 1986},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 21990,
                    "msrp_aud_max": 25990,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1260,
                    "standard_features": ["Pop-up headlights", "Limited slip differential", "Four-wheel independent suspension", "Power windows", "15-inch alloy wheels"],
                    "notes": "Narrow-body sports GT."
                },
                {
                    "badge_name": "Starion Turbo Widebody (JD)",
                    "years": {"start": 1987, "end": 1989},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 34990,
                    "msrp_aud_max": 39990,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1340,
                    "standard_features": ["Blistered factory widebody guards", "Front-mount intercooler", "16-inch 5-spoke alloys", "Leather seats", "Air conditioning", "Cruise control"],
                    "notes": "Extremely desirable widebody collector car."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Starion Turbo Widebody JD",
                    "body_style": "2-door Coupe",
                    "engine_code": "4G63T-JD",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1987,
                    "years_end": 1989,
                    "msrp_aud": 36990,
                    "power_kw": 132.0,
                    "torque_nm": 245.0,
                    "fuel_l_100km": 10.8,
                    "towing_braked_kg": 1000,
                    "notes": "Widebody rear-drive turbo icon."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}
