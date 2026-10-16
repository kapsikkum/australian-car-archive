"""Wave 2 Mazda deep-dive models: MX-5, CX-5, RX-3 / 808, 626 / Mazda6."""

MX5_MODEL = {
    "make_slug": "mazda",
    "model_slug": "mx-5",
    "name": "MX-5",
    "vehicle_type": "Roadster / Convertible",
    "segment": "Sports Car",
    "years_sold_au": {"start": 1989, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mazda MX-5 is the world's best-selling two-seater sports car and an icon of pure driving pleasure in Australia. Embodying the philosophy of 'Jinba Ittai' (horse and rider as one), the MX-5 revived the classic British roadster concept with Japanese reliability, near-perfect 50:50 weight distribution, and rear-wheel-drive purity.",
    "australian_market_notes": "Launched in Australia in October 1989, the NA MX-5 was crowned 1989 Wheels Car of the Year, sparking an Australian roadster renaissance. Across four generations, Australian buyers received exclusive special editions, including the Australia-only factory turbocharged MX-5 SE (NB8C) in 2004, the Power Retractable Hard Top (PRHT) NC, and the ND which captured the 2016 Wheels Car of the Year award.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "NA",
            "generation_name": "MX-5 1st Generation",
            "years": {"start": 1989, "end": 1997},
            "body_styles": ["2-door Roadster"],
            "platform": "Mazda NA",
            "ancap_rating": "Untested",
            "summary": "1989 Wheels Car of the Year. Iconic pop-up headlights, manual soft-top, double-wishbone suspension at all four corners, and free-revving 1.6L and 1.8L DOHC 16-valve engines.",
            "engines": [
                {
                    "engine_code": "B6-ZE",
                    "name": "Mazda B6-ZE 1.6L DOHC",
                    "displacement_cc": 1597,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 85.0,
                    "power_rpm": "6500",
                    "torque_nm": 137.0,
                    "torque_rpm": "5500",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Original NA6CE powerplant featuring light flywheel and tuned exhaust note."
                },
                {
                    "engine_code": "BP-ZE",
                    "name": "Mazda BP-ZE 1.8L DOHC",
                    "displacement_cc": 1839,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 96.0,
                    "power_rpm": "6500",
                    "torque_nm": 150.0,
                    "torque_rpm": "5500",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Introduced in 1994 NA8C with larger disc brakes and chassis bracing."
                }
            ],
            "badges": [
                {
                    "badge_name": "Base Roadster",
                    "years": {"start": 1989, "end": 1997},
                    "body_styles": ["2-door Roadster"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 29990,
                    "msrp_aud_max": 38990,
                    "fuel_consumption_l_100km": 7.8,
                    "kerb_weight_kg": 950,
                    "standard_features": ["Pop-up headlights", "14-inch 'daisy' alloy wheels", "Vinyl manual folding soft-top", "Momo steering wheel (early)"],
                    "notes": "Lightweight 950kg sports roadster."
                },
                {
                    "badge_name": "Clubman",
                    "years": {"start": 1994, "end": 1997},
                    "body_styles": ["2-door Roadster"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 42000,
                    "fuel_consumption_l_100km": 8.0,
                    "kerb_weight_kg": 990,
                    "standard_features": ["Bilstein shock absorbers", "Torsen limited-slip differential", "Rear lip spoiler", "De-powered steering option", "Stiffer springs"],
                    "notes": "Track-focused enthusiast special in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "MX-5 NA6 Manual",
                    "body_style": "2-door Roadster",
                    "engine_code": "B6-ZE",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1989,
                    "years_end": 1993,
                    "msrp_aud": 29990,
                    "power_kw": 85.0,
                    "torque_nm": 137.0,
                    "fuel_l_100km": 7.8,
                    "towing_braked_kg": 0,
                    "notes": "Original 1989 launch car; pure driving dynamics."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "NB",
            "generation_name": "MX-5 2nd Generation",
            "years": {"start": 1998, "end": 2005},
            "body_styles": ["2-door Roadster"],
            "platform": "Mazda NB",
            "ancap_rating": "Untested",
            "summary": "Fixed projector headlights, glass rear heated window, 6-speed manual, S-VT variable valve timing, and Australia's unique factory turbocharged MX-5 SE Turbo hero.",
            "engines": [
                {
                    "engine_code": "BP-Z3",
                    "name": "Mazda BP-Z3 1.8L S-VT",
                    "displacement_cc": 1839,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 106.0,
                    "power_rpm": "7000",
                    "torque_nm": 168.0,
                    "torque_rpm": "5500",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16-valve S-VT",
                    "notes": "Sequential valve timing on intake cam from late 2000 NB8B facelift."
                },
                {
                    "engine_code": "BP-Z3-Turbo",
                    "name": "Mazda BP-Z3 1.8L Turbo (MX-5 SE)",
                    "displacement_cc": 1839,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled (IHI RHF5)",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 150.0,
                    "power_rpm": "6500",
                    "torque_nm": 280.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Factory turbocharged model developed for Australia and North America (Mazdaspeed)."
                }
            ],
            "badges": [
                {
                    "badge_name": "Base / Classic",
                    "years": {"start": 1998, "end": 2005},
                    "body_styles": ["2-door Roadster"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "6-speed manual", "4-speed auto"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 44500,
                    "fuel_consumption_l_100km": 8.3,
                    "kerb_weight_kg": 1030,
                    "standard_features": ["15-inch alloy wheels", "Dual airbags", "Glass rear window with demister", "Power mirrors and windows", "Torsen LSD (manual)"],
                    "notes": "Refined second-generation roadster."
                },
                {
                    "badge_name": "SE Turbo",
                    "years": {"start": 2004, "end": 2005},
                    "body_styles": ["2-door Roadster"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed shot-peened manual"],
                    "msrp_aud_min": 45490,
                    "msrp_aud_max": 45490,
                    "fuel_consumption_l_100km": 9.1,
                    "kerb_weight_kg": 1105,
                    "standard_features": ["150kW turbo engine", "17-inch Racing Hart alloy wheels", "Bilstein sports suspension", "Bosch ABS", "Red/black leather sports seats", "Rear boot spoiler", "Large front air dam"],
                    "notes": "Australian performance icon; 0-100 km/h in 6.2s."
                }
            ],
            "configurations": [
                {
                    "badge_name": "MX-5 SE Turbo",
                    "body_style": "2-door Roadster",
                    "engine_code": "BP-Z3-Turbo",
                    "transmission": "6-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 2004,
                    "years_end": 2005,
                    "msrp_aud": 45490,
                    "power_kw": 150.0,
                    "torque_nm": 280.0,
                    "fuel_l_100km": 9.1,
                    "towing_braked_kg": 0,
                    "notes": "Only 206 factory turbocharged units sold in Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "NC",
            "generation_name": "MX-5 3rd Generation",
            "years": {"start": 2005, "end": 2015},
            "body_styles": ["2-door Roadster Soft-top", "2-door Roadster Coupe PRHT"],
            "platform": "Mazda NC",
            "ancap_rating": "4 stars",
            "summary": "2005 Wheels Car of the Year. Sized up to the RX-8 platform, powered by the 2.0L MZR engine, and introduced the world's fastest Power Retractable Hard Top (12 seconds).",
            "engines": [
                {
                    "engine_code": "LF-VE",
                    "name": "Mazda MZR LF-VE 2.0L",
                    "displacement_cc": 1999,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 118.0,
                    "power_rpm": "6700",
                    "torque_nm": 188.0,
                    "torque_rpm": "5000",
                    "compression_ratio": "10.8:1",
                    "valvetrain": "DOHC 16-valve S-VT",
                    "notes": "All-aluminium block; rev limiter raised to 7,500rpm on NC2 facelift with forged crankshaft."
                }
            ],
            "badges": [
                {
                    "badge_name": "Soft Top / Touring",
                    "years": {"start": 2005, "end": 2015},
                    "body_styles": ["2-door Roadster"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "6-speed activematic auto"],
                    "msrp_aud_min": 41865,
                    "msrp_aud_max": 46990,
                    "fuel_consumption_l_100km": 8.1,
                    "kerb_weight_kg": 1105,
                    "standard_features": ["17-inch alloy wheels", "Bose premium audio", "Leather upholstery (Touring)", "Limited slip differential (manual)", "DSC stability control"],
                    "notes": "2005 Wheels COTY winner."
                },
                {
                    "badge_name": "Roadster Coupe (PRHT)",
                    "years": {"start": 2006, "end": 2015},
                    "body_styles": ["2-door Roadster Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "6-speed auto"],
                    "msrp_aud_min": 45490,
                    "msrp_aud_max": 51990,
                    "fuel_consumption_l_100km": 8.1,
                    "kerb_weight_kg": 1142,
                    "standard_features": ["Electric folding hardtop (12 seconds)", "Bose 7-speaker audio", "17-inch alloys", "Leather seats", "Chrome accents"],
                    "notes": "Accounted for over 70% of Australian NC sales."
                }
            ],
            "configurations": [
                {
                    "badge_name": "MX-5 Roadster Coupe PRHT Manual",
                    "body_style": "2-door Roadster Coupe",
                    "engine_code": "LF-VE",
                    "transmission": "6-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 2006,
                    "years_end": 2015,
                    "msrp_aud": 47990,
                    "power_kw": 118.0,
                    "torque_nm": 188.0,
                    "fuel_l_100km": 8.1,
                    "towing_braked_kg": 0,
                    "notes": "Fastest folding hardtop of its era."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "ND",
            "generation_name": "MX-5 4th Generation",
            "years": {"start": 2015, "end": "Present"},
            "body_styles": ["2-door Roadster Soft-top", "2-door Targa RF (Retractable Fastback)"],
            "platform": "Mazda ND",
            "ancap_rating": "5 stars",
            "summary": "2016 Wheels Car of the Year. Gram strategy shedding 100kg down to 1,005kg, SKYACTIV-G engines (1.5L and 2.0L upgraded to 135kW in ND2), and stunning RF fastback.",
            "engines": [
                {
                    "engine_code": "P5-VP",
                    "name": "Mazda SKYACTIV-G 1.5L",
                    "displacement_cc": 1496,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 96.0,
                    "power_rpm": "7000",
                    "torque_nm": 150.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve Dual S-VT",
                    "notes": "Sweet-revving high-compression 1.5L engine in early entry models."
                },
                {
                    "engine_code": "PE-VPR",
                    "name": "Mazda SKYACTIV-G 2.0L (ND2)",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 135.0,
                    "power_rpm": "7000",
                    "torque_nm": 205.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve Dual S-VT",
                    "notes": "ND2 upgrade featuring lighter pistons, larger throttle body, dual-mass flywheel, and 7,500rpm redline."
                }
            ],
            "badges": [
                {
                    "badge_name": "Roadster / GT",
                    "years": {"start": 2015, "end": "Present"},
                    "body_styles": ["2-door Roadster"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 31990,
                    "msrp_aud_max": 44990,
                    "fuel_consumption_l_100km": 6.8,
                    "kerb_weight_kg": 1035,
                    "standard_features": ["LED headlights", "MZD Connect touchscreen", "Limited slip differential (manual)", "Bose 9-speaker audio (GT)", "Heated leather seats (GT)"],
                    "notes": "2016 Wheels COTY award winner."
                },
                {
                    "badge_name": "RF / RF GT / GT RS",
                    "years": {"start": 2017, "end": "Present"},
                    "body_styles": ["2-door Targa RF"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 38550,
                    "msrp_aud_max": 51990,
                    "fuel_consumption_l_100km": 6.9,
                    "kerb_weight_kg": 1087,
                    "standard_features": ["Electric retractable targa roof", "Bilstein gas dampers (GT RS)", "Brembo 4-piston front brakes (GT RS)", "17-inch BBS forged alloys (GT RS)"],
                    "notes": "GT RS package adds factory track hardware."
                }
            ],
            "configurations": [
                {
                    "badge_name": "MX-5 RF GT RS Manual",
                    "body_style": "2-door Targa RF",
                    "engine_code": "PE-VPR",
                    "transmission": "6-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 2021,
                    "years_end": "Present",
                    "msrp_aud": 51990,
                    "power_kw": 135.0,
                    "torque_nm": 205.0,
                    "fuel_l_100km": 6.9,
                    "towing_braked_kg": 0,
                    "notes": "Equipped with Brembo brakes and Bilstein suspension."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

CX5_MODEL = {
    "make_slug": "mazda",
    "model_slug": "cx-5",
    "name": "CX-5",
    "vehicle_type": "Medium SUV",
    "segment": "Medium SUV",
    "years_sold_au": {"start": 2012, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mazda CX-5 is one of Australia's all-time most popular SUVs, holding the title of best-selling SUV in the country outright for multiple consecutive years. Debuting Mazda's SKYACTIV powertrain suite and Kodo 'Soul of Motion' design language, the CX-5 elevated the mid-size family crossover segment with class-leading steering feel, premium interiors, and punchy turbo power.",
    "australian_market_notes": "Launched in March 2012, the CX-5 quickly dislodged long-time incumbents like the Toyota RAV4 and Subaru Forester from top spot. Australian models benefited from continuous refinements, including local ride calibrations, the introduction of the 170kW/420Nm 2.5-litre Turbo engine, and the luxurious Akera and sporty GT SP grades.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "KE",
            "generation_name": "CX-5 1st Generation",
            "years": {"start": 2012, "end": "2017"},
            "body_styles": ["5-door SUV"],
            "platform": "Mazda Skyactiv-Chassis",
            "ancap_rating": "5 stars",
            "summary": "First full SKYACTIV model featuring high-tensile steel, 2.0L & 2.5L petrol engines, and a torquey 2.2L twin-turbo diesel returning 5.7L/100km.",
            "engines": [
                {
                    "engine_code": "PE-VPS",
                    "name": "Mazda SKYACTIV-G 2.0L",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 114.0,
                    "power_rpm": "6000",
                    "torque_nm": 200.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve Dual S-VT",
                    "notes": "Standard front-wheel-drive powertrain."
                },
                {
                    "engine_code": "PY-VPS",
                    "name": "Mazda SKYACTIV-G 2.5L",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 138.0,
                    "power_rpm": "5700",
                    "torque_nm": 250.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve Dual S-VT",
                    "notes": "Added in early 2013 for all AWD petrol models."
                },
                {
                    "engine_code": "SH-VPTS",
                    "name": "Mazda SKYACTIV-D 2.2L Twin-Turbo Diesel",
                    "displacement_cc": 2191,
                    "displacement_litres": 2.2,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Sequential Twin-Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 129.0,
                    "power_rpm": "4500",
                    "torque_nm": 420.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "14.0:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "World's lowest compression diesel ratio for rapid revving."
                }
            ],
            "badges": [
                {
                    "badge_name": "Maxx",
                    "years": {"start": 2012, "end": 2017},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 27800,
                    "msrp_aud_max": 33990,
                    "fuel_consumption_l_100km": 6.4,
                    "kerb_weight_kg": 1445,
                    "standard_features": ["17-inch steel wheels", "Reversing camera", "5.8-inch touchscreen", "Push button start", "6 airbags"],
                    "notes": "Huge value entry model."
                },
                {
                    "badge_name": "Maxx Sport",
                    "years": {"start": 2012, "end": 2017},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 33540,
                    "msrp_aud_max": 39470,
                    "fuel_consumption_l_100km": 6.9,
                    "kerb_weight_kg": 1510,
                    "standard_features": ["17-inch alloy wheels", "Dual-zone climate control", "Satellite navigation", "Auto headlights & wipers", "Front fog lamps"],
                    "notes": "The volume seller of the CX-5 range."
                },
                {
                    "badge_name": "Akera",
                    "years": {"start": 2012, "end": 2017},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "AWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 45770,
                    "msrp_aud_max": 50610,
                    "fuel_consumption_l_100km": 5.7,
                    "kerb_weight_kg": 1630,
                    "standard_features": ["19-inch alloys", "Leather seats", "Sunroof", "Bose audio", "Blind spot monitoring", "High beam control"],
                    "notes": "Luxury AWD flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "CX-5 Maxx Sport AWD 2.5",
                    "body_style": "5-door SUV",
                    "engine_code": "PY-VPS",
                    "transmission": "6-speed automatic",
                    "drivetrain": "AWD",
                    "years_start": 2013,
                    "years_end": 2017,
                    "msrp_aud": 36620,
                    "power_kw": 138.0,
                    "torque_nm": 250.0,
                    "fuel_l_100km": 7.4,
                    "towing_braked_kg": 1800,
                    "notes": "Australia's favorite SUV configuration."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "KF",
            "generation_name": "CX-5 2nd Generation",
            "years": {"start": 2017, "end": "Present"},
            "body_styles": ["5-door SUV"],
            "platform": "Mazda Skyactiv-Chassis II",
            "ancap_rating": "5 stars",
            "summary": "Sophisticated styling with Soul Red Crystal paint, G-Vectoring Control Plus, luxury Akera trim with Nappa leather, and the 170kW/420Nm 2.5-litre turbo engine.",
            "engines": [
                {
                    "engine_code": "PY-VPS-Gen2",
                    "name": "Mazda SKYACTIV-G 2.5L Cylinder Deactivation",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 140.0,
                    "power_rpm": "6000",
                    "torque_nm": 252.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve Dual S-VT",
                    "notes": "Equipped with cylinder deactivation cruising on 2 cylinders."
                },
                {
                    "engine_code": "PY-VPTS",
                    "name": "Mazda SKYACTIV-G 2.5T Dynamic Pressure Turbo",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 170.0,
                    "power_rpm": "5000",
                    "torque_nm": 420.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16-valve Dual S-VT",
                    "notes": "Flagship turbo engine with 420Nm torque at just 2,000rpm."
                }
            ],
            "badges": [
                {
                    "badge_name": "Maxx Sport",
                    "years": {"start": 2017, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 34390,
                    "msrp_aud_max": 42500,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 1575,
                    "standard_features": ["17-inch alloys", "Apple CarPlay & Android Auto", "Rear air vents", "Dual-zone climate control", "Blind spot monitoring", "Smart city brake support"],
                    "notes": "Consistent best-seller."
                },
                {
                    "badge_name": "GT SP Turbo",
                    "years": {"start": 2021, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "i-ACTIV AWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 51590,
                    "msrp_aud_max": 54500,
                    "fuel_consumption_l_100km": 8.2,
                    "kerb_weight_kg": 1720,
                    "standard_features": ["170kW 2.5T turbo engine", "19-inch gloss black alloys", "Black exterior accents", "Red stitching interior", "Bose 10-speaker audio"],
                    "notes": "Performance-themed family crossover."
                },
                {
                    "badge_name": "Akera Turbo",
                    "years": {"start": 2018, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "i-ACTIV AWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 53590,
                    "msrp_aud_max": 55500,
                    "fuel_consumption_l_100km": 8.2,
                    "kerb_weight_kg": 1735,
                    "standard_features": ["Chroma brown Nappa leather", "Ventilated front seats", "Real Sen wood inserts", "360-degree camera", "Adaptive LED headlamps"],
                    "notes": "Executive luxury flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "CX-5 GT SP 2.5T AWD",
                    "body_style": "5-door SUV",
                    "engine_code": "PY-VPTS",
                    "transmission": "6-speed automatic",
                    "drivetrain": "AWD",
                    "years_start": 2021,
                    "years_end": "Present",
                    "msrp_aud": 51590,
                    "power_kw": 170.0,
                    "torque_nm": 420.0,
                    "fuel_l_100km": 8.2,
                    "towing_braked_kg": 2000,
                    "notes": "0-100 km/h in 7.7 seconds with 420Nm torque."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

RX3_808_MODEL = {
    "make_slug": "mazda",
    "model_slug": "rx-3-808",
    "name": "RX-3 / 808",
    "vehicle_type": "Rotary / Piston Coupe & Sedan",
    "segment": "Sports Coupe / Small Car",
    "years_sold_au": {"start": 1972, "end": 1978},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mazda RX-3 (Savanna) and its reciprocating-piston sister the Mazda 808 (Grand Familia) are iconic pillars of Australian motorsport history and Japanese performance folklore. Famed for taking the fight directly to Holden Torana GTR XU-1s and Ford Falcon GT-HOs at Mount Panorama Bathurst, the RX-3's screaming twin-rotor Wankel rotary engine won legions of fanatical followers.",
    "australian_market_notes": "Introduced in March 1972, the RX-3 was sold alongside the cheaper, conventional four-cylinder 808. In motorsport, the RX-3 proved an unbeatable giant-killer in the under-3.0-litre class at the Bathurst 1000, claiming a historic 1st, 2nd, and 3rd in class in 1975 led by Don Holland. Surviving authentic RX-3 Coupes command extraordinary auction values across Australia today.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "S102A/S124A",
            "generation_name": "RX-3 Series I, II & III",
            "years": {"start": 1972, "end": 1978},
            "body_styles": ["2-door Coupe", "4-door Sedan", "5-door Station Wagon"],
            "platform": "Mazda S-platform",
            "ancap_rating": "Untested",
            "summary": "Rotary-powered icon. Series I (10A twin-rotor), Series II (12A single distributor with pointed nose), and Series III (spoilers and updated dash). 1975 Bathurst class dominator.",
            "engines": [
                {
                    "engine_code": "10A",
                    "name": "Mazda 10A Twin-Rotor Rotary",
                    "displacement_cc": 982,
                    "displacement_litres": 1.0,
                    "cylinders": 2,
                    "configuration": "Rotary (2-Rotor)",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 82.0,
                    "power_rpm": "7000",
                    "torque_nm": 135.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "Rotary Ports",
                    "notes": "Twin rotor 491cc x 2 with dual distributors in Series I."
                },
                {
                    "engine_code": "12A",
                    "name": "Mazda 12A Twin-Rotor Rotary",
                    "displacement_cc": 1146,
                    "displacement_litres": 1.1,
                    "cylinders": 2,
                    "configuration": "Rotary (2-Rotor)",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 97.0,
                    "power_rpm": "7000",
                    "torque_nm": 157.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "Rotary Ports",
                    "notes": "Larger 573cc x 2 rotors introduced in Series II (1974) with single distributor."
                }
            ],
            "badges": [
                {
                    "badge_name": "RX-3 Coupe",
                    "years": {"start": 1972, "end": 1978},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual", "5-speed manual", "3-speed automatic"],
                    "msrp_aud_min": 3299,
                    "msrp_aud_max": 4890,
                    "fuel_consumption_l_100km": 12.5,
                    "kerb_weight_kg": 885,
                    "standard_features": ["High-back bucket seats", "Wood-rim steering wheel", "Sports instruments with 7000rpm redline tachometer", "Front disc brakes", "Hexagonal tail-lights (Coupe)"],
                    "notes": "Highly prized collector car in Australia."
                },
                {
                    "badge_name": "RX-3 Sedan / Wagon",
                    "years": {"start": 1972, "end": 1976},
                    "body_styles": ["4-door Sedan", "5-door Station Wagon"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual", "3-speed auto"],
                    "msrp_aud_min": 3150,
                    "msrp_aud_max": 4350,
                    "fuel_consumption_l_100km": 12.5,
                    "kerb_weight_kg": 905,
                    "standard_features": ["4 doors", "Vinyl seats", "Centre console", "Heater/demister"],
                    "notes": "Sedan and rare rotary wagon."
                }
            ],
            "configurations": [
                {
                    "badge_name": "RX-3 Coupe 12A",
                    "body_style": "2-door Coupe",
                    "engine_code": "12A",
                    "transmission": "4-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1974,
                    "years_end": 1978,
                    "msrp_aud": 4290,
                    "power_kw": 97.0,
                    "torque_nm": 157.0,
                    "fuel_l_100km": 12.5,
                    "towing_braked_kg": 750,
                    "notes": "Iconic Australian touring car racer."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "STC/SN3A",
            "generation_name": "Mazda 808 (Grand Familia)",
            "years": {"start": 1972, "end": 1977},
            "body_styles": ["2-door Coupe", "4-door Sedan", "5-door Station Wagon"],
            "platform": "Mazda S-platform",
            "ancap_rating": "Untested",
            "summary": "Piston-engine brother of the RX-3. Shared body panels with rectangular headlights, powered by conventional 1.3L and 1.6L 4-cylinder reciprocating engines.",
            "engines": [
                {
                    "engine_code": "TC",
                    "name": "Mazda TC 1.3L OHC",
                    "displacement_cc": 1272,
                    "displacement_litres": 1.3,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 54.0,
                    "power_rpm": "6000",
                    "torque_nm": 92.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "9.2:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Economy piston engine."
                },
                {
                    "engine_code": "NA",
                    "name": "Mazda NA 1.6L OHC",
                    "displacement_cc": 1586,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 60.0,
                    "power_rpm": "5500",
                    "torque_nm": 115.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "8.6:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Offered in 808 Super Deluxe."
                }
            ],
            "badges": [
                {
                    "badge_name": "808 Deluxe / Super Deluxe",
                    "years": {"start": 1972, "end": 1977},
                    "body_styles": ["Coupe", "Sedan", "Station Wagon"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual", "3-speed automatic"],
                    "msrp_aud_min": 2490,
                    "msrp_aud_max": 3490,
                    "fuel_consumption_l_100km": 8.4,
                    "kerb_weight_kg": 855,
                    "standard_features": ["Single rectangular headlights", "Vinyl interior", "Heater/demister", "Push-button radio"],
                    "notes": "Affordable small car widely converted into RX-3 rotary replicas today."
                }
            ],
            "configurations": [
                {
                    "badge_name": "808 Sedan 1300",
                    "body_style": "4-door Sedan",
                    "engine_code": "TC",
                    "transmission": "4-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1972,
                    "years_end": 1977,
                    "msrp_aud": 2690,
                    "power_kw": 54.0,
                    "torque_nm": 92.0,
                    "fuel_l_100km": 8.4,
                    "towing_braked_kg": 700,
                    "notes": "Piston family runabout."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

MAZDA_626_6_MODEL = {
    "make_slug": "mazda",
    "model_slug": "626-mazda6",
    "name": "626 / Mazda6",
    "vehicle_type": "Sedan / Hatchback / Wagon",
    "segment": "Medium Car",
    "years_sold_au": {"start": 1979, "end": 2024},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mazda 626 and its successor the Mazda6 served as Australia's benchmark mid-size Japanese passenger car for 45 years. From the 1983 Wheels Car of the Year winning front-wheel drive 626 GC to the ferocious 190kW Mazda6 MPS turbocharged all-wheel-drive performance hero, it balanced executive styling with dynamic driver engagement.",
    "australian_market_notes": "First imported as the rear-drive 626 CB in 1979, the model soared to acclaim with the 1983 GC series, which took Wheels Car of the Year. In 2002, the nameplate reinvented itself as the sleek Mazda6 (GG), winning universal accolades. In 2005, Mazda unleashed the Mazda6 MPS with a 2.3L turbo engine and active-torque AWD to rival Subaru's Liberty GT. Production concluded in 2024 with the 20th Anniversary Edition.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "CB/GC/GD/GE/GF",
            "generation_name": "Mazda 626 (5 Generations)",
            "years": {"start": 1979, "end": 2002},
            "body_styles": ["4-door Sedan", "5-door Hatch", "2-door Coupe", "5-door Wagon"],
            "platform": "Mazda CB / GC / GD / GE / GF",
            "ancap_rating": "Untested",
            "summary": "Classic 626 heritage. The 1983 GC won Wheels Car of the Year, followed by the turbo 2.2L GD, sleek V6-powered GE, and dependable GF series.",
            "engines": [
                {
                    "engine_code": "FE",
                    "name": "Mazda FE 2.0L OHC",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 74.0,
                    "power_rpm": "5500",
                    "torque_nm": 153.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "8.6:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "1983 Wheels COTY winning engine in GC series."
                },
                {
                    "engine_code": "F2T",
                    "name": "Mazda F2T 2.2L Turbo",
                    "displacement_cc": 2184,
                    "displacement_litres": 2.2,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 108.0,
                    "power_rpm": "4700",
                    "torque_nm": 258.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "7.8:1",
                    "valvetrain": "SOHC 12-valve",
                    "notes": "Fitted to the rare GD Turbo with 4-wheel steering."
                },
                {
                    "engine_code": "KL-DE",
                    "name": "Mazda KL-DE 2.5L 24V DOHC V6",
                    "displacement_cc": 2497,
                    "displacement_litres": 2.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 121.0,
                    "power_rpm": "5500",
                    "torque_nm": 217.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "9.2:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "Silky V6 in 1990s GE series."
                }
            ],
            "badges": [
                {
                    "badge_name": "Super Saloon / Ghia / Limited",
                    "years": {"start": 1983, "end": 2002},
                    "body_styles": ["Sedan", "Hatch", "Coupe", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 11990,
                    "msrp_aud_max": 38990,
                    "fuel_consumption_l_100km": 8.8,
                    "kerb_weight_kg": 1180,
                    "standard_features": ["Velour trim", "Power windows", "Air conditioning", "Alloy wheels", "Cruise control"],
                    "notes": "Wheels COTY winner in 1983."
                }
            ],
            "configurations": [
                {
                    "badge_name": "626 Super Saloon 2.0",
                    "body_style": "5-door Hatch",
                    "engine_code": "FE",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1983,
                    "years_end": 1987,
                    "msrp_aud": 13990,
                    "power_kw": 74.0,
                    "torque_nm": 153.0,
                    "fuel_l_100km": 8.5,
                    "towing_braked_kg": 1000,
                    "notes": "1983 Wheels Car of the Year winner."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "GG/GY",
            "generation_name": "Mazda6 1st Generation & MPS",
            "years": {"start": 2002, "end": 2008},
            "body_styles": ["4-door Sedan", "5-door Hatch", "5-door Wagon"],
            "platform": "Mazda GG",
            "ancap_rating": "4 stars",
            "summary": "Replaced 626 with dynamic 'Zoom-Zoom' styling, double-wishbone front suspension, and spawned the 190kW turbo AWD Mazda6 MPS performance hero.",
            "engines": [
                {
                    "engine_code": "L3-VE",
                    "name": "Mazda MZR L3-VE 2.3L",
                    "displacement_cc": 2261,
                    "displacement_litres": 2.3,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 122.0,
                    "power_rpm": "6500",
                    "torque_nm": 207.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.6:1",
                    "valvetrain": "DOHC 16-valve S-VT",
                    "notes": "Standard engine in Classic, Luxury, and Luxury Sports."
                },
                {
                    "engine_code": "L3-VDT",
                    "name": "Mazda MZR 2.3L DISI Turbo (MPS)",
                    "displacement_cc": 2261,
                    "displacement_litres": 2.3,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 190.0,
                    "power_rpm": "5500",
                    "torque_nm": 380.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve Direct Injection",
                    "notes": "Direct injection spark ignition turbo with top-mount intercooler and bonnet power bulge."
                }
            ],
            "badges": [
                {
                    "badge_name": "Classic / Luxury / Luxury Sports",
                    "years": {"start": 2002, "end": 2008},
                    "body_styles": ["Sedan", "Hatch", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "6-speed manual", "4-speed auto", "5-speed auto"],
                    "msrp_aud_min": 28490,
                    "msrp_aud_max": 42000,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 1390,
                    "standard_features": ["16-inch or 17-inch alloys", "Climate control", "Leather seats (Luxury)", "Bose 7-speaker audio", "Sports body kit (Sports)"],
                    "notes": "Massive Australian sales hit."
                },
                {
                    "badge_name": "MPS (Mazda Performance Series)",
                    "years": {"start": 2005, "end": 2007},
                    "body_styles": ["4-door Sedan"],
                    "drivetrain": "Active Torque Split AWD",
                    "transmissions": ["6-speed manual"],
                    "msrp_aud_min": 48600,
                    "msrp_aud_max": 54600,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1620,
                    "standard_features": ["190kW DISI turbo engine", "Active torque split AWD with rear LSD", "18-inch 15-spoke alloys", "Brembo-developed ventilated brakes", "Leather sports seats", "Bonnet scoop ducting"],
                    "notes": "Cult performance sedan rivaling Subaru Liberty GT; 0-100 km/h in 6.6s."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Mazda6 MPS AWD",
                    "body_style": "4-door Sedan",
                    "engine_code": "L3-VDT",
                    "transmission": "6-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 2005,
                    "years_end": 2007,
                    "msrp_aud": 48600,
                    "power_kw": 190.0,
                    "torque_nm": 380.0,
                    "fuel_l_100km": 10.5,
                    "towing_braked_kg": 1400,
                    "notes": "190kW turbocharged AWD sports sedan."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "GH",
            "generation_name": "Mazda6 2nd Generation",
            "years": {"start": 2008, "end": 2012},
            "body_styles": ["4-door Sedan", "5-door Hatch", "5-door Wagon"],
            "platform": "Mazda GH",
            "ancap_rating": "5 stars",
            "summary": "Aerodynamic coupe-like silhouette, upgraded 2.5L engine, and high-torque 2.2L MZR-CD turbodiesel with 400Nm.",
            "engines": [
                {
                    "engine_code": "L5-VE",
                    "name": "Mazda MZR L5-VE 2.5L",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 125.0,
                    "power_rpm": "6000",
                    "torque_nm": 226.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.7:1",
                    "valvetrain": "DOHC 16-valve S-VT",
                    "notes": "Torquey 2.5-litre four cylinder."
                },
                {
                    "engine_code": "R2AA",
                    "name": "Mazda MZR-CD 2.2L Turbo Diesel",
                    "displacement_cc": 2184,
                    "displacement_litres": 2.2,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 136.0,
                    "power_rpm": "3500",
                    "torque_nm": 400.0,
                    "torque_rpm": "1800-3000",
                    "compression_ratio": "16.3:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "400Nm of torque returning 5.9L/100km."
                }
            ],
            "badges": [
                {
                    "badge_name": "Classic / Luxury / Sports Luxury",
                    "years": {"start": 2008, "end": 2012},
                    "body_styles": ["Sedan", "Hatch", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "5-speed automatic"],
                    "msrp_aud_min": 29740,
                    "msrp_aud_max": 43500,
                    "fuel_consumption_l_100km": 8.7,
                    "kerb_weight_kg": 1450,
                    "standard_features": ["17 or 18-inch alloys", "6 airbags", "Dynamic stability control", "Dual-zone climate control", "Bi-xenon headlights (Sports)"],
                    "notes": "5-star ANCAP safety across range."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Mazda6 Diesel Sports Hatch",
                    "body_style": "5-door Hatch",
                    "engine_code": "R2AA",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2008,
                    "years_end": 2012,
                    "msrp_aud": 39690,
                    "power_kw": 136.0,
                    "torque_nm": 400.0,
                    "fuel_l_100km": 5.9,
                    "towing_braked_kg": 1500,
                    "notes": "400Nm turbo diesel performance hatch."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "GJ/GL",
            "generation_name": "Mazda6 3rd Generation",
            "years": {"start": 2012, "end": 2024},
            "body_styles": ["4-door Sedan", "5-door Wagon"],
            "platform": "Mazda Skyactiv-Chassis",
            "ancap_rating": "5 stars",
            "summary": "12-year tour-de-force featuring Kodo design, SKYACTIV engines, i-ELOOP brake energy regeneration, 170kW 2.5T turbo, and 20th Anniversary Edition.",
            "engines": [
                {
                    "engine_code": "PY-VPR",
                    "name": "Mazda SKYACTIV-G 2.5L",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 140.0,
                    "power_rpm": "6000",
                    "torque_nm": 252.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve Dual S-VT",
                    "notes": "High compression petrol engine."
                },
                {
                    "engine_code": "PY-VPTS-6",
                    "name": "Mazda SKYACTIV-G 2.5T Turbo",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 170.0,
                    "power_rpm": "5000",
                    "torque_nm": 420.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 16-valve Dual S-VT",
                    "notes": "420Nm turbo engine added in 2018."
                }
            ],
            "badges": [
                {
                    "badge_name": "Sport / Touring",
                    "years": {"start": 2012, "end": 2024},
                    "body_styles": ["Sedan", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 33490,
                    "msrp_aud_max": 41500,
                    "fuel_consumption_l_100km": 7.0,
                    "kerb_weight_kg": 1520,
                    "standard_features": ["17-inch alloys", "MZD Connect touchscreen", "Blind spot monitoring", "Autonomous emergency braking", "LED headlamps"],
                    "notes": "Refined executive family cruiser."
                },
                {
                    "badge_name": "GT SP / Atenza / 20th Anniversary",
                    "years": {"start": 2012, "end": 2024},
                    "body_styles": ["Sedan", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 45490,
                    "msrp_aud_max": 54635,
                    "fuel_consumption_l_100km": 7.6,
                    "kerb_weight_kg": 1610,
                    "standard_features": ["19-inch alloys", "Nappa leather upholstery", "11-speaker Bose audio", "Sunroof", "Ventilated front seats", "Head-up display"],
                    "notes": "Celebrated 20th Anniversary Edition in Artisan Red closed out production in 2024."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Mazda6 Atenza 2.5T Sedan",
                    "body_style": "4-door Sedan",
                    "engine_code": "PY-VPTS-6",
                    "transmission": "6-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 2018,
                    "years_end": 2024,
                    "msrp_aud": 51890,
                    "power_kw": 170.0,
                    "torque_nm": 420.0,
                    "fuel_l_100km": 7.6,
                    "towing_braked_kg": 1600,
                    "notes": "170kW / 420Nm luxury executive sedan."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}
