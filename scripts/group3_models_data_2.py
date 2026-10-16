"""
Deep-dive models 8 to 14 for Australian Car Archive Group 3
"""
from typing import Dict, Any

DEEP_DIVE_MODELS_PART2: Dict[str, Dict[str, Any]] = {
    "tesla/model-3": {
        "make_slug": "tesla",
        "model_slug": "model-3",
        "name": "Model 3",
        "vehicle_type": "Sedan",
        "segment": "Medium Electric Car",
        "years_sold_au": {"start": 2019, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The electric vehicle that opened the floodgates for mass EV adoption in Australia. Built in Shanghai for the Australian market, the Model 3 transformed automotive sales by outselling traditional petrol luxury sedans like the BMW 3 Series and Mercedes C-Class.",
        "australian_market_notes": "First delivered in Australia in August 2019. Rapidly captured top spots in state and federal vehicle sales charts, aided by State government electric vehicle rebates and federal FBT exemptions. The 'Highland' facelift arrived in late 2023, introducing superior sound isolation, ventilated seats, and revised suspension tuning.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Model-3-Pre-Highland",
                "generation_name": "Model 3 (Original & Refresh)",
                "years": {"start": 2019, "end": "2023"},
                "body_styles": ["4-door sedan"],
                "platform": "Tesla Model 3 platform",
                "ancap_rating": "5 stars",
                "summary": "Original launch model with glass roof, 15-inch landscape touchscreen, heat pump (from 2021), and LFP battery transition for Standard Range Plus / RWD.",
                "engines": [
                    {
                        "engine_code": "3D1/3D6 Rear Motor",
                        "name": "Single Permanent Magnet Rear Motor",
                        "displacement_cc": 0,
                        "displacement_litres": 0.0,
                        "cylinders": 0,
                        "configuration": "Single Electric Motor",
                        "aspiration": "Electric",
                        "fuel_type": "Electric",
                        "power_kw": 208,
                        "power_rpm": "Electric",
                        "torque_nm": 420,
                        "torque_rpm": "0-4000",
                        "compression_ratio": "N/A",
                        "valvetrain": "N/A",
                        "notes": "Paired with 60kWh LFP (Lithium Iron Phosphate) battery pack built in Giga Shanghai."
                    },
                    {
                        "engine_code": "Dual Motor Performance",
                        "name": "Dual Electric Motors (Performance)",
                        "displacement_cc": 0,
                        "displacement_litres": 0.0,
                        "cylinders": 0,
                        "configuration": "Dual Electric Motors",
                        "aspiration": "Electric",
                        "fuel_type": "Electric",
                        "power_kw": 357,
                        "power_rpm": "Electric",
                        "torque_nm": 660,
                        "torque_rpm": "0-5000",
                        "compression_ratio": "N/A",
                        "valvetrain": "N/A",
                        "notes": "Induction motor front and permanent magnet motor rear; 82kWh nickel-manganese-cobalt battery pack."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "RWD (Standard Range)",
                        "years": {"start": 2019, "end": "2023"},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["Single-speed reduction gear"],
                        "msrp_aud_min": 57400,
                        "msrp_aud_max": 66900,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 1752,
                        "standard_features": ["15-inch touchscreen", "Panoramic glass roof", "Autopilot suite", "Power tailgate", "Wireless phone charging pads", "Heated front and rear seats"],
                        "notes": "491km WLTP range; Australia's top-selling EV."
                    },
                    {
                        "badge_name": "Performance AWD",
                        "years": {"start": 2019, "end": "2023"},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "AWD",
                        "transmissions": ["Single-speed reduction gear"],
                        "msrp_aud_min": 83400,
                        "msrp_aud_max": 99900,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 1844,
                        "standard_features": ["20-inch Uberturbine wheels", "Performance brakes with red callipers", "Carbon-fibre rear spoiler", "Lowered suspension", "Track Mode V2", "Aluminium pedals"],
                        "notes": "0-100 km/h in 3.3 seconds."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "RWD (Standard Range)",
                        "body_style": "4-door sedan",
                        "engine_code": "3D1/3D6 Rear Motor",
                        "transmission": "Single-speed reduction gear",
                        "drivetrain": "RWD",
                        "years_start": 2021,
                        "years_end": "2023",
                        "msrp_aud": 61900,
                        "power_kw": 208,
                        "torque_nm": 420,
                        "fuel_l_100km": 0.0,
                        "towing_braked_kg": 1000,
                        "notes": "60kWh LFP battery with 170kW DC Supercharging."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "Model-3-Highland",
                "generation_name": "Model 3 (Highland Update)",
                "years": {"start": 2023, "end": "Present"},
                "body_styles": ["4-door sedan"],
                "platform": "Tesla Model 3 Highland",
                "ancap_rating": "5 stars",
                "summary": "Highland redesign bringing 360-degree acoustic glass, rear 8-inch screen, ambient lighting, ventilated seats, deleted indicator stalks, and 343kW Performance with adaptive damping.",
                "engines": [
                    {
                        "engine_code": "Highland Performance Dual Motor",
                        "name": "Highland Performance Dual Electric Motors",
                        "displacement_cc": 0,
                        "displacement_litres": 0.0,
                        "cylinders": 0,
                        "configuration": "Dual Electric Motors",
                        "aspiration": "Electric",
                        "fuel_type": "Electric",
                        "power_kw": 343,
                        "power_rpm": "Electric",
                        "torque_nm": 741,
                        "torque_rpm": "0-6000",
                        "compression_ratio": "N/A",
                        "valvetrain": "N/A",
                        "notes": "Next-gen 4D2 rear drive unit; adaptive damping suspension."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "RWD Highland",
                        "years": {"start": 2023, "end": "Present"},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["Single-speed reduction gear"],
                        "msrp_aud_min": 58900,
                        "msrp_aud_max": 61900,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 1765,
                        "standard_features": ["Rear 8.0-inch passenger display", "Ventilated front seats", "Steering wheel buttons for indicators", "17-speaker audio system", "Blind-spot camera indicator LED", "513km WLTP range"],
                        "notes": "Benchmark aerodynamic drag coefficient of 0.219 Cd."
                    },
                    {
                        "badge_name": "Performance Highland",
                        "years": {"start": 2024, "end": "Present"},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "AWD",
                        "transmissions": ["Single-speed reduction gear"],
                        "msrp_aud_min": 80900,
                        "msrp_aud_max": 83900,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 1851,
                        "standard_features": ["Adaptive damping system", "Bespoke sports bucket seats", "20-inch Warp forged wheels", "Carbon-fibre front splitter and rear diffuser", "Track Mode V3"],
                        "notes": "0-100 km/h in 3.1 seconds; 528km range."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Performance Highland",
                        "body_style": "4-door sedan",
                        "engine_code": "Highland Performance Dual Motor",
                        "transmission": "Single-speed reduction gear",
                        "drivetrain": "AWD",
                        "years_start": 2024,
                        "years_end": "Present",
                        "msrp_aud": 80900,
                        "power_kw": 343,
                        "torque_nm": 741,
                        "fuel_l_100km": 0.0,
                        "towing_braked_kg": 1000,
                        "notes": "Adaptive damping with 3.1s 0-100 km/h."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "tesla/model-y": {
        "make_slug": "tesla",
        "model_slug": "model-y",
        "name": "Model Y",
        "vehicle_type": "SUV",
        "segment": "Medium Electric SUV",
        "years_sold_au": {"start": 2022, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "Australia's top-selling electric SUV and one of the highest-selling SUVs outright in Australia. Built on the Model 3 platform with a taller crossover body, 2,158 litres of total cargo storage, and class-leading electrical efficiency.",
        "australian_market_notes": "First customer deliveries commenced in Australia in June 2022. It immediately overwhelmed order banks, regularly exceeding 2,500 sales per month and taking the title of Australia's most popular luxury crossover.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Model-Y-Gen1",
                "generation_name": "Model Y First Generation",
                "years": {"start": 2022, "end": "Present"},
                "body_styles": ["5-door SUV"],
                "platform": "Tesla Model Y platform",
                "ancap_rating": "5 stars (98% adult occupant protection)",
                "summary": "Front and rear single-piece gigacastings, structural battery pack integration, 15-inch display, panoramic glass roof, RWD, Long Range AWD, and Performance AWD.",
                "engines": [
                    {
                        "engine_code": "3D7 Single Motor (RWD)",
                        "name": "Single Permanent Magnet Rear Motor",
                        "displacement_cc": 0,
                        "displacement_litres": 0.0,
                        "cylinders": 0,
                        "configuration": "Single Electric Motor",
                        "aspiration": "Electric",
                        "fuel_type": "Electric",
                        "power_kw": 220,
                        "power_rpm": "Electric",
                        "torque_nm": 420,
                        "torque_rpm": "0-4000",
                        "compression_ratio": "N/A",
                        "valvetrain": "N/A",
                        "notes": "Paired with 60kWh LFP battery pack; 455km WLTP range."
                    },
                    {
                        "engine_code": "Dual Motor Performance",
                        "name": "Dual Electric Motors (Performance AWD)",
                        "displacement_cc": 0,
                        "displacement_litres": 0.0,
                        "cylinders": 0,
                        "configuration": "Dual Electric Motors",
                        "aspiration": "Electric",
                        "fuel_type": "Electric",
                        "power_kw": 357,
                        "power_rpm": "Electric",
                        "torque_nm": 660,
                        "torque_rpm": "0-5000",
                        "compression_ratio": "N/A",
                        "valvetrain": "N/A",
                        "notes": "75kWh/82kWh NMC battery, 514km WLTP range."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "RWD",
                        "years": {"start": 2022, "end": "Present"},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "RWD",
                        "transmissions": ["Single-speed reduction gear"],
                        "msrp_aud_min": 65400,
                        "msrp_aud_max": 72300,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 1909,
                        "standard_features": ["19-inch Gemini alloys", "Autopilot", "15-inch touchscreen", "Power tailgate", "Full panoramic glass roof", "Heated front and rear seats", "Camp mode and Dog mode"],
                        "notes": "Australia's undisputed electric vehicle sales leader."
                    },
                    {
                        "badge_name": "Performance",
                        "years": {"start": 2022, "end": "Present"},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["Single-speed reduction gear"],
                        "msrp_aud_min": 91400,
                        "msrp_aud_max": 98400,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 1995,
                        "standard_features": ["21-inch Uberturbine alloys", "Performance brakes", "Carbon fibre spoiler", "Lowered suspension", "Aluminium pedals", "0-100 km/h in 3.7 seconds"],
                        "notes": "Supercar-baiting family SUV."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "RWD",
                        "body_style": "5-door SUV",
                        "engine_code": "3D7 Single Motor (RWD)",
                        "transmission": "Single-speed reduction gear",
                        "drivetrain": "RWD",
                        "years_start": 2022,
                        "years_end": "Present",
                        "msrp_aud": 65400,
                        "power_kw": 220,
                        "torque_nm": 420,
                        "fuel_l_100km": 0.0,
                        "towing_braked_kg": 1600,
                        "notes": "60kWh LFP battery with 1600kg braked towing."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "byd/shark-6-atto-3": {
        "make_slug": "byd",
        "model_slug": "shark-6-atto-3",
        "name": "Shark 6 / Atto 3 / Seal",
        "vehicle_type": "Ute / SUV / Sedan",
        "segment": "Electric & Plug-in Hybrid Pioneers",
        "years_sold_au": {"start": 2022, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The trio of game-changing vehicles that propelled BYD to electric and hybrid leadership in Australia: the Atto 3 compact SUV, the Seal sports sedan, and the groundbreaking Shark 6 plug-in hybrid dual-cab ute with 321kW.",
        "australian_market_notes": "Distributed in Australia by EVDirect. The Atto 3 established BYD's brand recognition in 2022. In late 2024, the Shark 6 dual-cab ute made its global right-hand drive debut in Australia, following thousands of kilometres of rigorous local suspension tuning and torture testing across regional Australia.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Atto-3",
                "generation_name": "Atto 3 Electric SUV",
                "years": {"start": 2022, "end": "Present"},
                "body_styles": ["5-door SUV"],
                "platform": "BYD e-Platform 3.0",
                "ancap_rating": "5 stars",
                "summary": "Compact electric crossover with Blade Battery cell-to-pack technology, gym-inspired interior, guitar string door pockets, and rotating 12.8/15.6-inch touchscreen.",
                "engines": [
                    {
                        "engine_code": "BYD-TZ200XSQ",
                        "name": "150kW Front Electric Motor",
                        "displacement_cc": 0,
                        "displacement_litres": 0.0,
                        "cylinders": 0,
                        "configuration": "Single Electric Motor",
                        "aspiration": "Electric",
                        "fuel_type": "Electric",
                        "power_kw": 150,
                        "power_rpm": "Electric",
                        "torque_nm": 310,
                        "torque_rpm": "0-4620",
                        "compression_ratio": "N/A",
                        "valvetrain": "N/A",
                        "notes": "Paired with 49.9kWh (Standard) or 60.5kWh (Extended) Blade Battery."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Extended Range",
                        "years": {"start": 2022, "end": "Present"},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "FWD",
                        "transmissions": ["Single-speed reduction gear"],
                        "msrp_aud_min": 47490,
                        "msrp_aud_max": 51011,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 1750,
                        "standard_features": ["60.5kWh Blade Battery", "15.6-inch rotating touchscreen", "Panoramic sunroof", "Wireless phone charger", "Vehicle-to-Load (V2L) adapter", "360-degree camera"],
                        "notes": "420km WLTP driving range."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Extended Range",
                        "body_style": "5-door SUV",
                        "engine_code": "BYD-TZ200XSQ",
                        "transmission": "Single-speed reduction gear",
                        "drivetrain": "FWD",
                        "years_start": 2022,
                        "years_end": "Present",
                        "msrp_aud": 47490,
                        "power_kw": 150,
                        "torque_nm": 310,
                        "fuel_l_100km": 0.0,
                        "towing_braked_kg": 750,
                        "notes": "60.5kWh LFP Blade battery."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "Shark-6",
                "generation_name": "Shark 6 DMO Super Hybrid Ute",
                "years": {"start": 2024, "end": "Present"},
                "body_styles": ["Dual-cab ute"],
                "platform": "BYD DMO (Dual Mode Off-Road) Super Hybrid",
                "ancap_rating": "5 stars (Targeted)",
                "summary": "Australia's first mass-market plug-in hybrid dual-cab ute; ladder-frame with cell-to-chassis Blade Battery, 1.5L Turbo petrol + front/rear electric motors producing 321kW and 650Nm, independent rear coil suspension, and 2,500kg braked towing.",
                "engines": [
                    {
                        "engine_code": "BYD476ZQC + Dual Motors",
                        "name": "1.5L Turbo + Dual Electric Motors (DMO)",
                        "displacement_cc": 1498,
                        "displacement_litres": 1.5,
                        "cylinders": 4,
                        "configuration": "Inline-4 + Dual Motors",
                        "aspiration": "Turbocharged + Dual Electric",
                        "fuel_type": "Plug-in Hybrid (Petrol / Electric)",
                        "power_kw": 321,
                        "power_rpm": "Combined",
                        "torque_nm": 650,
                        "torque_rpm": "Combined",
                        "compression_ratio": "12.5:1",
                        "valvetrain": "DOHC 16-valve, Miller cycle",
                        "notes": "Front motor (170kW/310Nm), rear motor (150kW/340Nm), 1.5L turbo petrol generator/drive engine."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Premium AWD",
                        "years": {"start": 2024, "end": "Present"},
                        "body_styles": ["Dual-cab ute"],
                        "drivetrain": "AWD",
                        "transmissions": ["Dedicated Hybrid Transmission (E-CVT)"],
                        "msrp_aud_min": 57900,
                        "msrp_aud_max": 60900,
                        "fuel_consumption_l_100km": 2.0,
                        "kerb_weight_kg": 2710,
                        "standard_features": ["29.58kWh Blade Battery pack", "100km pure EV range", "Over 800km total range", "15.6-inch rotating screen", "Head-up display", "Heated and ventilated seats", "V2L vehicle-to-load 6kW power outlets in tub"],
                        "notes": "0-100 km/h in 5.7 seconds; tested specifically on Australian corrugations."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Premium AWD",
                        "body_style": "Dual-cab ute",
                        "engine_code": "BYD476ZQC + Dual Motors",
                        "transmission": "E-CVT",
                        "drivetrain": "AWD",
                        "years_start": 2024,
                        "years_end": "Present",
                        "msrp_aud": 57900,
                        "power_kw": 321,
                        "torque_nm": 650,
                        "fuel_l_100km": 2.0,
                        "towing_braked_kg": 2500,
                        "notes": "321kW dual electric motor plug-in hybrid utility."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "mg/zs-mg4": {
        "make_slug": "mg",
        "model_slug": "zs-mg4",
        "name": "ZS / ZST / MG4",
        "vehicle_type": "SUV / Hatchback",
        "segment": "Small SUV & Electric Hatchback",
        "years_sold_au": {"start": 2017, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The modern pillars of MG Motor's Australian volume resurgence under SAIC: the top-selling ZS and turbocharged ZST compact SUVs, the trailblazing ZS EV, and the universally acclaimed rear-wheel-drive MG4 electric hatchback (including the 320kW XPower).",
        "australian_market_notes": "The ZS was launched in late 2017 and steadily rose to become the number-one best-selling small SUV in Australia. In 2020, the ZS EV arrived as Australia's first sub-$45,000 electric SUV. In 2023, the MG4 arrived on the modular MSP platform, winning multiple Australian Car of the Year awards for its rear-wheel-drive dynamic agility and sharp pricing.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "ZS-ZST",
                "generation_name": "ZS & ZST Compact SUV",
                "years": {"start": 2017, "end": "Present"},
                "body_styles": ["5-door SUV"],
                "platform": "SAIC SSA platform",
                "ancap_rating": "4 stars (ZS) / 5 stars (ZST)",
                "summary": "ZS 1.5L naturally aspirated, upgraded to ZST with 1.3L Turbo (115kW), 6-speed Aisin automatic, and MG Pilot active driver safety.",
                "engines": [
                    {
                        "engine_code": "LIH 1.3T",
                        "name": "1.3L Turbocharged Petrol (ZST)",
                        "displacement_cc": 1349,
                        "displacement_litres": 1.3,
                        "cylinders": 3,
                        "configuration": "Inline-3",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 115,
                        "power_rpm": "5200",
                        "torque_nm": 230,
                        "torque_rpm": "1800-4400",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 12-valve",
                        "notes": "Co-developed by SAIC and GM; paired with 6-speed torque-converter auto."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "ZST Essence",
                        "years": {"start": 2020, "end": "Present"},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed automatic"],
                        "msrp_aud_min": 32990,
                        "msrp_aud_max": 34990,
                        "fuel_consumption_l_100km": 7.1,
                        "kerb_weight_kg": 1295,
                        "standard_features": ["MG Pilot safety suite", "Panoramic glass sunroof", "10.1-inch infotainment screen", "360-degree camera", "Heated front seats", "17-inch two-tone alloys"],
                        "notes": "Popular premium trim level."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "ZST Essence",
                        "body_style": "5-door SUV",
                        "engine_code": "LIH 1.3T",
                        "transmission": "6-speed automatic",
                        "drivetrain": "FWD",
                        "years_start": 2020,
                        "years_end": "Present",
                        "msrp_aud": 32990,
                        "power_kw": 115,
                        "torque_nm": 230,
                        "fuel_l_100km": 7.1,
                        "towing_braked_kg": 500,
                        "notes": "1.3L Turbo with 6-speed auto."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "MG4",
                "generation_name": "MG4 EV Hatchback",
                "years": {"start": 2023, "end": "Present"},
                "body_styles": ["5-door hatchback"],
                "platform": "SAIC MSP (Modular Scalable Platform)",
                "ancap_rating": "5 stars",
                "summary": "Purpose-built rear-wheel drive electric platform with 50:50 weight distribution, ultra-thin 110mm One Pack battery, 51kWh, 64kWh, 77kWh Long Range, and 320kW dual-motor XPower.",
                "engines": [
                    {
                        "engine_code": "TZ204XS1150",
                        "name": "150kW Rear Electric Motor",
                        "displacement_cc": 0,
                        "displacement_litres": 0.0,
                        "cylinders": 0,
                        "configuration": "Single Electric Motor",
                        "aspiration": "Electric",
                        "fuel_type": "Electric",
                        "power_kw": 150,
                        "power_rpm": "Electric",
                        "torque_nm": 250,
                        "torque_rpm": "0-4000",
                        "compression_ratio": "N/A",
                        "valvetrain": "N/A",
                        "notes": "Fitted to 64kWh Essence; 435km WLTP range."
                    },
                    {
                        "engine_code": "Dual Motor XPower",
                        "name": "Dual Electric Motors (XPower AWD)",
                        "displacement_cc": 0,
                        "displacement_litres": 0.0,
                        "cylinders": 0,
                        "configuration": "Dual Electric Motors",
                        "aspiration": "Electric",
                        "fuel_type": "Electric",
                        "power_kw": 320,
                        "power_rpm": "Electric",
                        "torque_nm": 600,
                        "torque_rpm": "0-5000",
                        "compression_ratio": "N/A",
                        "valvetrain": "N/A",
                        "notes": "Front motor 150kW, rear motor 170kW; 0-100 km/h in 3.8 seconds."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "64 Essence",
                        "years": {"start": 2023, "end": "Present"},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "RWD",
                        "transmissions": ["Single-speed reduction gear"],
                        "msrp_aud_min": 44990,
                        "msrp_aud_max": 47990,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 1672,
                        "standard_features": ["64kWh ternary NMC battery", "Rear-wheel drive", "Twin aero rear spoiler", "18-inch aerodynamic alloy wheels", "10.25-inch infotainment display", "Wireless phone charging"],
                        "notes": "Praised for hot hatch chassis dynamics."
                    },
                    {
                        "badge_name": "XPower AWD",
                        "years": {"start": 2023, "end": "Present"},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "AWD",
                        "transmissions": ["Single-speed reduction gear"],
                        "msrp_aud_min": 59990,
                        "msrp_aud_max": 62990,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 1800,
                        "standard_features": ["320kW / 600Nm dual motors", "Orange brake calliper covers with upsized discs", "Electronic locking differential (XDS)", "Launch Control", "Alcantara/leatherette interior"],
                        "notes": "0-100 km/h in 3.8 seconds."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "XPower AWD",
                        "body_style": "5-door hatchback",
                        "engine_code": "Dual Motor XPower",
                        "transmission": "Single-speed reduction gear",
                        "drivetrain": "AWD",
                        "years_start": 2023,
                        "years_end": "Present",
                        "msrp_aud": 59990,
                        "power_kw": 320,
                        "torque_nm": 600,
                        "fuel_l_100km": 0.0,
                        "towing_braked_kg": 500,
                        "notes": "320kW all-wheel drive electric performance hatch."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "gwm-haval/cannon-h6": {
        "make_slug": "gwm-haval",
        "model_slug": "cannon-h6",
        "name": "Cannon / Haval H6 / Tank 300",
        "vehicle_type": "Ute / SUV / 4WD",
        "segment": "Utes & Medium/Large SUVs",
        "years_sold_au": {"start": 2009, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The full evolution of Great Wall Motor in Australia: beginning with the pioneering 2009 Great Wall V240 and V200 utes, progressing to the top-selling GWM Cannon dual-cab, high-tech Haval H6 Hybrid SUV, and heavy-duty Tank 300 off-roader.",
        "australian_market_notes": "Great Wall Motors made history in 2009 as the first Chinese brand in Australia. In 2020, the brand launched the GWM Cannon ute with 3-tonne towing, standard ZF 8-speed automatic, and full suite of ADAS safety, earning a five-star ANCAP rating and capturing major market share from Japanese rivals.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Cannon-Ute",
                "generation_name": "GWM Cannon Ute",
                "years": {"start": 2020, "end": "Present"},
                "body_styles": ["Dual-cab ute"],
                "platform": "GWM P-Series Ladder Frame",
                "ancap_rating": "5 stars",
                "summary": "2.0L Turbo Diesel (120kW/400Nm), 8-speed ZF automatic, BorgWarner torque-on-demand 4WD, rear diff lock, and luxury Cannon-X and Cannon Alpha flagship.",
                "engines": [
                    {
                        "engine_code": "GW4D20M",
                        "name": "2.0L Turbo Diesel",
                        "displacement_cc": 1996,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 120,
                        "power_rpm": "3600",
                        "torque_nm": 400,
                        "torque_rpm": "1500-2500",
                        "compression_ratio": "16.3:1",
                        "valvetrain": "DOHC 16-valve, variable geometry turbo (VGT)",
                        "notes": "Paired with ZF 8-speed automatic transmission."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Cannon-X 4x4",
                        "years": {"start": 2020, "end": "Present"},
                        "body_styles": ["Dual-cab ute"],
                        "drivetrain": "4WD",
                        "transmissions": ["8-speed automatic"],
                        "msrp_aud_min": 41490,
                        "msrp_aud_max": 45490,
                        "fuel_consumption_l_100km": 9.4,
                        "kerb_weight_kg": 2100,
                        "standard_features": ["Leather-accented seats", "7.0-inch colour instrument cluster", "9.0-inch touchscreen with Apple CarPlay/Android Auto", "360-degree camera system", "Spray-in tub liner and gas-assisted tailgate", "Eaton rear differential lock"],
                        "notes": "Outstanding value 4x4 dual-cab."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Cannon-X 4x4",
                        "body_style": "Dual-cab ute",
                        "engine_code": "GW4D20M",
                        "transmission": "8-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2020,
                        "years_end": "Present",
                        "msrp_aud": 41490,
                        "power_kw": 120,
                        "torque_nm": 400,
                        "fuel_l_100km": 9.4,
                        "towing_braked_kg": 3000,
                        "notes": "ZF 8-speed with torque-on-demand 4WD."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "Haval-H6-Gen3",
                "generation_name": "Haval H6 Third Generation",
                "years": {"start": 2021, "end": "Present"},
                "body_styles": ["5-door SUV", "H6 GT coupe-SUV"],
                "platform": "GWM L.E.M.O.N. platform",
                "ancap_rating": "5 stars",
                "summary": "Mid-size family SUV available with 2.0L Turbo petrol (150kW) or 179kW H6 Hybrid with Dedicated Hybrid Transmission (DHT).",
                "engines": [
                    {
                        "engine_code": "GW4B15D + DHT",
                        "name": "1.5L Turbo Dedicated Hybrid (H6 Hybrid)",
                        "displacement_cc": 1499,
                        "displacement_litres": 1.5,
                        "cylinders": 4,
                        "configuration": "Inline-4 Hybrid",
                        "aspiration": "Turbocharged + Electric",
                        "fuel_type": "Hybrid (Petrol)",
                        "power_kw": 179,
                        "power_rpm": "Combined",
                        "torque_nm": 530,
                        "torque_rpm": "Combined",
                        "compression_ratio": "11.8:1",
                        "valvetrain": "DOHC 16-valve, Miller cycle",
                        "notes": "Class-leading torque and 5.2L/100km fuel economy."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "H6 Ultra Hybrid",
                        "years": {"start": 2022, "end": "Present"},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "FWD",
                        "transmissions": ["2-speed Dedicated Hybrid Transmission (DHT)"],
                        "msrp_aud_min": 42990,
                        "msrp_aud_max": 45990,
                        "fuel_consumption_l_100km": 5.2,
                        "kerb_weight_kg": 1690,
                        "standard_features": ["12.3-inch touchscreen", "10.25-inch digital cluster", "Head-up display", "Panoramic sunroof", "Heated and ventilated front seats", "Automated reverse parking assist"],
                        "notes": "Top-selling hybrid midsize SUV."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "H6 Ultra Hybrid",
                        "body_style": "5-door SUV",
                        "engine_code": "GW4B15D + DHT",
                        "transmission": "2-speed DHT",
                        "drivetrain": "FWD",
                        "years_start": 2022,
                        "years_end": "Present",
                        "msrp_aud": 42990,
                        "power_kw": 179,
                        "torque_nm": 530,
                        "fuel_l_100km": 5.2,
                        "towing_braked_kg": 1500,
                        "notes": "179kW/530Nm hybrid powertrain."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "jeep/wrangler": {
        "make_slug": "jeep",
        "model_slug": "wrangler",
        "name": "Wrangler",
        "vehicle_type": "4WD Convertible SUV",
        "segment": "Off-Road 4WD",
        "years_sold_au": {"start": 1996, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The direct descendant of the WWII Willys military Jeep, celebrated in Australia for live beam axles, removable doors and roof, fold-flat windscreen, and rock-crawling Rubicon mastery across TJ, JK, and JL generations.",
        "australian_market_notes": "The TJ generation officially revived the Wrangler nameplate in Australia in 1996 with all-coil suspension and the bulletproof 4.0L AMC inline-six. In 2007, the JK introduced the 4-door Wrangler Unlimited, dramatically expanding the model's family adventure appeal. The modern JL introduced weight-saving aluminium panels, 8-speed automatic, and improved highway refinement.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "TJ",
                "generation_name": "Wrangler TJ",
                "years": {"start": 1996, "end": "2006"},
                "body_styles": ["2-door soft top", "2-door hard top"],
                "platform": "Chrysler TJ",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Introduced Quadra-Coil live axle suspension, replacing leaf springs. AMC 4.0L High Output inline-six, Sport, Renegade, and halo Rubicon with Dana 44 axles and Rock-Trac 4:1 transfer case.",
                "engines": [
                    {
                        "engine_code": "PowerTech 4.0L",
                        "name": "AMC 4.0L High Output Inline-6",
                        "displacement_cc": 3960,
                        "displacement_litres": 4.0,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 130,
                        "power_rpm": "4600",
                        "torque_nm": 301,
                        "torque_rpm": "2800",
                        "compression_ratio": "8.8:1",
                        "valvetrain": "OHV 12-valve, cast-iron block and head",
                        "notes": "Indestructible tractor-like low-end torque for rock crawling."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Sport 4.0",
                        "years": {"start": 1996, "end": "2006"},
                        "body_styles": ["2-door soft top", "2-door hard top"],
                        "drivetrain": "4WD",
                        "transmissions": ["5-speed manual", "6-speed manual", "3-speed/4-speed automatic"],
                        "msrp_aud_min": 29990,
                        "msrp_aud_max": 36990,
                        "fuel_consumption_l_100km": 13.2,
                        "kerb_weight_kg": 1475,
                        "standard_features": ["Command-Trac part-time 4WD", "Dana 30 front / Dana 35 rear axle", "Full metal doors with roll-up windows", "Fold-down windscreen", "Removable doors"],
                        "notes": "Core enthusiast off-roader."
                    },
                    {
                        "badge_name": "Rubicon",
                        "years": {"start": 2003, "end": "2006"},
                        "body_styles": ["2-door soft top", "2-door hard top"],
                        "drivetrain": "4WD",
                        "transmissions": ["5-speed manual", "4-speed automatic"],
                        "msrp_aud_min": 43990,
                        "msrp_aud_max": 47990,
                        "fuel_consumption_l_100km": 14.1,
                        "kerb_weight_kg": 1560,
                        "standard_features": ["Rock-Trac 4:1 low range transfer case", "Heavy-duty Dana 44 front and rear axles", "Tru-Lok pneumatic locking front and rear diffs", "31-inch BFGoodrich Mud-Terrain tyres", "Diamond-plate rocker sill guards"],
                        "notes": "Factory-built rock crawler named after the Rubicon Trail."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Sport 4.0",
                        "body_style": "2-door soft top",
                        "engine_code": "PowerTech 4.0L",
                        "transmission": "5-speed manual",
                        "drivetrain": "4WD",
                        "years_start": 1997,
                        "years_end": "2006",
                        "msrp_aud": 29990,
                        "power_kw": 130,
                        "torque_nm": 301,
                        "fuel_l_100km": 13.2,
                        "towing_braked_kg": 900,
                        "notes": "Classic 4.0L 5-speed manual soft top."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "JK",
                "generation_name": "Wrangler JK",
                "years": {"start": 2007, "end": "2018"},
                "body_styles": ["2-door soft top", "4-door Unlimited"],
                "platform": "Chrysler JK",
                "ancap_rating": "4 stars",
                "summary": "Introduced the four-door Wrangler Unlimited; 3.8L V6 replaced by 209kW 3.6L Pentastar V6 and 2.8L CRD turbo diesel, electronic sway-bar disconnect, and huge Australian sales expansion.",
                "engines": [
                    {
                        "engine_code": "Pentastar 3.6L V6",
                        "name": "3.6L DOHC Pentastar V6",
                        "displacement_cc": 3604,
                        "displacement_litres": 3.6,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 209,
                        "power_rpm": "6350",
                        "torque_nm": 347,
                        "torque_rpm": "4300",
                        "compression_ratio": "10.2:1",
                        "valvetrain": "DOHC 24-valve, dual variable valve timing",
                        "notes": "Replaced the previous 3.8L cast-iron V6 with 40% more power."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Rubicon Unlimited 4-Door",
                        "years": {"start": 2012, "end": "2018"},
                        "body_styles": ["4-door Unlimited"],
                        "drivetrain": "4WD",
                        "transmissions": ["6-speed manual", "5-speed automatic"],
                        "msrp_aud_min": 49990,
                        "msrp_aud_max": 56990,
                        "fuel_consumption_l_100km": 11.7,
                        "kerb_weight_kg": 1995,
                        "standard_features": ["Electronic sway-bar disconnect", "Rock-Trac 4:1 transfer case", "Dana 44 heavy duty axles front/rear", "Tru-Lok electronic diff locks", "Freedom Top three-piece modular hardtop"],
                        "notes": "Australia's ultimate turn-key 4WD adventure rig."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Rubicon Unlimited 4-Door",
                        "body_style": "4-door Unlimited",
                        "engine_code": "Pentastar 3.6L V6",
                        "transmission": "5-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2012,
                        "years_end": "2018",
                        "msrp_aud": 53990,
                        "power_kw": 209,
                        "torque_nm": 347,
                        "fuel_l_100km": 11.7,
                        "towing_braked_kg": 2300,
                        "notes": "4-door Unlimited with electronic lockers and sway-bar disconnect."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "JL",
                "generation_name": "Wrangler JL",
                "years": {"start": 2018, "end": "Present"},
                "body_styles": ["2-door", "4-door Unlimited"],
                "platform": "FCA JL platform",
                "ancap_rating": "3 stars",
                "summary": "Aluminium doors, windscreen frame, and tailgate; 8-speed automatic standard; forward-facing TrailCam; 2.0L Turbo and 3.6L Pentastar; Night Eagle, Overland, and Rubicon.",
                "engines": [
                    {
                        "engine_code": "GME T4 Hurricane",
                        "name": "2.0L Turbo Petrol",
                        "displacement_cc": 1995,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 200,
                        "power_rpm": "5250",
                        "torque_nm": 400,
                        "torque_rpm": "3000",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 16-valve, twin-scroll turbo",
                        "notes": "Standard engine on Australian 2024+ JL refresh."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Rubicon Unlimited JL",
                        "years": {"start": 2019, "end": "Present"},
                        "body_styles": ["4-door Unlimited"],
                        "drivetrain": "4WD",
                        "transmissions": ["8-speed automatic"],
                        "msrp_aud_min": 68950,
                        "msrp_aud_max": 90450,
                        "fuel_consumption_l_100km": 9.9,
                        "kerb_weight_kg": 2045,
                        "standard_features": ["12.3-inch Uconnect 5 touchscreen", "Forward TrailCam off-road camera", "Electronic front sway-bar disconnect", "Tru-Lok front and rear lockers", "Off-Road+ drive mode", "Steel front bumper with removable end-caps"],
                        "notes": "Flagship 4WD rock crawler."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Rubicon Unlimited JL",
                        "body_style": "4-door Unlimited",
                        "engine_code": "GME T4 Hurricane",
                        "transmission": "8-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2024,
                        "years_end": "Present",
                        "msrp_aud": 90450,
                        "power_kw": 200,
                        "torque_nm": 400,
                        "fuel_l_100km": 9.9,
                        "towing_braked_kg": 2495,
                        "notes": "2.0L Turbo with full factory locking differentials."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "ram/ram-1500": {
        "make_slug": "ram",
        "model_slug": "ram-1500",
        "name": "RAM 1500",
        "vehicle_type": "Full-size Pickup Truck",
        "segment": "Full-size American Ute",
        "years_sold_au": {"start": 2018, "end": "Present"},
        "locally_built": True,
        "assembly_plants_au": ["Walkinshaw Automotive Group, Clayton, Victoria (2018-Present)"],
        "overview": "The full-size pickup that rewrote the Australian light commercial market. Re-engineered and remanufactured from left-hand drive to right-hand drive by Walkinshaw Automotive in Clayton, Victoria. Delivers 4.5-tonne towing, legendary 5.7L HEMI V8 rumble, expansive crew-cab luxury, and the 523kW supercharged TRX halo.",
        "australian_market_notes": "Launched in 2018 by RAM Trucks Australia / American Special Vehicles. Over 25,000 trucks remanufactured at Clayton, Victoria under full Australian Design Rule (ADR) compliance. Walkinshaw designed over 400 bespoke RHD components including the instrument panel, HVAC unit, steering gear, and wiring looms. Conquered the heavy towing market for large caravans, horse floats, and offshore fishing boats.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "DS",
                "generation_name": "RAM 1500 DS (Classic)",
                "years": {"start": 2018, "end": "2023"},
                "body_styles": ["Quad Cab", "Crew Cab"],
                "platform": "FCA DS platform",
                "ancap_rating": "Unrated (Exempt >3.5t GVM option / ADR Compliant)",
                "summary": "Remanufactured at Clayton VIC. 5.7L HEMI V8 with 8-speed automatic, coil-sprung rear suspension, 4.5-tonne towing, Express and Warlock trims.",
                "engines": [
                    {
                        "engine_code": "EZH HEMI 5.7L",
                        "name": "5.7L HEMI V8 with VVT and MDS",
                        "displacement_cc": 5654,
                        "displacement_litres": 5.7,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 291,
                        "power_rpm": "5600",
                        "torque_nm": 556,
                        "torque_rpm": "3950",
                        "compression_ratio": "10.5:1",
                        "valvetrain": "OHV 16-valve, Multi-Displacement System (cylinder deactivation)",
                        "notes": "Classic pushrod American V8 with deep exhaust burble."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Express Crew Cab",
                        "years": {"start": 2018, "end": "2023"},
                        "body_styles": ["Crew Cab"],
                        "drivetrain": "4WD",
                        "transmissions": ["TorqueFlite 8-speed automatic"],
                        "msrp_aud_min": 89950,
                        "msrp_aud_max": 99950,
                        "fuel_consumption_l_100km": 14.5,
                        "kerb_weight_kg": 2620,
                        "standard_features": ["4500kg braked towing capacity", "5.7L HEMI V8 (291kW)", "Part-time 4WD transfer case", "20-inch black alloy wheels", "Heavy-duty towbar with trailer brake controller", "Tub liner"],
                        "notes": "The foundation of Australia's full-size truck boom."
                    },
                    {
                        "badge_name": "Warlock",
                        "years": {"start": 2020, "end": "2023"},
                        "body_styles": ["Crew Cab"],
                        "drivetrain": "4WD",
                        "transmissions": ["TorqueFlite 8-speed automatic"],
                        "msrp_aud_min": 104450,
                        "msrp_aud_max": 109950,
                        "fuel_consumption_l_100km": 14.5,
                        "kerb_weight_kg": 2650,
                        "standard_features": ["Ram Rebel aggressive front grille", "Heavy-duty powder-coated front/rear bumpers", "1-inch suspension lift", "Black 20-inch semi-gloss alloys", "RamBox cargo lockable storage compartments in tub walls"],
                        "notes": "Aggressive street/off-road appearance package."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Express Crew Cab",
                        "body_style": "Crew Cab",
                        "engine_code": "EZH HEMI 5.7L",
                        "transmission": "8-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2018,
                        "years_end": "2023",
                        "msrp_aud": 89950,
                        "power_kw": 291,
                        "torque_nm": 556,
                        "fuel_l_100km": 14.5,
                        "towing_braked_kg": 4500,
                        "notes": "Clayton VIC remanufactured full-size pickup with 4.5-tonne towing."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "DT",
                "generation_name": "RAM 1500 DT (Next-Gen & TRX)",
                "years": {"start": 2021, "end": "Present"},
                "body_styles": ["Crew Cab"],
                "platform": "Stellantis DT platform",
                "ancap_rating": "ADR Compliant",
                "summary": "Redesigned high-strength steel chassis, eTorque mild-hybrid HEMI V8, 12-inch portrait Uconnect display, active air suspension, and the monumental 523kW 6.2L Supercharged Hellcat TRX.",
                "engines": [
                    {
                        "engine_code": "EZH eTorque",
                        "name": "5.7L HEMI V8 eTorque Mild-Hybrid",
                        "displacement_cc": 5654,
                        "displacement_litres": 5.7,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated Mild-Hybrid",
                        "fuel_type": "Petrol",
                        "power_kw": 291,
                        "power_rpm": "5600",
                        "torque_nm": 556,
                        "torque_rpm": "3950",
                        "compression_ratio": "10.5:1",
                        "valvetrain": "OHV 16-valve, 48V motor-generator",
                        "notes": "Belt-alternator starter provides supplemental torque and seamless stop-start."
                    },
                    {
                        "engine_code": "Hellcat 6.2L Supercharged",
                        "name": "6.2L Supercharged HEMI V8 (TRX)",
                        "displacement_cc": 6166,
                        "displacement_litres": 6.2,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Supercharged",
                        "fuel_type": "Petrol",
                        "power_kw": 523,
                        "power_rpm": "6100",
                        "torque_nm": 882,
                        "torque_rpm": "4800",
                        "compression_ratio": "9.5:1",
                        "valvetrain": "OHV 16-valve, 2.38L twin-screw supercharger",
                        "notes": "702 horsepower apex predator; 0-100 km/h in 4.5 seconds on dirt or bitumen."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Limited Crew Cab",
                        "years": {"start": 2021, "end": "Present"},
                        "body_styles": ["Crew Cab"],
                        "drivetrain": "4WD",
                        "transmissions": ["TorqueFlite 8-speed automatic"],
                        "msrp_aud_min": 142950,
                        "msrp_aud_max": 156950,
                        "fuel_consumption_l_100km": 12.2,
                        "kerb_weight_kg": 2660,
                        "standard_features": ["Four-corner Active-Level air suspension", "12.0-inch Uconnect touchscreen", "19-speaker Harman Kardon sound", "Premium Natura Plus leather", "Power-deployable side steps", "Twin-pane panoramic sunroof", "RamBox cargo system"],
                        "notes": "Ultra-luxury full-size truck."
                    },
                    {
                        "badge_name": "TRX",
                        "years": {"start": 2022, "end": "2024"},
                        "body_styles": ["Crew Cab"],
                        "drivetrain": "4WD",
                        "transmissions": ["TorqueFlite 8HP95 8-speed automatic"],
                        "msrp_aud_min": 209950,
                        "msrp_aud_max": 224950,
                        "fuel_consumption_l_100km": 19.6,
                        "kerb_weight_kg": 3050,
                        "standard_features": ["523kW 6.2L Supercharged V8", "Bilstein Black Hawk e2 adaptive performance shocks", "Dana 60 solid rear axle with electronic locker", "35-inch Goodyear Wrangler Territory tyres", "Bespoke widebody (8 inches wider)", "Launch Control with jump detection"],
                        "notes": "The most powerful factory production pickup truck ever sold in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Limited Crew Cab",
                        "body_style": "Crew Cab",
                        "engine_code": "EZH eTorque",
                        "transmission": "8-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2021,
                        "years_end": "Present",
                        "msrp_aud": 142950,
                        "power_kw": 291,
                        "torque_nm": 556,
                        "fuel_l_100km": 12.2,
                        "towing_braked_kg": 4500,
                        "notes": "DT air suspension luxury pickup."
                    },
                    {
                        "badge_name": "TRX",
                        "body_style": "Crew Cab",
                        "engine_code": "Hellcat 6.2L Supercharged",
                        "transmission": "8-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2022,
                        "years_end": "2024",
                        "msrp_aud": 209950,
                        "power_kw": 523,
                        "torque_nm": 882,
                        "fuel_l_100km": 19.6,
                        "towing_braked_kg": 3500,
                        "notes": "523kW Supercharged Hellcat V8 truck."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    }
}
