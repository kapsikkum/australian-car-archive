"""Wave 2 Toyota deep-dive models (Part 2): Aurion, Crown, HiAce, Yaris."""

AURION_MODEL = {
    "make_slug": "toyota",
    "model_slug": "aurion",
    "name": "Aurion",
    "vehicle_type": "Large Sedan",
    "segment": "Large Car",
    "years_sold_au": {"start": 2006, "end": 2017},
    "locally_built": True,
    "assembly_plants_au": ["Altona, Victoria (Toyota Motor Corporation Australia)"],
    "overview": "The Toyota Aurion was an Australian-manufactured large front-wheel-drive sedan engineered to compete directly against the Holden Commodore and Ford Falcon. Powered exclusively by the 200kW 3.5-litre 2GR-FE V6 and built at Altona, Victoria, it also sired the legendary Eaton TVS supercharged 241kW TRD Aurion.",
    "australian_market_notes": "Conceived specifically for the Australian market and regional export, the Aurion was launched in October 2006. With bespoke front and rear styling distinct from the four-cylinder Camry, the Aurion captured fleet, police highway patrol, and family sales. The TRD Aurion 3500S and 3500SL, developed by Toyota Racing Development Australia and Prodrive at Clayton VIC, became the world's most powerful front-wheel drive production sedan at release. Production ended on 3 October 2017 with the closure of Altona manufacturing.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "XV40",
            "generation_name": "Aurion 1st Generation",
            "years": {"start": 2006, "end": 2012},
            "body_styles": ["4-door Sedan"],
            "platform": "Toyota K platform",
            "ancap_rating": "4 stars (upgraded to 5 stars from 2009)",
            "summary": "First-generation Australian-built large V6 sedan. Featured the 200kW 2GR-FE V6, standard 6-speed automatic, and the 241kW Eaton TVS supercharged TRD Aurion 3500S/3500SL.",
            "engines": [
                {
                    "engine_code": "2GR-FE",
                    "name": "Toyota 2GR-FE 3.5L Dual VVT-i V6",
                    "displacement_cc": 3456,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 200.0,
                    "power_rpm": "6200",
                    "torque_nm": 336.0,
                    "torque_rpm": "4700",
                    "compression_ratio": "10.8:1",
                    "valvetrain": "DOHC 24-valve Dual VVT-i",
                    "notes": "Altona-assembled V6 running smoothly on regular 91 RON unleaded fuel."
                },
                {
                    "engine_code": "2GR-FZE",
                    "name": "Toyota/TRD 2GR-FZE 3.5L Supercharged V6",
                    "displacement_cc": 3456,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Supercharged (Eaton TVS Twin Vortices Series)",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 241.0,
                    "power_rpm": "6400",
                    "torque_nm": 400.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.8:1",
                    "valvetrain": "DOHC 24-valve Dual VVT-i",
                    "notes": "First production car in the world to feature the Eaton TVS supercharger; 0-100 km/h in 6.1s."
                }
            ],
            "badges": [
                {
                    "badge_name": "AT-X",
                    "years": {"start": 2006, "end": 2012},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 34990,
                    "msrp_aud_max": 35990,
                    "fuel_consumption_l_100km": 9.9,
                    "kerb_weight_kg": 1590,
                    "standard_features": ["6 airbags", "VSC stability control", "Power driver seat", "Cruise control", "16-inch steel wheels with covers"],
                    "notes": "Fleet and private value leader."
                },
                {
                    "badge_name": "Sportivo SX6 / ZR6",
                    "years": {"start": 2006, "end": 2012},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 38990,
                    "msrp_aud_max": 42990,
                    "fuel_consumption_l_100km": 9.9,
                    "kerb_weight_kg": 1615,
                    "standard_features": ["Sports body kit and rear spoiler", "17-inch alloy wheels", "Sports suspension tune", "Leather-accented sports seats (ZR6)"],
                    "notes": "Rivaled Commodore SV6 and Falcon XR6."
                },
                {
                    "badge_name": "Presara",
                    "years": {"start": 2006, "end": 2012},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 49990,
                    "msrp_aud_max": 49990,
                    "fuel_consumption_l_100km": 9.9,
                    "kerb_weight_kg": 1640,
                    "standard_features": ["Leather upholstery", "Satellite navigation", "Smart key entry", "Rear sunshade", "Moonroof", "HID headlamps"],
                    "notes": "Luxury flagship grade."
                },
                {
                    "badge_name": "TRD Aurion 3500S / 3500SL",
                    "years": {"start": 2007, "end": 2009},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed sports automatic"],
                    "msrp_aud_min": 56990,
                    "msrp_aud_max": 61500,
                    "fuel_consumption_l_100km": 10.9,
                    "kerb_weight_kg": 1660,
                    "standard_features": ["241kW supercharged V6", "19-inch alloy wheels with Dunlop SP Sport Maxx tyres", "Brembo-developed 325mm brakes", "TRD sports seats", "TRD aero package"],
                    "notes": "537 units produced by TRD Prodrive in Melbourne; Australian performance cult classic."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Aurion Sportivo ZR6",
                    "body_style": "4-door Sedan",
                    "engine_code": "2GR-FE",
                    "transmission": "6-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 2006,
                    "years_end": 2012,
                    "msrp_aud": 42990,
                    "power_kw": 200.0,
                    "torque_nm": 336.0,
                    "fuel_l_100km": 9.9,
                    "towing_braked_kg": 1600,
                    "notes": "Australian built 200kW performance sedan."
                },
                {
                    "badge_name": "TRD Aurion 3500SL Supercharged",
                    "body_style": "4-door Sedan",
                    "engine_code": "2GR-FZE",
                    "transmission": "6-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 2007,
                    "years_end": 2009,
                    "msrp_aud": 61500,
                    "power_kw": 241.0,
                    "torque_nm": 400.0,
                    "fuel_l_100km": 10.9,
                    "towing_braked_kg": 1200,
                    "notes": "241kW Eaton TVS supercharged halo model."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "XV50",
            "generation_name": "Aurion 2nd Generation",
            "years": {"start": 2012, "end": 2017},
            "body_styles": ["4-door Sedan"],
            "platform": "Toyota K platform",
            "ancap_rating": "5 stars",
            "summary": "Second and final generation built at Altona. Redesigned with higher-tensile steel, 5-star ANCAP safety, refined interior quality, and improved fuel efficiency of 9.3L/100km.",
            "engines": [
                {
                    "engine_code": "2GR-FE",
                    "name": "Toyota 2GR-FE 3.5L Dual VVT-i V6",
                    "displacement_cc": 3456,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 200.0,
                    "power_rpm": "6200",
                    "torque_nm": 336.0,
                    "torque_rpm": "4700",
                    "compression_ratio": "10.8:1",
                    "valvetrain": "DOHC 24-valve Dual VVT-i",
                    "notes": "Refined calibration delivering improved fuel economy."
                }
            ],
            "badges": [
                {
                    "badge_name": "AT-X",
                    "years": {"start": 2012, "end": 2017},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 36490,
                    "msrp_aud_max": 36490,
                    "fuel_consumption_l_100km": 9.3,
                    "kerb_weight_kg": 1555,
                    "standard_features": ["7 airbags standard", "Reversing camera", "Touchscreen display", "16-inch alloy wheels", "Dual-zone climate control"],
                    "notes": "Altona built volume large car."
                },
                {
                    "badge_name": "Sportivo SX6 / ZR6",
                    "years": {"start": 2012, "end": 2017},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 40990,
                    "msrp_aud_max": 47990,
                    "fuel_consumption_l_100km": 9.3,
                    "kerb_weight_kg": 1590,
                    "standard_features": ["Paddle shifters", "18-inch sports alloys", "Body kit", "Sports suspension tune", "Leather sports seats (ZR6)"],
                    "notes": "Aussie-tuned sports suspension."
                },
                {
                    "badge_name": "Presara",
                    "years": {"start": 2012, "end": 2017},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 49990,
                    "msrp_aud_max": 50440,
                    "fuel_consumption_l_100km": 9.3,
                    "kerb_weight_kg": 1625,
                    "standard_features": ["JBL premium 10-speaker audio", "Blind spot monitor", "Lane departure alert", "Sunroof", "Rear electric sunshade"],
                    "notes": "Final Australian-built executive luxury sedan."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Aurion Sportivo ZR6",
                    "body_style": "4-door Sedan",
                    "engine_code": "2GR-FE",
                    "transmission": "6-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 2012,
                    "years_end": 2017,
                    "msrp_aud": 47990,
                    "power_kw": 200.0,
                    "torque_nm": 336.0,
                    "fuel_l_100km": 9.3,
                    "towing_braked_kg": 1600,
                    "notes": "Final Australian-built Toyota V6 sedan before Altona closed in October 2017."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

CROWN_MODEL = {
    "make_slug": "toyota",
    "model_slug": "crown",
    "name": "Crown",
    "vehicle_type": "Luxury Sedan / Station Wagon",
    "segment": "Upper Large / Luxury",
    "years_sold_au": {"start": 1964, "end": 1988},
    "locally_built": True,
    "assembly_plants_au": ["Port Melbourne, Victoria (Australian Motor Industries / AMI)"],
    "overview": "The Toyota Crown established Toyota's reputation for engineering refinement and reliability in Australia. Built locally from CKD packs by Australian Motor Industries (AMI) in Port Melbourne from 1967 to 1979, the Crown offered six-cylinder prestige, luxurious appointments, and long-legged durability across five distinct Australian generations.",
    "australian_market_notes": "First imported in 1964, local assembly at AMI's Port Melbourne plant began with the MS55 third generation in 1967. The locally built MS55, MS65 'Whale', and MS85 series became trusted executive transport, luxury hire cars, and government fleet favorites. Following the cessation of local assembly in 1979, the MS112 and MS123 Royal Saloons were imported fully built from Japan until 1988, introducing Australian buyers to cutting-edge electronic luxury including TEMS suspension and digital instrumentation.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "S50",
            "generation_name": "Crown 3rd Generation (MS55)",
            "years": {"start": 1967, "end": 1971},
            "body_styles": ["4-door Sedan", "5-door Station Wagon"],
            "platform": "Toyota S50",
            "ancap_rating": "Untested",
            "summary": "First locally assembled Toyota Crown built by AMI at Port Melbourne. Powered by the smooth 2.3L M-series inline-six with perimeter frame chassis.",
            "engines": [
                {
                    "engine_code": "2M",
                    "name": "Toyota 2M 2.3L SOHC Inline-6",
                    "displacement_cc": 2253,
                    "displacement_litres": 2.3,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 82.0,
                    "power_rpm": "5200",
                    "torque_nm": 175.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "SOHC 12-valve",
                    "notes": "Cast iron block with aluminium cylinder head."
                }
            ],
            "badges": [
                {
                    "badge_name": "Deluxe Sedan",
                    "years": {"start": 1967, "end": 1971},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual", "3-speed Toyoglide automatic"],
                    "msrp_aud_min": 3690,
                    "msrp_aud_max": 4190,
                    "fuel_consumption_l_100km": 12.5,
                    "kerb_weight_kg": 1310,
                    "standard_features": ["Deep pile carpeting", "Padded dashboard", "Reclining front bench or bucket seats", "Heater/demister", "Push-button radio"],
                    "notes": "AMI Port Melbourne assembled."
                },
                {
                    "badge_name": "Station Wagon",
                    "years": {"start": 1968, "end": 1971},
                    "body_styles": ["5-door Station Wagon"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual", "3-speed Toyoglide automatic"],
                    "msrp_aud_min": 3950,
                    "msrp_aud_max": 4350,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1360,
                    "standard_features": ["Power tailgate window", "Fold-flat cargo floor", "Heavy-duty rear suspension", "Luggage rack"],
                    "notes": "Prestigious family and commercial wagon."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Crown Deluxe Sedan",
                    "body_style": "4-door Sedan",
                    "engine_code": "2M",
                    "transmission": "3-speed Toyoglide automatic",
                    "drivetrain": "RWD",
                    "years_start": 1967,
                    "years_end": 1971,
                    "msrp_aud": 4190,
                    "power_kw": 82.0,
                    "torque_nm": 175.0,
                    "fuel_l_100km": 12.5,
                    "towing_braked_kg": 1200,
                    "notes": "Pioneering Japanese luxury sedan assembled in Melbourne."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "S60/S70",
            "generation_name": "Crown 4th Generation 'Whale' (MS65)",
            "years": {"start": 1971, "end": 1974},
            "body_styles": ["4-door Sedan", "5-door Station Wagon"],
            "platform": "Toyota S60/S70",
            "ancap_rating": "Untested",
            "summary": "Distinctive stepped-hood 'spindle shape' styling earning the Australian nickname 'The Whale'. Upgraded to 2.6L 4M six-cylinder engine, assembled by AMI Port Melbourne.",
            "engines": [
                {
                    "engine_code": "4M",
                    "name": "Toyota 4M 2.6L SOHC Inline-6",
                    "displacement_cc": 2563,
                    "displacement_litres": 2.6,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 104.0,
                    "power_rpm": "5400",
                    "torque_nm": 196.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "SOHC 12-valve",
                    "notes": "Substantial torque increase over the 2M."
                }
            ],
            "badges": [
                {
                    "badge_name": "SE / Super Saloon",
                    "years": {"start": 1971, "end": 1974},
                    "body_styles": ["4-door Sedan", "Station Wagon"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual", "3-speed automatic"],
                    "msrp_aud_min": 4790,
                    "msrp_aud_max": 5490,
                    "fuel_consumption_l_100km": 13.0,
                    "kerb_weight_kg": 1380,
                    "standard_features": ["Power steering", "Air conditioning option", "Separate bucket seats", "Electrically heated rear glass"],
                    "notes": "AMI Port Melbourne assembly."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Crown SE 2600 Sedan",
                    "body_style": "4-door Sedan",
                    "engine_code": "4M",
                    "transmission": "3-speed automatic",
                    "drivetrain": "RWD",
                    "years_start": 1971,
                    "years_end": 1974,
                    "msrp_aud": 5190,
                    "power_kw": 104.0,
                    "torque_nm": 196.0,
                    "fuel_l_100km": 13.0,
                    "towing_braked_kg": 1300,
                    "notes": "Cult 1970s Australian executive cruiser."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "S80/S100",
            "generation_name": "Crown 5th Generation (MS85)",
            "years": {"start": 1974, "end": 1979},
            "body_styles": ["4-door Sedan", "5-door Station Wagon"],
            "platform": "Toyota S80/S100",
            "ancap_rating": "Untested",
            "summary": "Return to formal, conservative three-box sedan styling. Final generation assembled in Port Melbourne by AMI until Australian tariff and local content rules phased it out in 1979.",
            "engines": [
                {
                    "engine_code": "4M-ADR",
                    "name": "Toyota 4M 2.6L SOHC Inline-6 (ADR27A)",
                    "displacement_cc": 2563,
                    "displacement_litres": 2.6,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 82.0,
                    "power_rpm": "5000",
                    "torque_nm": 181.0,
                    "torque_rpm": "3400",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "SOHC 12-valve",
                    "notes": "Retuned to comply with Australian Design Rule 27A emissions standards."
                }
            ],
            "badges": [
                {
                    "badge_name": "Super Saloon",
                    "years": {"start": 1974, "end": 1979},
                    "body_styles": ["4-door Sedan", "Station Wagon"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual", "3-speed automatic"],
                    "msrp_aud_min": 6890,
                    "msrp_aud_max": 9950,
                    "fuel_consumption_l_100km": 13.5,
                    "kerb_weight_kg": 1420,
                    "standard_features": ["Four-wheel disc brakes", "Power windows", "Power steering", "Velour upholstery", "Tinted glass"],
                    "notes": "Final Australian assembled Crown."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Crown Super Saloon",
                    "body_style": "4-door Sedan",
                    "engine_code": "4M-ADR",
                    "transmission": "3-speed automatic",
                    "drivetrain": "RWD",
                    "years_start": 1974,
                    "years_end": 1979,
                    "msrp_aud": 8950,
                    "power_kw": 82.0,
                    "torque_nm": 181.0,
                    "fuel_l_100km": 13.5,
                    "towing_braked_kg": 1300,
                    "notes": "Last Crown built at AMI Port Melbourne plant."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "S110",
            "generation_name": "Crown 6th Generation (MS112)",
            "years": {"start": 1979, "end": 1983},
            "body_styles": ["4-door Sedan"],
            "platform": "Toyota S110",
            "ancap_rating": "Untested",
            "summary": "Imported fully built from Japan. Introduced electronic fuel injection (5M-E 2.8L), 4-wheel independent rear suspension, and 4-speed overdrive automatic.",
            "engines": [
                {
                    "engine_code": "5M-E",
                    "name": "Toyota 5M-E 2.8L EFI SOHC Inline-6",
                    "displacement_cc": 2759,
                    "displacement_litres": 2.8,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 107.0,
                    "power_rpm": "5200",
                    "torque_nm": 222.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "SOHC 12-valve EFI",
                    "notes": "Bosch L-Jetronic fuel injection delivering effortless highway cruising."
                }
            ],
            "badges": [
                {
                    "badge_name": "Royal Saloon",
                    "years": {"start": 1979, "end": 1983},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed automatic with overdrive"],
                    "msrp_aud_min": 17990,
                    "msrp_aud_max": 23500,
                    "fuel_consumption_l_100km": 11.9,
                    "kerb_weight_kg": 1490,
                    "standard_features": ["Dual-zone climate control with rear air controls", "Power front and rear seats", "Cruise control", "Alloy wheels"],
                    "notes": "Fully imported Japanese luxury flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Crown Royal Saloon 2.8i",
                    "body_style": "4-door Sedan",
                    "engine_code": "5M-E",
                    "transmission": "4-speed automatic with overdrive",
                    "drivetrain": "RWD",
                    "years_start": 1979,
                    "years_end": 1983,
                    "msrp_aud": 21500,
                    "power_kw": 107.0,
                    "torque_nm": 222.0,
                    "fuel_l_100km": 11.9,
                    "towing_braked_kg": 1400,
                    "notes": "Flagship Japanese luxury cruiser in Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "S120",
            "generation_name": "Crown 7th Generation (MS123)",
            "years": {"start": 1983, "end": 1988},
            "body_styles": ["4-door Sedan"],
            "platform": "Toyota S120",
            "ancap_rating": "Untested",
            "summary": "The final official Australian-market Crown generation. Featured the Twin Cam 24 5M-GE engine, digital instruments, and TEMS electronically modulated suspension.",
            "engines": [
                {
                    "engine_code": "5M-GE",
                    "name": "Toyota 5M-GE 2.8L DOHC 24V Inline-6",
                    "displacement_cc": 2759,
                    "displacement_litres": 2.8,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 125.0,
                    "power_rpm": "5600",
                    "torque_nm": 226.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.2:1",
                    "valvetrain": "DOHC 24-valve EFI",
                    "notes": "Twin-cam performance shared with MA61 Celica Supra."
                }
            ],
            "badges": [
                {
                    "badge_name": "Royal Saloon Twin Cam",
                    "years": {"start": 1983, "end": 1988},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed electronic automatic"],
                    "msrp_aud_min": 28990,
                    "msrp_aud_max": 38500,
                    "fuel_consumption_l_100km": 11.6,
                    "kerb_weight_kg": 1520,
                    "standard_features": ["TEMS electronic suspension damping", "Digital instrument cluster", "Rear seat audio and AC controls", "Electric moonroof"],
                    "notes": "Final Crown generation officially marketed through Toyota Australia dealer network."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Crown Royal Saloon Twin Cam",
                    "body_style": "4-door Sedan",
                    "engine_code": "5M-GE",
                    "transmission": "4-speed electronic automatic",
                    "drivetrain": "RWD",
                    "years_start": 1983,
                    "years_end": 1988,
                    "msrp_aud": 34990,
                    "power_kw": 125.0,
                    "torque_nm": 226.0,
                    "fuel_l_100km": 11.6,
                    "towing_braked_kg": 1500,
                    "notes": "Ultimate evolution of official Australian-delivered Crown."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

HIACE_MODEL = {
    "make_slug": "toyota",
    "model_slug": "hiace",
    "name": "HiAce",
    "vehicle_type": "Commercial Van / Commuter Bus",
    "segment": "Commercial Van",
    "years_sold_au": {"start": 1971, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Toyota HiAce is the unquestioned titan of Australian commercial vans and passenger shuttle transport. Across more than half a century, its cab-over and semi-bonnet configurations have kept Australian tradespeople, couriers, airport shuttles, and tourism fleets moving with renowned reliability and outstanding resale value.",
    "australian_market_notes": "First imported in 1971, the HiAce captured majority market share in the medium commercial van category for decades. While early H10-H200 generations used a cab-over-engine layout maximizing cargo length, the sixth-generation H300 moved to a semi-bonnet design to achieve a 5-star ANCAP safety rating while introducing the 130kW/450Nm 2.8GD turbo diesel and V6 power.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "H10/H20/H30/H40",
            "generation_name": "HiAce 1st & 2nd Generation",
            "years": {"start": 1971, "end": 1982},
            "body_styles": ["SWB Van", "LWB Van", "Commuter Bus", "Cab Chassis Ute"],
            "platform": "Toyota H10/H20",
            "ancap_rating": "Untested",
            "summary": "Established the HiAce name in Australia with cab-over forward control layout, sliding side door, and bulletproof 1.6L 12R and 2.0L 18R four-cylinder engines.",
            "engines": [
                {
                    "engine_code": "18R",
                    "name": "Toyota 18R 2.0L Petrol",
                    "displacement_cc": 1968,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 65.0,
                    "power_rpm": "5000",
                    "torque_nm": 145.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Mainstay commercial workhorse."
                }
            ],
            "badges": [
                {
                    "badge_name": "Standard Van / Commuter",
                    "years": {"start": 1971, "end": 1982},
                    "body_styles": ["SWB Van", "LWB Van", "Commuter Bus"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual", "5-speed manual"],
                    "msrp_aud_min": 2490,
                    "msrp_aud_max": 5990,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 1280,
                    "standard_features": ["Vinyl seating", "Heater/demister", "Column gearshift", "Rear tailgate or barn doors"],
                    "notes": "Aussie courier benchmark."
                }
            ],
            "configurations": [
                {
                    "badge_name": "HiAce LWB Van",
                    "body_style": "LWB Van",
                    "engine_code": "18R",
                    "transmission": "4-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1977,
                    "years_end": 1982,
                    "msrp_aud": 4990,
                    "power_kw": 65.0,
                    "torque_nm": 145.0,
                    "fuel_l_100km": 11.5,
                    "towing_braked_kg": 1000,
                    "notes": "1-tonne payload commercial workhorse."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "H50/H60/H70",
            "generation_name": "HiAce 3rd Generation",
            "years": {"start": 1982, "end": 1989},
            "body_styles": ["SWB Van", "LWB Van", "Super LWB Commuter Bus"],
            "platform": "Toyota H50",
            "ancap_rating": "Untested",
            "summary": "Crisper squared-off styling, introduction of the 2.4L 2L diesel engine and 2.0L 3Y petrol, cementing domination of airport shuttle and delivery trades.",
            "engines": [
                {
                    "engine_code": "2L",
                    "name": "Toyota 2L 2.4L Diesel",
                    "displacement_cc": 2446,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Diesel",
                    "power_kw": 54.0,
                    "power_rpm": "4000",
                    "torque_nm": 156.0,
                    "torque_rpm": "2200",
                    "compression_ratio": "22.2:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Indestructible naturally aspirated diesel."
                }
            ],
            "badges": [
                {
                    "badge_name": "Van / Commuter Bus",
                    "years": {"start": 1982, "end": 1989},
                    "body_styles": ["SWB Van", "LWB Van", "Commuter"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 9890,
                    "msrp_aud_max": 18500,
                    "fuel_consumption_l_100km": 9.8,
                    "kerb_weight_kg": 1410,
                    "standard_features": ["Side sliding door", "Front disc brakes", "Flow-through ventilation", "14-seat capacity (Commuter)"],
                    "notes": "Omnipresent tourist bus."
                }
            ],
            "configurations": [
                {
                    "badge_name": "HiAce Commuter Diesel",
                    "body_style": "Super LWB Commuter Bus",
                    "engine_code": "2L",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1983,
                    "years_end": 1989,
                    "msrp_aud": 16990,
                    "power_kw": 54.0,
                    "torque_nm": 156.0,
                    "fuel_l_100km": 9.8,
                    "towing_braked_kg": 1200,
                    "notes": "The ubiquitous Australian hotel and airport transfer minibus."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "H100",
            "generation_name": "HiAce 4th Generation",
            "years": {"start": 1989, "end": 2004},
            "body_styles": ["SWB Van", "LWB Van", "Super LWB Commuter Bus", "SBV Walk-Through"],
            "platform": "Toyota H100",
            "ancap_rating": "Untested",
            "summary": "15-year continuous production icon in Australia. Introduced 2.4L 2RZ-E EFI petrol and 2.8L 3L / 3.0L 5L diesels with aerodynamic flush-glass styling.",
            "engines": [
                {
                    "engine_code": "2RZ-E",
                    "name": "Toyota 2RZ-E 2.4L EFI Petrol",
                    "displacement_cc": 2438,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 88.0,
                    "power_rpm": "4800",
                    "torque_nm": 198.0,
                    "torque_rpm": "2600",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "SOHC 8-valve EFI",
                    "notes": "Workhorse EFI engine powering couriers nationwide."
                },
                {
                    "engine_code": "5L",
                    "name": "Toyota 5L 3.0L Diesel",
                    "displacement_cc": 2986,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Diesel",
                    "power_kw": 65.0,
                    "power_rpm": "4000",
                    "torque_nm": 197.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "22.2:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Legendary long-life naturally aspirated diesel."
                }
            ],
            "badges": [
                {
                    "badge_name": "LWB Van",
                    "years": {"start": 1989, "end": 2004},
                    "body_styles": ["LWB Van"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 19990,
                    "msrp_aud_max": 32000,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1520,
                    "standard_features": ["Power steering (later standard)", "AM/FM radio", "Side impact protection", "Rear wiper/washer"],
                    "notes": "Australia's undisputed #1 commercial delivery van."
                },
                {
                    "badge_name": "Commuter Bus",
                    "years": {"start": 1989, "end": 2004},
                    "body_styles": ["Super LWB Commuter Bus"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 32990,
                    "msrp_aud_max": 42000,
                    "fuel_consumption_l_100km": 10.9,
                    "kerb_weight_kg": 1780,
                    "standard_features": ["14 seats", "High roof", "Rear air conditioning", "Emergency roof hatch", "Tinted passenger glass"],
                    "notes": "Backbone of regional tour and airport operations."
                }
            ],
            "configurations": [
                {
                    "badge_name": "HiAce LWB EFI Van",
                    "body_style": "LWB Van",
                    "engine_code": "2RZ-E",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1998,
                    "years_end": 2004,
                    "msrp_aud": 27990,
                    "power_kw": 88.0,
                    "torque_nm": 198.0,
                    "fuel_l_100km": 10.5,
                    "towing_braked_kg": 1400,
                    "notes": "Peak fourth-generation volume configuration."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "H200",
            "generation_name": "HiAce 5th Generation",
            "years": {"start": 2004, "end": 2019},
            "body_styles": ["LWB Van", "Super LWB Van", "Commuter Bus"],
            "platform": "Toyota H200",
            "ancap_rating": "4 stars",
            "summary": "15-year reign with wide-body Super LWB options, 2.7L VVTi petrol and 3.0L D-4D common-rail turbo diesel delivering supreme reliability and strong resale values.",
            "engines": [
                {
                    "engine_code": "1KD-FTV",
                    "name": "Toyota 1KD-FTV 3.0L D-4D Turbo Diesel",
                    "displacement_cc": 2982,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 100.0,
                    "power_rpm": "3400",
                    "torque_nm": 300.0,
                    "torque_rpm": "1200-2400",
                    "compression_ratio": "16.0:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Common-rail injection with tremendous torque off idle."
                },
                {
                    "engine_code": "2TR-FE",
                    "name": "Toyota 2TR-FE 2.7L VVT-i Petrol",
                    "displacement_cc": 2694,
                    "displacement_litres": 2.7,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 111.0,
                    "power_rpm": "4800",
                    "torque_nm": 241.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "9.6:1",
                    "valvetrain": "DOHC 16-valve VVT-i",
                    "notes": "Low maintenance petrol workhorse."
                }
            ],
            "badges": [
                {
                    "badge_name": "LWB Van",
                    "years": {"start": 2005, "end": 2019},
                    "body_styles": ["LWB Van"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed auto", "6-speed auto"],
                    "msrp_aud_min": 31990,
                    "msrp_aud_max": 41990,
                    "fuel_consumption_l_100km": 8.7,
                    "kerb_weight_kg": 1690,
                    "standard_features": ["Dual front airbags", "ABS brakes", "Air conditioning", "Reversing camera (from 2012)", "Cruise control (facelift)"],
                    "notes": "Aussie tradie standard vehicle."
                },
                {
                    "badge_name": "Super LWB / Commuter",
                    "years": {"start": 2005, "end": 2019},
                    "body_styles": ["Super LWB Van", "Commuter Bus"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed auto", "6-speed auto"],
                    "msrp_aud_min": 41990,
                    "msrp_aud_max": 59990,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 1920,
                    "standard_features": ["High roof", "Wide body", "Rear air conditioning", "14 seats (Commuter)", "Sliding side step"],
                    "notes": "Dominated 14-seat transport sector."
                }
            ],
            "configurations": [
                {
                    "badge_name": "HiAce LWB Turbo Diesel",
                    "body_style": "LWB Van",
                    "engine_code": "1KD-FTV",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 2006,
                    "years_end": 2019,
                    "msrp_aud": 38490,
                    "power_kw": 100.0,
                    "torque_nm": 300.0,
                    "fuel_l_100km": 8.7,
                    "towing_braked_kg": 1400,
                    "notes": "Top-selling fleet van across Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "H300",
            "generation_name": "HiAce 6th Generation",
            "years": {"start": 2019, "end": "Present"},
            "body_styles": ["LWB Van", "LWB Crew Van", "Super LWB Van", "Commuter Bus"],
            "platform": "Toyota TNGA-based commercial platform",
            "ancap_rating": "5 stars",
            "summary": "Moved engine forward into a semi-bonnet architecture to achieve maximum 5-star ANCAP safety, powered by the 2.8L 1GD-FTV turbo diesel (130kW/450Nm) and 3.5L V6, with 6-speed transmissions.",
            "engines": [
                {
                    "engine_code": "1GD-FTV",
                    "name": "Toyota 1GD-FTV 2.8L D-4D Turbo Diesel",
                    "displacement_cc": 2755,
                    "displacement_litres": 2.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 130.0,
                    "power_rpm": "3400",
                    "torque_nm": 450.0,
                    "torque_rpm": "1600-2400",
                    "compression_ratio": "15.6:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Shared with HiLux and Prado; robust 450Nm of pulling power."
                },
                {
                    "engine_code": "7GR-FKS",
                    "name": "Toyota 7GR-FKS 3.5L Dual VVT-i V6",
                    "displacement_cc": 3456,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 207.0,
                    "power_rpm": "6000",
                    "torque_nm": 351.0,
                    "torque_rpm": "4600",
                    "compression_ratio": "11.8:1",
                    "valvetrain": "DOHC 24-valve Dual VVT-i",
                    "notes": "Available from 2019 to 2022."
                }
            ],
            "badges": [
                {
                    "badge_name": "LWB Van",
                    "years": {"start": 2019, "end": "Present"},
                    "body_styles": ["LWB Van"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 38640,
                    "msrp_aud_max": 47760,
                    "fuel_consumption_l_100km": 7.5,
                    "kerb_weight_kg": 2180,
                    "standard_features": ["Toyota Safety Sense with AEB & pedestrian detection", "Lane departure alert", "Blind spot monitor", "7 airbags", "Apple CarPlay & Android Auto"],
                    "notes": "5-star ANCAP commercial safety benchmark."
                },
                {
                    "badge_name": "Super LWB Van / Commuter",
                    "years": {"start": 2019, "end": "Present"},
                    "body_styles": ["Super LWB Van", "Commuter Bus"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 52640,
                    "msrp_aud_max": 73000,
                    "fuel_consumption_l_100km": 8.0,
                    "kerb_weight_kg": 2400,
                    "standard_features": ["12-seat capacity (Commuter GL)", "Power sliding side door", "Rear climate control", "Sat nav", "Front and rear parking sensors"],
                    "notes": "Can be driven on standard car licence (12-seat Commuter GL)."
                }
            ],
            "configurations": [
                {
                    "badge_name": "HiAce LWB 2.8 Turbo Diesel Auto",
                    "body_style": "LWB Van",
                    "engine_code": "1GD-FTV",
                    "transmission": "6-speed automatic",
                    "drivetrain": "RWD",
                    "years_start": 2019,
                    "years_end": "Present",
                    "msrp_aud": 47760,
                    "power_kw": 130.0,
                    "torque_nm": 450.0,
                    "fuel_l_100km": 8.2,
                    "towing_braked_kg": 1500,
                    "notes": "High safety, comfortable commercial benchmark."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

YARIS_MODEL = {
    "make_slug": "toyota",
    "model_slug": "yaris",
    "name": "Echo / Yaris / GR Yaris",
    "vehicle_type": "Hatchback / Sedan / Hot Hatch",
    "segment": "Light Car / Performance",
    "years_sold_au": {"start": 1999, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "Toyota's light car family in Australia spans from the quirky, spacious Echo through three generations of Yaris hatchbacks and sedans to the hyper-capable GR Yaris Rallye AWD homologation special. Combining exceptional reliability, hybrid fuel efficiency, and World Rally Championship engineering, it is a giant of small-car motoring.",
    "australian_market_notes": "Launched as the Echo in October 1999, it won the 1999 Wheels Car of the Year award for clever packaging and ultra-efficient VVT-i engines. Renamed Yaris in 2005, it became an urban staple. In late 2020, Toyota astonished the Australian market by launching the bespoke GR Yaris at an introductory price of $39,950 driveaway (followed by the limited Rallye edition), instantly selling out all allocations and earning acclaim as one of the greatest homologation hot hatches of the modern era.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "NCP10",
            "generation_name": "Echo (1st Gen Yaris)",
            "years": {"start": 1999, "end": 2005},
            "body_styles": ["3-door Hatch", "5-door Hatch", "4-door Sedan"],
            "platform": "Toyota NBC platform",
            "ancap_rating": "3 stars",
            "summary": "1999 Wheels Car of the Year winner. Centrally mounted digital 3D instrument binnacle, tall roof packaging, and ultra-efficient 1.3L 2NZ-FE and 1.5L 1NZ-FE engines.",
            "engines": [
                {
                    "engine_code": "2NZ-FE",
                    "name": "Toyota 2NZ-FE 1.3L VVT-i",
                    "displacement_cc": 1299,
                    "displacement_litres": 1.3,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 63.0,
                    "power_rpm": "6000",
                    "torque_nm": 122.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16-valve VVT-i",
                    "notes": "Pioneering VVT-i light car engine returning under 6.0L/100km."
                },
                {
                    "engine_code": "1NZ-FE",
                    "name": "Toyota 1NZ-FE 1.5L VVT-i",
                    "displacement_cc": 1497,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 80.0,
                    "power_rpm": "6000",
                    "torque_nm": 142.0,
                    "torque_rpm": "4200",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16-valve VVT-i",
                    "notes": "Standard in Echo Sedan and Echo Sportivo."
                }
            ],
            "badges": [
                {
                    "badge_name": "Echo Hatch",
                    "years": {"start": 1999, "end": 2005},
                    "body_styles": ["3-door Hatch", "5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 14990,
                    "msrp_aud_max": 18990,
                    "fuel_consumption_l_100km": 5.8,
                    "kerb_weight_kg": 880,
                    "standard_features": ["Central digital instrument cluster", "60/40 sliding rear seat", "Twin gloveboxes", "Driver airbag (later dual)"],
                    "notes": "1999 Wheels COTY winner."
                },
                {
                    "badge_name": "Echo Sportivo",
                    "years": {"start": 2001, "end": 2005},
                    "body_styles": ["3-door Hatch", "5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 19990,
                    "msrp_aud_max": 20990,
                    "fuel_consumption_l_100km": 6.4,
                    "kerb_weight_kg": 920,
                    "standard_features": ["1.5L 80kW engine", "14-inch alloy wheels", "Sports suspension tune", "Body kit", "Leather steering wheel", "Sports seats"],
                    "notes": "Nimble pocket rocket weighing under 950kg."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Echo Sportivo Hatch",
                    "body_style": "3-door Hatch",
                    "engine_code": "1NZ-FE",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2001,
                    "years_end": 2005,
                    "msrp_aud": 19990,
                    "power_kw": 80.0,
                    "torque_nm": 142.0,
                    "fuel_l_100km": 6.4,
                    "towing_braked_kg": 700,
                    "notes": "Original lightweight warm hatch."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "NCP90",
            "generation_name": "Yaris 1st Generation (AU)",
            "years": {"start": 2005, "end": 2011},
            "body_styles": ["3-door Hatch", "5-door Hatch", "4-door Sedan"],
            "platform": "Toyota B platform",
            "ancap_rating": "5 stars (with safety pack)",
            "summary": "First generation to adopt the global Yaris name in Australia. Offered YR (1.3L), YRS (1.5L), and sporty YRX grades.",
            "engines": [
                {
                    "engine_code": "1NZ-FE",
                    "name": "Toyota 1NZ-FE 1.5L VVT-i",
                    "displacement_cc": 1497,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 80.0,
                    "power_rpm": "6000",
                    "torque_nm": 141.0,
                    "torque_rpm": "4200",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16-valve VVT-i",
                    "notes": "Fitted to YRS and YRX trims."
                }
            ],
            "badges": [
                {
                    "badge_name": "YR",
                    "years": {"start": 2005, "end": 2011},
                    "body_styles": ["3-door Hatch", "5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 14990,
                    "msrp_aud_max": 17490,
                    "fuel_consumption_l_100km": 6.0,
                    "kerb_weight_kg": 1020,
                    "standard_features": ["Central display", "Air conditioning", "Power front windows", "Dual airbags", "ABS brakes"],
                    "notes": "Affordable city runabout."
                },
                {
                    "badge_name": "YRX",
                    "years": {"start": 2005, "end": 2011},
                    "body_styles": ["3-door Hatch", "5-door Hatch", "4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 19490,
                    "msrp_aud_max": 21990,
                    "fuel_consumption_l_100km": 6.1,
                    "kerb_weight_kg": 1055,
                    "standard_features": ["1.5L 80kW engine", "15-inch alloy wheels", "Sports body kit and rear spoiler", "Front fog lamps", "Leather steering wheel"],
                    "notes": "Top trim hatch and sedan."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Yaris YRX 5-door",
                    "body_style": "5-door Hatch",
                    "engine_code": "1NZ-FE",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2005,
                    "years_end": 2011,
                    "msrp_aud": 19490,
                    "power_kw": 80.0,
                    "torque_nm": 141.0,
                    "fuel_l_100km": 6.1,
                    "towing_braked_kg": 900,
                    "notes": "Popular first-car choice in Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "NCP130",
            "generation_name": "Yaris 2nd Generation (AU)",
            "years": {"start": 2011, "end": 2020},
            "body_styles": ["5-door Hatch"],
            "platform": "Toyota B platform",
            "ancap_rating": "5 stars",
            "summary": "Moved to conventional driver-facing instruments. Lineup standardized as Ascent (1.3L), SX (1.5L), and ZR (1.5L with LED headlamps and sports kit).",
            "engines": [
                {
                    "engine_code": "1NZ-FE",
                    "name": "Toyota 1NZ-FE 1.5L VVT-i",
                    "displacement_cc": 1497,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 80.0,
                    "power_rpm": "6000",
                    "torque_nm": 141.0,
                    "torque_rpm": "4200",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16-valve VVT-i",
                    "notes": "Dependable workhorse powertrain."
                }
            ],
            "badges": [
                {
                    "badge_name": "Ascent",
                    "years": {"start": 2011, "end": 2020},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 15490,
                    "msrp_aud_max": 17290,
                    "fuel_consumption_l_100km": 5.7,
                    "kerb_weight_kg": 1010,
                    "standard_features": ["7 airbags standard", "Reversing camera", "6.1-inch touchscreen", "Cruise control", "Emergency brake assist"],
                    "notes": "5-star ANCAP rating standard."
                },
                {
                    "badge_name": "ZR",
                    "years": {"start": 2011, "end": 2020},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 21490,
                    "msrp_aud_max": 23590,
                    "fuel_consumption_l_100km": 6.4,
                    "kerb_weight_kg": 1050,
                    "standard_features": ["1.5L engine", "Bi-LED headlights", "16-inch alloy wheels", "Sports seats", "Rear spoiler", "Sat nav"],
                    "notes": "Sporty urban flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Yaris Ascent Auto",
                    "body_style": "5-door Hatch",
                    "engine_code": "1NZ-FE",
                    "transmission": "4-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 2014,
                    "years_end": 2020,
                    "msrp_aud": 17290,
                    "power_kw": 80.0,
                    "torque_nm": 141.0,
                    "fuel_l_100km": 6.4,
                    "towing_braked_kg": 900,
                    "notes": "High volume Australian suburban runabout."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "XP210",
            "generation_name": "Yaris 3rd Gen & GR Yaris",
            "years": {"start": 2020, "end": "Present"},
            "body_styles": ["5-door Hatch", "3-door Performance Hatch"],
            "platform": "TNGA-B (GA-B) / GR-FOUR bespoke chassis",
            "ancap_rating": "5 stars (Standard Yaris)",
            "summary": "Revolutionary leap on TNGA-B platform featuring standard hybrid returning 3.3L/100km, alongside the bespoke GR Yaris and GR Yaris Rallye WRC homologation hero.",
            "engines": [
                {
                    "engine_code": "M15A-FXE",
                    "name": "Toyota M15A-FXE 1.5L Hybrid",
                    "displacement_cc": 1490,
                    "displacement_litres": 1.5,
                    "cylinders": 3,
                    "configuration": "Inline-3",
                    "aspiration": "Naturally Aspirated + Electric Motor",
                    "fuel_type": "Petrol Hybrid",
                    "power_kw": 85.0,
                    "power_rpm": "5500",
                    "torque_nm": 141.0,
                    "torque_rpm": "3800-4800",
                    "compression_ratio": "14.0:1",
                    "valvetrain": "DOHC 12-valve Dual VVT-i",
                    "notes": "Remarkable 3.3L/100km combined fuel consumption."
                },
                {
                    "engine_code": "G16E-GTS",
                    "name": "Toyota G16E-GTS 1.6L Turbo (GR Yaris)",
                    "displacement_cc": 1618,
                    "displacement_litres": 1.6,
                    "cylinders": 3,
                    "configuration": "Inline-3",
                    "aspiration": "Single-Scroll Ball-Bearing Turbocharged",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 200.0,
                    "power_rpm": "6500",
                    "torque_nm": 370.0,
                    "torque_rpm": "3000-4600",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 12-valve Dual VVT-i",
                    "notes": "World's most powerful production 3-cylinder engine; carbon-fibre roof, aluminium doors/bonnet."
                }
            ],
            "badges": [
                {
                    "badge_name": "Ascent Sport / SX Hybrid",
                    "years": {"start": 2020, "end": "Present"},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["e-CVT", "CVT"],
                    "msrp_aud_min": 24800,
                    "msrp_aud_max": 30200,
                    "fuel_consumption_l_100km": 3.3,
                    "kerb_weight_kg": 1085,
                    "standard_features": ["Toyota Safety Sense with centre airbag", "8-inch touchscreen", "Apple CarPlay & Android Auto", "LED headlamps (SX)"],
                    "notes": "Sub-4.0L/100km real-world hybrid economy."
                },
                {
                    "badge_name": "GR Yaris & GR Yaris Rallye",
                    "years": {"start": 2020, "end": "Present"},
                    "body_styles": ["3-door Performance Hatch"],
                    "drivetrain": "GR-FOUR All-Wheel Drive",
                    "transmissions": ["6-speed intelligent manual (iMT)"],
                    "msrp_aud_min": 49500,
                    "msrp_aud_max": 54500,
                    "fuel_consumption_l_100km": 7.6,
                    "kerb_weight_kg": 1280,
                    "standard_features": ["GR-FOUR AWD with Normal/Sport/Track modes", "Front and rear Torsen LSDs (Rallye)", "Forged BBS 18-inch wheels", "Michelin Pilot Sport 4S tyres", "Circuit suspension tune", "Carbon composite roof"],
                    "notes": "250-unit Australian Rallye edition and 1,000 launch cars sold out instantly; Australian performance legend."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GR Yaris Rallye AWD",
                    "body_style": "3-door Performance Hatch",
                    "engine_code": "G16E-GTS",
                    "transmission": "6-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 2021,
                    "years_end": "Present",
                    "msrp_aud": 54500,
                    "power_kw": 200.0,
                    "torque_nm": 370.0,
                    "fuel_l_100km": 7.6,
                    "towing_braked_kg": 0,
                    "notes": "0-100 km/h in 5.2 seconds; dual Torsen limited-slip differentials."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}
