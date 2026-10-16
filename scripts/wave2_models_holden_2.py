"""
Wave 2 Deep-Dive Model Data: Holden Modern Volume Lines (Part 2)
Models:
5. Astra
6. Barina
7. Cruze
8. Rodeo
"""
from typing import Any, Dict

MODEL_ASTRA: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "astra",
    "name": "Holden Astra",
    "vehicle_type": "Hatchback / Sedan / Wagon / Coupe / Convertible",
    "segment": "Small",
    "years_sold_au": {"start": 1984, "end": 2020},
    "locally_built": True,
    "assembly_plants_au": [
        "Clayton, Victoria (Nissan AMI JV, LB/LC/LD)",
        "Elizabeth, South Australia (LD body panels)",
        "Antwerp, Belgium (Opel, TS/AH)",
        "Bochum, Germany (Opel, AH)",
        "Gliwice, Poland (Opel, AH/BK)",
        "Ellesmere Port, United Kingdom (Vauxhall/Opel, BK)"
    ],
    "overview": "Spanning 36 years across seven generations, the Holden Astra was Holden's frontline small car. Launched in August 1984 as the LB/LC Astra, it originated as a badge-engineered Nissan Pulsar assembled in Clayton, Victoria. Under the Button Car Plan, the 1987 LD Astra combined Nissan body engineering with Holden's locally manufactured 1.6L and 1.8L Family II engines. In 1996, the Astra was reborn as the TR series, imported from Opel in Europe. The 1998 TS Astra became a massive commercial triumph, winning Wheels Car of the Year and spawning the hot hatch SRi and SRi Turbo (147 kW). The 2004 AH brought dynamic European styling and the 177 kW Astra VXR, followed by the PJ VXR coupe and the final high-tech 2016-2020 BK Astra hatchback (European Car of the Year) before Holden's retirement.",
    "australian_market_notes": "The TS Astra was Holden's best-selling passenger car after the Commodore in the late 1990s and early 2000s, renowned for its vault-solid German body rigidity, standard dual airbags, and Lotus-tuned suspension. The sporty SRi and SRi Turbo models earned fierce cult status among hot hatch enthusiasts, while Bertone-styled Astra Convertibles brought accessible European glamour to Australian beaches.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "LB-LC",
            "generation_name": "LB / LC Astra",
            "years": {"start": 1984, "end": 1987},
            "body_styles": ["5-door hatchback"],
            "platform": "Nissan N12 platform",
            "ancap_rating": None,
            "summary": "First Holden Astra, produced jointly with Nissan Australia at Clayton, Victoria. Based on the N12 Pulsar with unique Holden grille and badging.",
            "engines": [
                {
                    "engine_code": "Nissan-E15",
                    "name": "Nissan E15 1.5L OHC Inline-4",
                    "displacement_cc": 1488,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 52.0,
                    "power_rpm": "5600",
                    "torque_nm": 115.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "Single-barrel Hitachi carburettor."
                },
                {
                    "engine_code": "Nissan-E16",
                    "name": "Nissan E16 1.6L OHC Inline-4",
                    "displacement_cc": 1597,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 55.0,
                    "power_rpm": "5600",
                    "torque_nm": 124.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "Introduced in LC update in 1986."
                }
            ],
            "badges": [
                {
                    "badge_name": "SL/X",
                    "years": {"start": 1984, "end": 1987},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "3-speed automatic"],
                    "msrp_aud_min": 8590,
                    "msrp_aud_max": 9980,
                    "fuel_consumption_l_100km": 7.8,
                    "kerb_weight_kg": 910,
                    "standard_features": [
                        "Cloth seat trim",
                        "AM/FM push-button radio",
                        "Split-folding rear seat",
                        "Rear window wiper/washer"
                    ],
                    "notes": "Core private buyer model."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SL/X",
                    "body_style": "Hatchback",
                    "engine_code": "Nissan-E15",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 8590,
                    "power_kw": 52.0,
                    "torque_nm": 115.0,
                    "fuel_l_100km": 7.8,
                    "towing_braked_kg": 600,
                    "notes": "First-generation Australian compact hatch."
                }
            ]
        },
        {
            "series_code": "LD",
            "generation_name": "LD Astra",
            "years": {"start": 1987, "end": 1989},
            "body_styles": ["4-door sedan", "5-door hatchback"],
            "platform": "Nissan N13 platform",
            "ancap_rating": None,
            "summary": "Product of the Button Car Plan sharing the Nissan Pulsar platform, fitted with Holden's locally manufactured Family II 1.6L and 1.8L multi-point EFI engines.",
            "engines": [
                {
                    "engine_code": "Family-II-1.6L",
                    "name": "Holden Family II 16LF 1.6L OHC Inline-4",
                    "displacement_cc": 1598,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 59.0,
                    "power_rpm": "5400",
                    "torque_nm": 124.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "Manufactured at Holden's Fishermans Bend engine plant in Melbourne."
                },
                {
                    "engine_code": "Family-II-1.8L",
                    "name": "Holden Family II 18LE 1.8L EFI Inline-4",
                    "displacement_cc": 1796,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 79.0,
                    "power_rpm": "5600",
                    "torque_nm": 145.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "Bosch multi-point electronic fuel injection."
                }
            ],
            "badges": [
                {
                    "badge_name": "SL/X",
                    "years": {"start": 1987, "end": 1989},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "3-speed automatic"],
                    "msrp_aud_min": 12990,
                    "msrp_aud_max": 14990,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 995,
                    "standard_features": ["1.6L Family II engine", "Power steering", "Tinted glass", "Cloth upholstery"],
                    "notes": "Mainstream sedan and hatch."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SL/X",
                    "body_style": "Sedan",
                    "engine_code": "Family-II-1.8L",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 14200,
                    "power_kw": 79.0,
                    "torque_nm": 145.0,
                    "fuel_l_100km": 8.0,
                    "towing_braked_kg": 750,
                    "notes": "1.8L EFI Family II sedan."
                }
            ]
        },
        {
            "series_code": "TS",
            "generation_name": "TS Astra",
            "years": {"start": 1998, "end": 2005},
            "body_styles": ["3-door hatchback", "5-door hatchback", "4-door sedan", "2-door convertible"],
            "platform": "GM T-body (Opel Astra G)",
            "ancap_rating": 4,
            "summary": "Wheels Car of the Year 1998. Acclaimed German Opel engineering, galvanized steel body, Lotus-tuned dynamic suspension, and the fiery SRi and SRi Turbo hot hatches.",
            "engines": [
                {
                    "engine_code": "ECOTEC-1.8-X18XE1",
                    "name": "Holden ECOTEC 1.8L DOHC 16V Inline-4",
                    "displacement_cc": 1796,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 85.0,
                    "power_rpm": "5400",
                    "torque_nm": 170.0,
                    "torque_rpm": "3400",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Upgraded to Z18XE with 92 kW in late 2000."
                },
                {
                    "engine_code": "ECOTEC-2.2-Z22SE",
                    "name": "Holden ECOTEC 2.2L DOHC 16V Inline-4",
                    "displacement_cc": 2198,
                    "displacement_litres": 2.2,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 108.0,
                    "power_rpm": "5800",
                    "torque_nm": 203.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "All-aluminium engine with twin counter-rotating balance shafts; fitted to Astra SRi."
                },
                {
                    "engine_code": "Turbo-2.0-Z20LET",
                    "name": "Holden 2.0L Turbo DOHC 16V Inline-4",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 147.0,
                    "power_rpm": "5400",
                    "torque_nm": 250.0,
                    "torque_rpm": "1950",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Garrett water-cooled turbocharger, air-to-air intercooler; powers Astra SRi Turbo."
                }
            ],
            "badges": [
                {
                    "badge_name": "City",
                    "years": {"start": 1998, "end": 2004},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 18990,
                    "msrp_aud_max": 21990,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 1130,
                    "standard_features": ["Dual front airbags", "Engine immobiliser", "AM/FM CD stereo", "Power steering"],
                    "notes": "Benchmark entry model."
                },
                {
                    "badge_name": "CD",
                    "years": {"start": 1998, "end": 2005},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 21490,
                    "msrp_aud_max": 24990,
                    "fuel_consumption_l_100km": 7.6,
                    "kerb_weight_kg": 1160,
                    "standard_features": ["Air conditioning", "Power front windows", "Heated electric mirrors", "Velour interior"],
                    "notes": "Popular mid-spec trim."
                },
                {
                    "badge_name": "SRi",
                    "years": {"start": 2001, "end": 2004},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 27990,
                    "msrp_aud_max": 29990,
                    "fuel_consumption_l_100km": 8.6,
                    "kerb_weight_kg": 1240,
                    "standard_features": [
                        "2.2L 108 kW alloy engine",
                        "16-inch alloy wheels",
                        "Sports suspension",
                        "Sports bucket seats with white-faced dials",
                        "Traction control and ABS"
                    ],
                    "notes": "Atmospheric 3-door sports hatch."
                },
                {
                    "badge_name": "SRi Turbo",
                    "years": {"start": 2003, "end": 2004},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 36990,
                    "msrp_aud_max": 37990,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 1290,
                    "standard_features": [
                        "147 kW 2.0L Turbo engine",
                        "17-inch 5-spoke alloy wheels",
                        "Full Irmscher sports body kit",
                        "Cruise control",
                        "Leather sports seats and electronic stability program (ESP)"
                    ],
                    "notes": "Hot hatch legend; 0-100 km/h in 7.0 seconds."
                }
            ],
            "configurations": [
                {
                    "badge_name": "CD",
                    "body_style": "Hatchback",
                    "engine_code": "ECOTEC-1.8-X18XE1",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 21490,
                    "power_kw": 85.0,
                    "torque_nm": 170.0,
                    "fuel_l_100km": 7.4,
                    "towing_braked_kg": 1000,
                    "notes": "Wheels Car of the Year winner."
                },
                {
                    "badge_name": "SRi Turbo",
                    "body_style": "Hatchback",
                    "engine_code": "Turbo-2.0-Z20LET",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 36990,
                    "power_kw": 147.0,
                    "torque_nm": 250.0,
                    "fuel_l_100km": 8.9,
                    "towing_braked_kg": 1200,
                    "notes": "Top-tier hot hatch pocket rocket."
                }
            ]
        },
        {
            "series_code": "AH",
            "generation_name": "AH Astra",
            "years": {"start": 2004, "end": 2009},
            "body_styles": ["3-door coupe", "5-door hatchback", "4-door sedan", "5-door wagon", "2-door TwinTop"],
            "platform": "GM Delta platform (Opel Astra H)",
            "ancap_rating": 4,
            "summary": "Crisp European exterior design, Continuous Damping Control (CDC) sports chassis, punchy CDTi common-rail turbo-diesel, and the blistering 177 kW Astra VXR.",
            "engines": [
                {
                    "engine_code": "ECOTEC-1.8-Z18XER",
                    "name": "Holden ECOTEC 1.8L VVT Inline-4",
                    "displacement_cc": 1796,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 103.0,
                    "power_rpm": "6300",
                    "torque_nm": 175.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16V VVT",
                    "notes": "Variable Valve Timing (VVT)."
                },
                {
                    "engine_code": "Turbo-2.0-VXR-Z20LEH",
                    "name": "Holden VXR 2.0L Turbo DOHC 16V Inline-4",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 177.0,
                    "power_rpm": "5600",
                    "torque_nm": 320.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Forged pistons, under-crown oil spray jets, 1.2 bar boost; powers Astra VXR."
                }
            ],
            "badges": [
                {
                    "badge_name": "CD",
                    "years": {"start": 2004, "end": 2009},
                    "body_styles": ["Hatchback", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 21990,
                    "msrp_aud_max": 24990,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 1215,
                    "standard_features": ["ABS with EBD", "Front and side airbags", "15-inch steel wheels", "Cruise control"],
                    "notes": "High-volume fleet and family choice."
                },
                {
                    "badge_name": "VXR",
                    "years": {"start": 2006, "end": 2009},
                    "body_styles": ["Coupe"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual"],
                    "msrp_aud_min": 42990,
                    "msrp_aud_max": 44990,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 1393,
                    "standard_features": [
                        "177 kW 2.0L Turbo engine",
                        "19-inch alloy wheels",
                        "Recaro leather sports bucket seats",
                        "IDSPlus interactive driving system with continuous damping",
                        "Centre-exit trapezoidal chrome exhaust"
                    ],
                    "notes": "Performance flagship; 244 km/h top speed."
                }
            ],
            "configurations": [
                {
                    "badge_name": "CD",
                    "body_style": "Hatchback",
                    "engine_code": "ECOTEC-1.8-Z18XER",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 21990,
                    "power_kw": 103.0,
                    "torque_nm": 175.0,
                    "fuel_l_100km": 7.4,
                    "towing_braked_kg": 1200,
                    "notes": "Standard Australian specification."
                },
                {
                    "badge_name": "VXR",
                    "body_style": "Coupe",
                    "engine_code": "Turbo-2.0-VXR-Z20LEH",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 42990,
                    "power_kw": 177.0,
                    "torque_nm": 320.0,
                    "fuel_l_100km": 9.2,
                    "towing_braked_kg": 1400,
                    "notes": "High-octane hot hatch icon."
                }
            ]
        },
        {
            "series_code": "BK",
            "generation_name": "BK Astra",
            "years": {"start": 2016, "end": 2020},
            "body_styles": ["5-door hatchback"],
            "platform": "GM D2XX platform (Opel Astra K)",
            "ancap_rating": 5,
            "summary": "European Car of the Year 2016. High-tensile lightweight architecture, Apple CarPlay/Android Auto, IntelliLux LED matrix headlights, and powerful 147 kW 1.6L direct-injection turbo.",
            "engines": [
                {
                    "engine_code": "ECOTEC-1.4T-B14XFT",
                    "name": "Holden ECOTEC 1.4L Direct-Injection Turbo Inline-4",
                    "displacement_cc": 1399,
                    "displacement_litres": 1.4,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 110.0,
                    "power_rpm": "5600",
                    "torque_nm": 240.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16V VVT SIDI",
                    "notes": "Spark Ignition Direct Injection (SIDI) aluminium turbo."
                },
                {
                    "engine_code": "ECOTEC-1.6T-B16SHT",
                    "name": "Holden ECOTEC 1.6L Direct-Injection Turbo Inline-4",
                    "displacement_cc": 1598,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 147.0,
                    "power_rpm": "5500",
                    "torque_nm": 300.0,
                    "torque_rpm": "1650",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16V VVT SIDI",
                    "notes": "Overboost feature lifts torque to 300 Nm in RS and RS-V."
                }
            ],
            "badges": [
                {
                    "badge_name": "R",
                    "years": {"start": 2016, "end": 2020},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 21990,
                    "msrp_aud_max": 24190,
                    "fuel_consumption_l_100km": 5.8,
                    "kerb_weight_kg": 1245,
                    "standard_features": ["7-inch colour touchscreen", "Apple CarPlay & Android Auto", "Rear camera and rear park assist", "17-inch alloy wheels"],
                    "notes": "Entry-level turbo hatch."
                },
                {
                    "badge_name": "RS-V",
                    "years": {"start": 2016, "end": 2020},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 30990,
                    "msrp_aud_max": 33190,
                    "fuel_consumption_l_100km": 6.3,
                    "kerb_weight_kg": 1335,
                    "standard_features": [
                        "147 kW 1.6L Turbo engine",
                        "Leather appointed sports seats with heating",
                        "8-inch touchscreen with embedded satellite navigation",
                        "IntelliLux LED Matrix headlights",
                        "Blind spot alert and lane keep assist"
                    ],
                    "notes": "High-spec flagship hot hatch."
                }
            ],
            "configurations": [
                {
                    "badge_name": "RS-V",
                    "body_style": "Hatchback",
                    "engine_code": "ECOTEC-1.6T-B16SHT",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 30990,
                    "power_kw": 147.0,
                    "torque_nm": 300.0,
                    "fuel_l_100km": 6.3,
                    "towing_braked_kg": 1400,
                    "notes": "147 kW 6-speed manual hot hatch."
                }
            ]
        }
    ]
}

MODEL_BARINA: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "barina",
    "name": "Holden Barina",
    "vehicle_type": "Hatchback / Sedan / Convertible",
    "segment": "Light / Subcompact",
    "years_sold_au": {"start": 1985, "end": 2018},
    "locally_built": False,
    "assembly_plants_au": [
        "Imported (Kosai & Hamamatsu, Japan, MB/ML/MF/MH)",
        "Imported (Zaragoza, Spain, SB/XC)",
        "Imported (Eisenach, Germany, SB/XC)",
        "Imported (Bupyeong, South Korea, TK/TM)"
    ],
    "overview": "For over 33 years across six generations, the Holden Barina was Australia's quintessential light car. Introduced in February 1985 as the MB Barina (a badge-engineered Suzuki Cultus made unforgettable by poet Pam Ayres' commercial: 'Beep beep, Barina!'), the model transitioned through the ML, MF, and MH series. In 1994, Holden pivoted to GM Europe with the SB Barina (Opel Corsa B), creating an Australian youth lifestyle phenomenon that produced the cult Barina GSi (1.6L 16V twin-cam). The 2001 XC Barina won Wheels Car of the Year 2001. Sourcing moved to GM Daewoo in 2005 with the value-focused TK, while the final 2011-2018 TM Barina featured GM's global Gamma II platform, culminating in the sporty Barina RS powered by a 103 kW 1.4L Turbo engine.",
    "australian_market_notes": "The SB Barina revolutionized Australia's light car market, introducing European chassis feel, standard driver airbag options, and vibrant youth-oriented exterior color palettes. It dominated private light car sales for years, while the hot hatch Barina GSi became an enduring grassroots motorsport and hillclimb favorite.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "MB-ML",
            "generation_name": "MB / ML Barina",
            "years": {"start": 1985, "end": 1988},
            "body_styles": ["5-door hatchback"],
            "platform": "Suzuki M-platform (Cultus)",
            "ancap_rating": None,
            "summary": "First-generation Barina. Suzuki Cultus base, celebrated in iconic Pam Ayres television advertising. Super-economical 1.3L four-cylinder engine.",
            "engines": [
                {
                    "engine_code": "Suzuki-G13A",
                    "name": "Suzuki G13A 1.3L OHC Inline-4",
                    "displacement_cc": 1324,
                    "displacement_litres": 1.3,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 54.0,
                    "power_rpm": "5300",
                    "torque_nm": 103.0,
                    "torque_rpm": "3700",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "Lightweight all-aluminium engine block."
                }
            ],
            "badges": [
                {
                    "badge_name": "Barina Hatch",
                    "years": {"start": 1985, "end": 1988},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 7890,
                    "msrp_aud_max": 8890,
                    "fuel_consumption_l_100km": 6.2,
                    "kerb_weight_kg": 735,
                    "standard_features": ["5-speed manual transmission", "AM radio", "Fold-down rear seat", "Cloth seat inserts"],
                    "notes": "Famous 'Beep beep, Barina' icon."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Barina Hatch",
                    "body_style": "Hatchback",
                    "engine_code": "Suzuki-G13A",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 7890,
                    "power_kw": 54.0,
                    "torque_nm": 103.0,
                    "fuel_l_100km": 6.2,
                    "towing_braked_kg": 500,
                    "notes": "Featherweight 735 kg fuel miser."
                }
            ]
        },
        {
            "series_code": "SB",
            "generation_name": "SB Barina",
            "years": {"start": 1994, "end": 2001},
            "body_styles": ["3-door hatchback", "5-door hatchback", "2-door convertible"],
            "platform": "GM4200 platform (Opel Corsa B)",
            "ancap_rating": 3,
            "summary": "Transition to GM Europe Opel Corsa B. Phenomenal sales success among Australian youth; introduced vibrant colors, European ergonomics, and the famous twin-cam Barina GSi hot hatch.",
            "engines": [
                {
                    "engine_code": "ECOTEC-1.4-C14SE",
                    "name": "Holden ECOTEC 1.4L OHC Inline-4",
                    "displacement_cc": 1389,
                    "displacement_litres": 1.4,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 60.0,
                    "power_rpm": "5800",
                    "torque_nm": 114.0,
                    "torque_rpm": "3400",
                    "compression_ratio": "9.8:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "Multi-point fuel injection."
                },
                {
                    "engine_code": "ECOTEC-1.6-C16XE",
                    "name": "Holden ECOTEC 1.6L DOHC 16V Inline-4",
                    "displacement_cc": 1598,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 78.0,
                    "power_rpm": "6000",
                    "torque_nm": 150.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Twin-cam high-revving sports engine in Barina GSi (later X16XE)."
                }
            ],
            "badges": [
                {
                    "badge_name": "City",
                    "years": {"start": 1994, "end": 2000},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 13990,
                    "msrp_aud_max": 15490,
                    "fuel_consumption_l_100km": 6.8,
                    "kerb_weight_kg": 885,
                    "standard_features": ["Side intrusion door beams", "Seatbelt pretensioners", "Body-coloured bumpers", "AM/FM stereo cassette"],
                    "notes": "Youth-oriented 3-door entry model."
                },
                {
                    "badge_name": "GSi",
                    "years": {"start": 1994, "end": 1998},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 21990,
                    "msrp_aud_max": 23490,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 965,
                    "standard_features": [
                        "1.6L 16V DOHC 78 kW engine",
                        "14-inch sports alloy wheels",
                        "Rear spoiler and body kit",
                        "Sports bucket seats",
                        "Anti-lock Braking System (ABS) and power steering"
                    ],
                    "notes": "Celebrated 1990s hot hatch cult classic."
                }
            ],
            "configurations": [
                {
                    "badge_name": "City",
                    "body_style": "Hatchback",
                    "engine_code": "ECOTEC-1.4-C14SE",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 13990,
                    "power_kw": 60.0,
                    "torque_nm": 114.0,
                    "fuel_l_100km": 6.8,
                    "towing_braked_kg": 750,
                    "notes": "Vibrant European-designed compact."
                },
                {
                    "badge_name": "GSi",
                    "body_style": "Hatchback",
                    "engine_code": "ECOTEC-1.6-C16XE",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 21990,
                    "power_kw": 78.0,
                    "torque_nm": 150.0,
                    "fuel_l_100km": 7.4,
                    "towing_braked_kg": 900,
                    "notes": "Pocket rocket hot hatch."
                }
            ]
        },
        {
            "series_code": "TM",
            "generation_name": "TM Barina",
            "years": {"start": 2011, "end": 2018},
            "body_styles": ["5-door hatchback", "4-door sedan"],
            "platform": "GM Gamma II platform",
            "ancap_rating": 5,
            "summary": "Motorcycle-inspired digital gauge cluster, 5-star ANCAP safety across the range, MyLink touch infotainment, and the warm hatch Barina RS with 103 kW 1.4L Turbo.",
            "engines": [
                {
                    "engine_code": "ECOTEC-1.6-F16D4",
                    "name": "Holden ECOTEC 1.6L DOHC 16V Inline-4",
                    "displacement_cc": 1598,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 85.0,
                    "power_rpm": "6000",
                    "torque_nm": 155.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.8:1",
                    "valvetrain": "DOHC 16V VVT",
                    "notes": "Standard engine across CD and CDX."
                },
                {
                    "engine_code": "Turbo-1.4-LUJ",
                    "name": "Holden 1.4L Turbo DOHC 16V Inline-4",
                    "displacement_cc": 1364,
                    "displacement_litres": 1.4,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 103.0,
                    "power_rpm": "4900",
                    "torque_nm": 200.0,
                    "torque_rpm": "1850",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16V VVT",
                    "notes": "Garrett turbocharger, 200 Nm flat torque curve; exclusive to Barina RS."
                }
            ],
            "badges": [
                {
                    "badge_name": "CD",
                    "years": {"start": 2011, "end": 2018},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 15990,
                    "msrp_aud_max": 18190,
                    "fuel_consumption_l_100km": 6.8,
                    "kerb_weight_kg": 1180,
                    "standard_features": ["6 airbags", "Electronic stability control", "15-inch alloy wheels", "Bluetooth connectivity", "Cruise control"],
                    "notes": "5-star ANCAP rating standard."
                },
                {
                    "badge_name": "RS",
                    "years": {"start": 2013, "end": 2017},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 20990,
                    "msrp_aud_max": 23190,
                    "fuel_consumption_l_100km": 6.5,
                    "kerb_weight_kg": 1245,
                    "standard_features": [
                        "103 kW 1.4L Turbo engine",
                        "17-inch sports gunmetal alloy wheels",
                        "10mm lowered sports suspension and quicker steering rack",
                        "Sport leather-wrapped steering wheel and alloy sports pedals",
                        "MyLink 7-inch touchscreen with app integration"
                    ],
                    "notes": "Warm sports hatch edition."
                }
            ],
            "configurations": [
                {
                    "badge_name": "CD",
                    "body_style": "Hatchback",
                    "engine_code": "ECOTEC-1.6-F16D4",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 15990,
                    "power_kw": 85.0,
                    "torque_nm": 155.0,
                    "fuel_l_100km": 6.8,
                    "towing_braked_kg": 1000,
                    "notes": "Everyday city hatch."
                },
                {
                    "badge_name": "RS",
                    "body_style": "Hatchback",
                    "engine_code": "Turbo-1.4-LUJ",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 20990,
                    "power_kw": 103.0,
                    "torque_nm": 200.0,
                    "fuel_l_100km": 6.5,
                    "towing_braked_kg": 1100,
                    "notes": "1.4L Turbo 6-speed manual warm hatch."
                }
            ]
        }
    ]
}

MODEL_CRUZE: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "cruze",
    "name": "Holden Cruze",
    "vehicle_type": "Small SUV / Sedan / Hatchback / Sportwagon",
    "segment": "Small / Compact",
    "years_sold_au": {"start": 2002, "end": 2016},
    "locally_built": True,
    "assembly_plants_au": [
        "Elizabeth, South Australia (JH Series II & III, 2011-2016)",
        "Kosai, Japan (YG crossover, 2002-2006)",
        "Bupyeong, South Korea (JG, 2009-2011)",
        "Gunsan, South Korea (JH Sportwagon, 2012-2016)"
    ],
    "overview": "The Holden Cruze nameplate lived two major chapters in Australia. First launched from 2002 to 2006 as the YG Cruze, it was an innovative subcompact all-wheel-drive crossover co-developed with Suzuki (based on the Ignis) featuring elevated ground clearance and 1.5L power. In 2009, Holden revived the name with the JG Cruze sedan. Most significantly, from March 2011 until October 2016, Holden invested over $1 billion to manufacture the JH Cruze Series II locally on a dedicated assembly line alongside the Commodore at Elizabeth, South Australia. The Australian-built Cruze featured an Australian-designed 5-door hatchback body style, local steering and suspension tuning, high-spec SRi and SRi-V turbo models (1.4L and 1.6L 132 kW turbos), and an efficient 2.0L Turbo Diesel. Over 125,000 Cruzes were built at Elizabeth.",
    "australian_market_notes": "The local production of the JH Cruze represented the return of small-car manufacturing to Australia for the first time since the 1990s. Holden's Melbourne design studio, led by Peter Hughes, penned the 5-door hatchback variant that was exported to world markets. Australian engineers recalibrated the suspension, dampers, and steering rack specifically for rough Australian rural bitumen, providing significantly superior composure compared to imported rivals.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "YG",
            "generation_name": "YG Cruze AWD",
            "years": {"start": 2002, "end": 2006},
            "body_styles": ["5-door SUV crossover"],
            "platform": "Suzuki Ignis platform",
            "ancap_rating": 3,
            "summary": "Subcompact AWD lifestyle crossover joint-venture with Suzuki. High ground clearance, flared wheel arches, and full-time all-wheel drive.",
            "engines": [
                {
                    "engine_code": "Suzuki-M15A",
                    "name": "Suzuki M15A 1.5L DOHC 16V Inline-4",
                    "displacement_cc": 1490,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 74.0,
                    "power_rpm": "5500",
                    "torque_nm": 138.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16V VVT",
                    "notes": "All-aluminium construction with variable valve timing."
                }
            ],
            "badges": [
                {
                    "badge_name": "Cruze AWD",
                    "years": {"start": 2002, "end": 2006},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 19990,
                    "msrp_aud_max": 22490,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 990,
                    "standard_features": ["Viscous-coupling all-wheel drive", "Dual front airbags", "15-inch alloy wheels", "Roof rails", "Air conditioning"],
                    "notes": "Pioneering compact AWD crossover."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Cruze AWD",
                    "body_style": "Hatchback",
                    "engine_code": "Suzuki-M15A",
                    "transmission": "5-speed manual",
                    "drivetrain": "AWD",
                    "msrp_aud": 19990,
                    "power_kw": 74.0,
                    "torque_nm": 138.0,
                    "fuel_l_100km": 7.4,
                    "towing_braked_kg": 800,
                    "notes": "Lightweight AWD pioneer."
                }
            ]
        },
        {
            "series_code": "JH-Series-II",
            "generation_name": "JH Cruze (Locally Manufactured)",
            "years": {"start": 2011, "end": 2016},
            "body_styles": ["4-door sedan", "5-door hatchback", "5-door wagon"],
            "platform": "GM Delta II platform",
            "ancap_rating": 5,
            "summary": "Manufactured at Elizabeth, South Australia. Australian-penned 5-door hatchback, locally tuned suspension and steering, introducing 1.4L Turbo, 1.6L 132 kW Turbo, and 2.0L Turbo Diesel.",
            "engines": [
                {
                    "engine_code": "ECOTEC-1.8-F18D4",
                    "name": "Holden ECOTEC 1.8L DOHC 16V Inline-4",
                    "displacement_cc": 1796,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 104.0,
                    "power_rpm": "6200",
                    "torque_nm": 176.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16V VVT",
                    "notes": "Standard engine in CD and Equipe."
                },
                {
                    "engine_code": "iTi-1.4-Turbo",
                    "name": "Holden 1.4L iTi Turbo DOHC 16V Inline-4",
                    "displacement_cc": 1364,
                    "displacement_litres": 1.4,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 103.0,
                    "power_rpm": "4900",
                    "torque_nm": 200.0,
                    "torque_rpm": "1850",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16V VVT",
                    "notes": "Intelligent Turbo Induction (iTi) with electric power steering and Watts linkage rear suspension."
                },
                {
                    "engine_code": "Turbo-1.6-SIDI",
                    "name": "Holden 1.6L SIDI Turbo DOHC 16V Inline-4",
                    "displacement_cc": 1598,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 132.0,
                    "power_rpm": "5500",
                    "torque_nm": 230.0,
                    "torque_rpm": "2200",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16V VVT SIDI",
                    "notes": "Direct injection performance engine; powers Australian SRi and SRi-V from 2013."
                },
                {
                    "engine_code": "VCDi-2.0-Diesel",
                    "name": "Holden 2.0L VCDi Common-Rail Turbo Diesel Inline-4",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 120.0,
                    "power_rpm": "3800",
                    "torque_nm": 360.0,
                    "torque_rpm": "1750",
                    "compression_ratio": "16.5:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Variable-geometry turbocharger with 360 Nm of torque."
                }
            ],
            "badges": [
                {
                    "badge_name": "Equipe",
                    "years": {"start": 2013, "end": 2016},
                    "body_styles": ["Sedan", "Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "6-speed automatic with Active Select"],
                    "msrp_aud_min": 19490,
                    "msrp_aud_max": 22490,
                    "fuel_consumption_l_100km": 7.0,
                    "kerb_weight_kg": 1390,
                    "standard_features": [
                        "MyLink 7-inch colour touchscreen infotainment",
                        "Rear view camera and rear park sensors",
                        "17-inch alloy wheels",
                        "6 airbags and 5-star ANCAP rating"
                    ],
                    "notes": "Locally built volume sales leader."
                },
                {
                    "badge_name": "SRi-V",
                    "years": {"start": 2011, "end": 2016},
                    "body_styles": ["Sedan", "Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 26490,
                    "msrp_aud_max": 28990,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 1455,
                    "standard_features": [
                        "132 kW 1.6L SIDI Turbo engine (from 2013)",
                        "Watts linkage sports rear suspension",
                        "18-inch sports alloy wheels",
                        "Leather appointed sports seats with heating",
                        "Keyless entry with push-button start and satellite navigation"
                    ],
                    "notes": "Elizabeth-built sports flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Equipe",
                    "body_style": "Sedan",
                    "engine_code": "ECOTEC-1.8-F18D4",
                    "transmission": "6-speed automatic with Active Select",
                    "drivetrain": "FWD",
                    "msrp_aud": 21690,
                    "power_kw": 104.0,
                    "torque_nm": 176.0,
                    "fuel_l_100km": 7.4,
                    "towing_braked_kg": 1200,
                    "notes": "Locally manufactured Australian sedan."
                },
                {
                    "badge_name": "SRi-V",
                    "body_style": "Hatchback",
                    "engine_code": "Turbo-1.6-SIDI",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 26490,
                    "power_kw": 132.0,
                    "torque_nm": 230.0,
                    "fuel_l_100km": 7.4,
                    "towing_braked_kg": 1200,
                    "notes": "132 kW Australian-built sports turbo hatch."
                }
            ]
        }
    ]
}

MODEL_RODEO: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "rodeo",
    "name": "Holden Rodeo",
    "vehicle_type": "Ute / Cab Chassis / Space Cab / Crew Cab 4x2 & 4x4",
    "segment": "Light Commercial / One-Tonne Ute",
    "years_sold_au": {"start": 1980, "end": 2008},
    "locally_built": False,
    "assembly_plants_au": [
        "Imported (Fujisawa, Japan, KB/TF)",
        "Imported (Samut Prakan & Rayong, Thailand, TF/RA)"
    ],
    "overview": "For nearly three decades from 1980 to 2008, the Holden Rodeo was one of Australia's most trusted commercial workhorses and outback touring utilities. Engineered by Isuzu Motors and sold through Holden dealerships across Australia, the Rodeo spanned the tough KB series (1980-1988), the long-running TF series (1988-2003, famous for its bulletproof 2.8L 4JB1-T turbo-diesel and 3.2L V6), and the redesigned RA series (2003-2008). The Rodeo pioneered crew-cab four-wheel-drive dual-cab versatility in Australia, proving equally adept on cattle stations, mining sites, and suburban driveways before being renamed Colorado in 2008.",
    "australian_market_notes": "The Rodeo built an unbreakable reputation for mechanical durability across regional Australia. The 2.8-litre turbo-diesel TF Rodeo was celebrated for regularly clocking 500,000+ kilometers with minimal maintenance. The RA series introduced Holden's 3.6L Alloytec V6 and Isuzu's revered 3.0L 4JJ1 common-rail turbo-diesel, cementing its status as a 3,000 kg towing benchmark.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "KB",
            "generation_name": "KB Rodeo",
            "years": {"start": 1980, "end": 1988},
            "body_styles": ["Single Cab Ute", "Single Cab Chassis", "Space Cab", "Crew Cab"],
            "platform": "Isuzu Faster KB platform",
            "ancap_rating": None,
            "summary": "First-generation Rodeo in Australia, replacing the Chevrolet LUV. Introduced tough ladder-frame chassis, selectable 4WD with free-wheeling front hubs, and economical diesel power.",
            "engines": [
                {
                    "engine_code": "Isuzu-G200Z",
                    "name": "Isuzu G200Z 2.0L OHC Inline-4",
                    "displacement_cc": 1949,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 65.0,
                    "power_rpm": "4600",
                    "torque_nm": 147.0,
                    "torque_rpm": "2600",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "Cast iron block with alloy cylinder head."
                },
                {
                    "engine_code": "Isuzu-C223-Diesel",
                    "name": "Isuzu C223 2.2L OHV Diesel Inline-4",
                    "displacement_cc": 2238,
                    "displacement_litres": 2.2,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Diesel",
                    "power_kw": 45.0,
                    "power_rpm": "4000",
                    "torque_nm": 139.0,
                    "torque_rpm": "2200",
                    "compression_ratio": "21.0:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Indirect diesel injection; extreme durability."
                }
            ],
            "badges": [
                {
                    "badge_name": "Rodeo 4WD Single Cab",
                    "years": {"start": 1980, "end": 1988},
                    "body_styles": ["Single Cab Ute"],
                    "drivetrain": "4WD",
                    "transmissions": ["4-speed manual", "5-speed manual"],
                    "msrp_aud_min": 8990,
                    "msrp_aud_max": 11500,
                    "fuel_consumption_l_100km": 9.8,
                    "kerb_weight_kg": 1350,
                    "standard_features": ["Dual-range transfer case", "Manual locking front hubs", "Heavy-duty rear leaf springs", "1-tonne payload rating"],
                    "notes": "Classic bush workhorse."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Rodeo 4WD Single Cab",
                    "body_style": "Single Cab Ute",
                    "engine_code": "Isuzu-C223-Diesel",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "msrp_aud": 9990,
                    "power_kw": 45.0,
                    "torque_nm": 139.0,
                    "fuel_l_100km": 9.8,
                    "towing_braked_kg": 1400,
                    "notes": "Legendary outback diesel workhorse."
                }
            ]
        },
        {
            "series_code": "TF",
            "generation_name": "TF Rodeo",
            "years": {"start": 1988, "end": 2003},
            "body_styles": ["Single Cab", "Space Cab", "Crew Cab"],
            "platform": "Isuzu TF platform",
            "ancap_rating": 2,
            "summary": "Longest-running Rodeo generation spanning 15 years. Built legendary reputation with 2.8L 4JB1-T turbo-diesel and 3.2L 6VD1 V6 in 4x2 and 4x4 configurations.",
            "engines": [
                {
                    "engine_code": "Isuzu-4JB1-T",
                    "name": "Isuzu 4JB1-T 2.8L Direct-Injection Turbo Diesel Inline-4",
                    "displacement_cc": 2771,
                    "displacement_litres": 2.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 74.0,
                    "power_rpm": "3800",
                    "torque_nm": 225.0,
                    "torque_rpm": "2300",
                    "compression_ratio": "18.2:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Direct injection gear-driven camshaft turbo diesel; legendary longevity."
                },
                {
                    "engine_code": "Isuzu-6VD1-V6",
                    "name": "Isuzu 6VD1 3.2L SOHC 24V V6",
                    "displacement_cc": 3165,
                    "displacement_litres": 3.2,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 140.0,
                    "power_rpm": "5400",
                    "torque_nm": 265.0,
                    "torque_rpm": "4200",
                    "compression_ratio": "9.3:1",
                    "valvetrain": "SOHC 24V",
                    "notes": "Smooth alloy V6 delivering car-like highway cruising."
                }
            ],
            "badges": [
                {
                    "badge_name": "LX Crew Cab 4x4",
                    "years": {"start": 1990, "end": 2003},
                    "body_styles": ["Crew Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 26990,
                    "msrp_aud_max": 34990,
                    "fuel_consumption_l_100km": 10.4,
                    "kerb_weight_kg": 1640,
                    "standard_features": ["Dual-range 4WD", "Power steering", "Air conditioning option", "Cloth bench/bucket seats", "1-tonne payload"],
                    "notes": "Most popular dual-cab configuration."
                },
                {
                    "badge_name": "LT Space Cab / Crew Cab",
                    "years": {"start": 1998, "end": 2003},
                    "body_styles": ["Crew Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 36990,
                    "msrp_aud_max": 42500,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1720,
                    "standard_features": [
                        "3.2L V6 engine standard",
                        "16-inch alloy wheels",
                        "Power windows and mirrors",
                        "Flares and side steps",
                        "Velour upholstery and remote central locking"
                    ],
                    "notes": "Flagship recreational 4x4 ute."
                }
            ],
            "configurations": [
                {
                    "badge_name": "LX Crew Cab 4x4",
                    "body_style": "Crew Cab",
                    "engine_code": "Isuzu-4JB1-T",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "msrp_aud": 31990,
                    "power_kw": 74.0,
                    "torque_nm": 225.0,
                    "fuel_l_100km": 10.2,
                    "towing_braked_kg": 2000,
                    "notes": "2.8L turbo-diesel 4x4 dual cab workhorse."
                },
                {
                    "badge_name": "LT Crew Cab",
                    "body_style": "Crew Cab",
                    "engine_code": "Isuzu-6VD1-V6",
                    "transmission": "4-speed automatic",
                    "drivetrain": "4WD",
                    "msrp_aud": 39990,
                    "power_kw": 140.0,
                    "torque_nm": 265.0,
                    "fuel_l_100km": 12.5,
                    "towing_braked_kg": 2200,
                    "notes": "3.2L V6 petrol luxury 4x4."
                }
            ]
        },
        {
            "series_code": "RA",
            "generation_name": "RA Rodeo",
            "years": {"start": 2003, "end": 2008},
            "body_styles": ["Single Cab", "Space Cab", "Crew Cab"],
            "platform": "Isuzu D-Max / GM GMT355 platform",
            "ancap_rating": 3,
            "summary": "All-new aerodynamic body, push-button electronic 'Shift-on-the-Fly' 4WD, Australian-built 3.6L Alloytec V6, and Isuzu 3.0L common-rail turbo diesel. Final Rodeo series before becoming Colorado.",
            "engines": [
                {
                    "engine_code": "Alloytec-3.6-V6",
                    "name": "Holden Alloytec 3.6L DOHC 24V V6",
                    "displacement_cc": 3564,
                    "displacement_litres": 3.6,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 157.0,
                    "power_rpm": "5300",
                    "torque_nm": 313.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "10.2:1",
                    "valvetrain": "DOHC 24V",
                    "notes": "Cast and assembled in Port Melbourne, Victoria."
                },
                {
                    "engine_code": "Isuzu-4JJ1-TC",
                    "name": "Isuzu 4JJ1-TC 3.0L Common-Rail Turbo Diesel Inline-4",
                    "displacement_cc": 2999,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 120.0,
                    "power_rpm": "3600",
                    "torque_nm": 360.0,
                    "torque_rpm": "1800",
                    "compression_ratio": "17.5:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Common-rail high-pressure injection with intercooler; introduced in 2007."
                }
            ],
            "badges": [
                {
                    "badge_name": "LT Crew Cab 4x4",
                    "years": {"start": 2003, "end": 2008},
                    "body_styles": ["Crew Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 38990,
                    "msrp_aud_max": 44990,
                    "fuel_consumption_l_100km": 10.6,
                    "kerb_weight_kg": 1820,
                    "standard_features": [
                        "Push-button 4WD shift-on-the-fly",
                        "16-inch alloy wheels",
                        "Dual front airbags and ABS with EBD",
                        "Cruise control and power windows",
                        "Fog lamps and chrome sports bar"
                    ],
                    "notes": "Flagship 4x4 dual cab."
                }
            ],
            "configurations": [
                {
                    "badge_name": "LT Crew Cab 4x4",
                    "body_style": "Crew Cab",
                    "engine_code": "Isuzu-4JJ1-TC",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "msrp_aud": 41990,
                    "power_kw": 120.0,
                    "torque_nm": 360.0,
                    "fuel_l_100km": 8.4,
                    "towing_braked_kg": 3000,
                    "notes": "3.0L common-rail turbo diesel 3-tonne tow vehicle."
                }
            ]
        }
    ]
}
