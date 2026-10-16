"""
Deep-dive model data for Ford Falcon and Ford Territory.
"""
from typing import Any, Dict

FALCON_DATA: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "falcon",
    "name": "Ford Falcon",
    "vehicle_type": "Sedan / Wagon / Coupe",
    "segment": "Large",
    "years_sold_au": {"start": 1960, "end": 2016},
    "locally_built": True,
    "assembly_plants_au": [
        "Broadmeadows, Victoria",
        "Eagle Farm, Queensland",
        "Homebush, New South Wales"
    ],
    "overview": "The Ford Falcon is one of the most storied names in Australian industrial and cultural history. Manufactured continuously at Broadmeadows, Victoria for 56 years (1960-2016) across seven distinct generations and over 3.5 million units, the Falcon fought an epic rivalry with the Holden Commodore. From the pioneering XK and the legendary XY GT-HO Phase III (the fastest 4-door production car in the world) to the Australian-designed XA hardtop, the bestselling XF, the indestructible Intech and Barra DOHC sixes, the high-revving Boss V8s, and the supercharged Sprint series, the Falcon embodied Australian engineering resilience and high performance.",
    "australian_market_notes": "Originally derived from the North American compact Falcon in 1960, the XK was comprehensively modified for Australia following ball-joint challenges, culminating in the 1965 XP Durability Run (70,000 miles at 70 mph at You Yangs). The 1967 XR created the Australian V8 muscle car era with the Falcon GT. The 1972 XA was the first Falcon entirely designed and engineered in Australia. In 1980, the XD/XE introduced alloy cylinder heads and Watts-linkage coil rear suspension. In 2002, the BA Falcon brought the revolutionary 4.0L DOHC 24V 'Barra' inline-six and Control Blade independent rear suspension, winning Wheels COTY. In 2008, the FG became the first Australian-built car to score a maximum 5-star ANCAP safety rating. On 7 October 2016, a blue FG X XR6 sedan became the final vehicle produced by Ford Australia.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "XR-XY",
            "generation_name": "Second Generation (XR, XT, XW, XY)",
            "years": {"start": 1966, "end": 1972},
            "body_styles": ["4-door sedan", "5-door wagon"],
            "platform": "Ford full-size unibody",
            "ancap_rating": None,
            "summary": "Mustang-bred styling; birth of the Australian muscle car with the XR Falcon GT (289 Windsor V8); Allan Moffat's back-to-back Bathurst victories in the 351 Cleveland-powered XY GT-HO Phase III.",
            "engines": [
                {
                    "engine_code": "Windsor-289-V8",
                    "name": "Ford Windsor 289ci (4.7L) V8 (XR GT)",
                    "displacement_cc": 4728,
                    "displacement_litres": 4.7,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Super)",
                    "power_kw": 168.0,
                    "power_rpm": "4800",
                    "torque_nm": 414.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "9.8:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Autolite 4-barrel carburettor; first Australian Falcon GT."
                },
                {
                    "engine_code": "Cleveland-351-Phase-III",
                    "name": "Ford 351ci (5.8L) Cleveland V8 (XY GT-HO Phase III)",
                    "displacement_cc": 5752,
                    "displacement_litres": 5.8,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (100 Octane)",
                    "power_kw": 283.0,
                    "power_rpm": "5400",
                    "torque_nm": 515.0,
                    "torque_rpm": "3400",
                    "compression_ratio": "11.0:1",
                    "valvetrain": "OHV 16V Solid Lifter High-Lift Cam",
                    "notes": "Holley 780cfm 4-barrel carburettor, 'shaker' air intake; Bathurst 1971 winner; fastest 4-door production car in the world."
                }
            ],
            "badges": [
                {
                    "badge_name": "Falcon GT",
                    "years": {"start": 1967, "end": 1972},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed Toploader manual", "3-speed Cruisomatic auto"],
                    "msrp_aud_min": 3890,
                    "msrp_aud_max": 4950,
                    "fuel_consumption_l_100km": 17.5,
                    "kerb_weight_kg": 1520,
                    "standard_features": ["351ci V8 (XW/XY)", "Shaker bonnet scoop", "Full instrumentation including 8,000rpm tachometer", "Front power disc brakes", "Twin exhausts"],
                    "notes": "The defining muscle car badge of Australia."
                },
                {
                    "badge_name": "GT-HO Phase III",
                    "years": {"start": 1971, "end": 1972},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed close-ratio Toploader manual"],
                    "msrp_aud_min": 5250,
                    "msrp_aud_max": 5800,
                    "fuel_consumption_l_100km": 19.0,
                    "kerb_weight_kg": 1524,
                    "standard_features": ["High-output 351 Cleveland V8", "Detroit Locker 9-inch rear axle", "Heavy-duty front stabilizer", "Rear boot spoiler", "Shaker scoop"],
                    "notes": "300 units built; 0-100 km/h in 6.4s; top speed 228 km/h; Australia's million-dollar muscle car."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GT-HO Phase III",
                    "body_style": "4-door sedan",
                    "engine_code": "Cleveland-351-Phase-III",
                    "transmission": "4-speed close-ratio Toploader manual",
                    "drivetrain": "RWD",
                    "msrp_aud": 5250,
                    "power_kw": 283.0,
                    "torque_nm": 515.0,
                    "fuel_l_100km": 19.0,
                    "towing_braked_kg": 1500,
                    "notes": "The holy grail of Australian automotive history."
                }
            ]
        },
        {
            "series_code": "XA-XC",
            "generation_name": "Third Generation (XA, XB, XC)",
            "years": {"start": 1972, "end": 1979},
            "body_styles": ["4-door sedan", "5-door wagon", "2-door hardtop coupe"],
            "platform": "Ford Australia all-new unibody",
            "ancap_rating": None,
            "summary": "First all-Australian designed Falcon. Stunning Coke-bottle styling; Hardtop Coupe; Mad Max Interceptor (XB GT); famous 1977 Bathurst 1-2 Moffat/Bond finish in XC Coupes; XC Cobra limited edition.",
            "engines": [
                {
                    "engine_code": "Crossflow-250",
                    "name": "Ford 4.1L (250ci) Crossflow Inline-6",
                    "displacement_cc": 4089,
                    "displacement_litres": 4.1,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 92.0,
                    "power_rpm": "4000",
                    "torque_nm": 298.0,
                    "torque_rpm": "1800",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 12V Crossflow head",
                    "notes": "Introduced in 1976 XC with crossflow cylinder head."
                },
                {
                    "engine_code": "Cleveland-351-4V",
                    "name": "Ford 351ci (5.8L) Cleveland V8",
                    "displacement_cc": 5752,
                    "displacement_litres": 5.8,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 224.0,
                    "power_rpm": "5400",
                    "torque_nm": 515.0,
                    "torque_rpm": "3400",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "OHV 16V",
                    "notes": "4-barrel Holley / Motorcraft carburettor."
                }
            ],
            "badges": [
                {
                    "badge_name": "Falcon 500",
                    "years": {"start": 1972, "end": 1979},
                    "body_styles": ["Sedan", "Wagon", "Hardtop"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual", "Cruisomatic 3-speed auto"],
                    "msrp_aud_min": 3290,
                    "msrp_aud_max": 4450,
                    "fuel_consumption_l_100km": 13.5,
                    "kerb_weight_kg": 1385,
                    "standard_features": ["Flow-through ventilation", "Front disc brakes", "Full steel bumpers"],
                    "notes": "Mainstream family seller."
                },
                {
                    "badge_name": "XC Cobra",
                    "years": {"start": 1978, "end": 1978},
                    "body_styles": ["2-door hardtop coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual (Borg-Warner)", "3-speed auto"],
                    "msrp_aud_min": 8705,
                    "msrp_aud_max": 10500,
                    "fuel_consumption_l_100km": 16.5,
                    "kerb_weight_kg": 1540,
                    "standard_features": ["White with blue dual racing stripes", "302 or 351 Cleveland V8", "Globe Bathurst alloy wheels", "Rear deck spoiler", "Option 97 homologation pack"],
                    "notes": "400 numbered coupes built to celebrate the 1977 Bathurst 1-2 victory."
                }
            ],
            "configurations": [
                {
                    "badge_name": "XC Cobra",
                    "body_style": "2-door hardtop coupe",
                    "engine_code": "Cleveland-351-4V",
                    "transmission": "4-speed manual (Borg-Warner)",
                    "drivetrain": "RWD",
                    "msrp_aud": 8950,
                    "power_kw": 162.0,
                    "torque_nm": 429.0,
                    "fuel_l_100km": 16.5,
                    "towing_braked_kg": 1600,
                    "notes": "Iconic Aussie muscle car."
                }
            ]
        },
        {
            "series_code": "BA-BF",
            "generation_name": "Sixth Generation - BA & BF Series",
            "years": {"start": 2002, "end": 2008},
            "body_styles": ["4-door sedan", "5-door wagon", "2-door utility"],
            "platform": "Ford EA169 architecture",
            "ancap_rating": "4 Stars",
            "summary": "Massive $500 million engineering overhaul that won the 2002 Wheels Car of the Year. Introduced the legendary 4.0L DOHC 24V Barra inline-six, the devastating Barra 240T/245T Turbo, Boss 260/290 quad-cam V8s, Control Blade independent rear suspension, and the peerless ZF 6-speed automatic in BF.",
            "engines": [
                {
                    "engine_code": "Barra-182",
                    "name": "Barra 182 4.0L DOHC 24V Inline-6",
                    "displacement_cc": 3984,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Unleaded)",
                    "power_kw": 182.0,
                    "power_rpm": "5000",
                    "torque_nm": 380.0,
                    "torque_rpm": "3250",
                    "compression_ratio": "9.7:1",
                    "valvetrain": "DOHC 24V Dual Independent Variable Cam Timing (VCT)",
                    "notes": "Bulletproof Australian-designed six; upgraded to Barra 190 (190kW/383Nm) in BF."
                },
                {
                    "engine_code": "Barra-240T",
                    "name": "Barra 240T 4.0L DOHC 24V Turbo Inline-6",
                    "displacement_cc": 3984,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol (Premium Unleaded)",
                    "power_kw": 240.0,
                    "power_rpm": "5250",
                    "torque_nm": 450.0,
                    "torque_rpm": "2000-4500",
                    "compression_ratio": "8.7:1",
                    "valvetrain": "DOHC 24V DIVCT with Garrett GT3582R Turbocharger",
                    "notes": "Legendary Australian turbo motor; massive low-down torque; upgraded to 245kW in BF."
                },
                {
                    "engine_code": "Boss-260-V8",
                    "name": "Boss 260 5.4L DOHC 32V Modular V8",
                    "displacement_cc": 5408,
                    "displacement_litres": 5.4,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Premium Unleaded)",
                    "power_kw": 260.0,
                    "power_rpm": "5250",
                    "torque_nm": 500.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 32V Quad-Cam",
                    "notes": "Cast-iron block with Mustang Cobra R quad-cam cylinder heads."
                }
            ],
            "badges": [
                {
                    "badge_name": "XT",
                    "years": {"start": 2002, "end": 2008},
                    "body_styles": ["Sedan", "Wagon"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual (Tremec T5)", "4-speed auto", "ZF 6-speed auto (BF)"],
                    "msrp_aud_min": 33900,
                    "msrp_aud_max": 38900,
                    "fuel_consumption_l_100km": 10.9,
                    "kerb_weight_kg": 1694,
                    "standard_features": ["Barra 182/190 engine", "Control Blade IRS (sedan)", "Interior Command Centre (ICC)", "ABS with EBD", "Dual airbags"],
                    "notes": "Fleet and family staple."
                },
                {
                    "badge_name": "XR6 Turbo",
                    "years": {"start": 2002, "end": 2008},
                    "body_styles": ["Sedan", "Utility"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed/6-speed manual (Tremec T56)", "4-speed auto / ZF 6-speed auto"],
                    "msrp_aud_min": 44640,
                    "msrp_aud_max": 51200,
                    "fuel_consumption_l_100km": 11.9,
                    "kerb_weight_kg": 1710,
                    "standard_features": ["Barra 240T/245T Turbo", "Sports suspension", "17-inch alloys", "LSD", "Twin exhaust", "Sports seats"],
                    "notes": "0-100 km/h in 5.9s; performance sensation."
                },
                {
                    "badge_name": "XR8",
                    "years": {"start": 2002, "end": 2008},
                    "body_styles": ["Sedan", "Utility"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed/6-speed manual (T56)", "4-speed auto / ZF 6-speed auto"],
                    "msrp_aud_min": 46990,
                    "msrp_aud_max": 53500,
                    "fuel_consumption_l_100km": 14.5,
                    "kerb_weight_kg": 1785,
                    "standard_features": ["Boss 260 5.4L 32V V8", "Signature power-bulge bonnet", "17-inch/18-inch alloys", "Heavy-duty brakes", "Sports exhaust"],
                    "notes": "Deep muscular V8 rumble."
                }
            ],
            "configurations": [
                {
                    "badge_name": "XR6 Turbo",
                    "body_style": "Sedan",
                    "engine_code": "Barra-240T",
                    "transmission": "ZF 6-speed auto (BF)",
                    "drivetrain": "RWD",
                    "msrp_aud": 46490,
                    "power_kw": 245.0,
                    "torque_nm": 480.0,
                    "fuel_l_100km": 11.7,
                    "towing_braked_kg": 2300,
                    "notes": "The benchmark Australian performance sports sedan."
                }
            ]
        },
        {
            "series_code": "FG-FGX",
            "generation_name": "Seventh Generation - FG & FG X Series",
            "years": {"start": 2008, "end": 2016},
            "body_styles": ["4-door sedan", "2-door utility"],
            "platform": "Ford Orion platform",
            "ancap_rating": "5 Stars",
            "summary": "First Australian-built car to achieve a 5-star ANCAP rating. Barra 195, Barra 270T/310T Turbo, EcoBoost 2.0L Turbo, Boss 290, and final Sprint 6 (325kW) and Sprint 8 (345kW/400kW overboost). Final Australian Falcon built 7 October 2016.",
            "engines": [
                {
                    "engine_code": "Barra-195",
                    "name": "Barra 195 4.0L DOHC 24V Inline-6",
                    "displacement_cc": 3984,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Unleaded)",
                    "power_kw": 195.0,
                    "power_rpm": "6000",
                    "torque_nm": 391.0,
                    "torque_rpm": "3250",
                    "compression_ratio": "10.3:1",
                    "valvetrain": "DOHC 24V Dual Independent VCT",
                    "notes": "Composite variable intake manifold, 9.9 L/100km."
                },
                {
                    "engine_code": "Barra-270T",
                    "name": "Barra 270T 4.0L DOHC 24V Turbo Inline-6",
                    "displacement_cc": 3984,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol (Premium 95/98)",
                    "power_kw": 270.0,
                    "power_rpm": "5250",
                    "torque_nm": 533.0,
                    "torque_rpm": "1950-4750",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "DOHC 24V Garrett GT3576R Water-cooled Turbocharger",
                    "notes": "Massive 533Nm flat torque curve; 0-100 km/h in 5.1s."
                },
                {
                    "engine_code": "EcoBoost-2.0T",
                    "name": "Ford EcoBoost 2.0L Turbo Inline-4",
                    "displacement_cc": 1999,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol (95 RON)",
                    "power_kw": 179.0,
                    "power_rpm": "5500",
                    "torque_nm": 353.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16V Ti-VCT Direct Injection",
                    "notes": "Lightened front axle by 54kg, sharpening steering response; 8.1 L/100km."
                },
                {
                    "engine_code": "Miami-Supercharged-5.0",
                    "name": "Miami 5.0L Supercharged 32V V8 (Sprint 8)",
                    "displacement_cc": 4951,
                    "displacement_litres": 5.0,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Supercharged",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 345.0,
                    "power_rpm": "5750",
                    "torque_nm": 575.0,
                    "torque_rpm": "2220-6250",
                    "compression_ratio": "9.25:1",
                    "valvetrain": "DOHC 32V with Harrop HTV 1900 Supercharger",
                    "notes": "Delivers 400kW and 650Nm on transient overboost; 0-100 km/h in 4.5s; 750 units built."
                }
            ],
            "badges": [
                {
                    "badge_name": "XR6",
                    "years": {"start": 2008, "end": 2016},
                    "body_styles": ["Sedan", "Utility"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "ZF 6-speed automatic"],
                    "msrp_aud_min": 38990,
                    "msrp_aud_max": 43500,
                    "fuel_consumption_l_100km": 9.9,
                    "kerb_weight_kg": 1704,
                    "standard_features": ["Barra 195 engine", "Sports suspension", "18-inch alloys", "Sports seats", "8-inch touchscreen (FG X)"],
                    "notes": "The most popular sports sedan in Australia."
                },
                {
                    "badge_name": "XR6 Turbo",
                    "years": {"start": 2008, "end": 2016},
                    "body_styles": ["Sedan", "Utility"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual (TR-6060)", "ZF 6-speed automatic (6HP26)"],
                    "msrp_aud_min": 45490,
                    "msrp_aud_max": 50500,
                    "fuel_consumption_l_100km": 11.7,
                    "kerb_weight_kg": 1762,
                    "standard_features": ["Barra 270T 270kW/533Nm", "Upgraded front brakes", "Limited slip differential", "18-inch/19-inch alloys", "Launch control"],
                    "notes": "Cult performance icon."
                },
                {
                    "badge_name": "XR6 Sprint / XR8 Sprint",
                    "years": {"start": 2016, "end": 2016},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual (XR8)", "ZF 6-speed auto"],
                    "msrp_aud_min": 54990,
                    "msrp_aud_max": 62190,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1818,
                    "standard_features": ["Sprint 6 (325kW/370kW overboost) or Sprint 8 (345kW/400kW overboost)", "Brembo 6-piston front brakes", "Pirelli P-Zero tyres", "Sprint numbered build plaque", "Carbon-look accents"],
                    "notes": "Final limited edition masterpiece; 500 Sprint 6 and 750 Sprint 8 produced."
                }
            ],
            "configurations": [
                {
                    "badge_name": "XR6 Turbo",
                    "body_style": "Sedan",
                    "engine_code": "Barra-270T",
                    "transmission": "ZF 6-speed automatic (6HP26)",
                    "drivetrain": "RWD",
                    "msrp_aud": 46590,
                    "power_kw": 270.0,
                    "torque_nm": 533.0,
                    "fuel_l_100km": 11.7,
                    "towing_braked_kg": 2300,
                    "notes": "0-100 km/h in 5.1s; devastating highway punch."
                },
                {
                    "badge_name": "XR8 Sprint",
                    "body_style": "Sedan",
                    "engine_code": "Miami-Supercharged-5.0",
                    "transmission": "ZF 6-speed auto",
                    "drivetrain": "RWD",
                    "msrp_aud": 62190,
                    "power_kw": 345.0,
                    "torque_nm": 575.0,
                    "fuel_l_100km": 14.0,
                    "towing_braked_kg": 2300,
                    "notes": "400kW overboost; ultimate factory Falcon."
                }
            ]
        }
    ]
}

TERRITORY_DATA: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "territory",
    "name": "Ford Territory",
    "vehicle_type": "SUV",
    "segment": "Medium / Large SUV",
    "years_sold_au": {"start": 2004, "end": 2016},
    "locally_built": True,
    "assembly_plants_au": [
        "Broadmeadows, Victoria"
    ],
    "overview": "The Ford Territory was the first and only sports utility vehicle (SUV) designed, engineered, and manufactured in Australia. Developed under the code-name 'E265' at a cost of $500 million, the Territory debuted in April 2004 and won the prestigious 2004 Wheels Car of the Year award. Available in 5- and 7-seat configurations, in rear-wheel drive and permanent all-wheel drive, the Territory combined car-like handling, Virtual Pivot Control front suspension, and generous interior packaging, spanning SX, SY, and SZ series with Barra I6, Barra Turbo, and 2.7L V6 turbo-diesel engines.",
    "australian_market_notes": "Conceived under Ford Australia president Geoff Polites as Australian families began migrating from traditional large station wagons to high-riding SUVs, the Territory was engineered specifically for Australian family road trips, outback gravel touring, and boat towing. It featured 30 interior storage compartments, an independently opening tailgate glass window, and standard electronic stability control (ESC)—the first Australian-built car with standard ESC. Over 178,000 Territory SUVs were manufactured at Broadmeadows before local production concluded in October 2016.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "SX",
            "generation_name": "Territory SX Series",
            "years": {"start": 2004, "end": 2005},
            "body_styles": ["5-door SUV (5 or 7 seats)"],
            "platform": "Ford EA169 modified SUV platform",
            "ancap_rating": "4 Stars",
            "summary": "2004 Wheels Car of the Year winner; Barra 182 4.0L DOHC I6, Virtual Pivot Control front suspension, Control Blade rear IRS, TX, TS, Ghia.",
            "engines": [
                {
                    "engine_code": "Barra-182-Territory",
                    "name": "Barra 182 4.0L DOHC 24V Inline-6",
                    "displacement_cc": 3984,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Unleaded)",
                    "power_kw": 182.0,
                    "power_rpm": "5000",
                    "torque_nm": 380.0,
                    "torque_rpm": "3250",
                    "compression_ratio": "9.7:1",
                    "valvetrain": "DOHC 24V Dual Independent VCT",
                    "notes": "Specially calibrated torque curve for SUV towing."
                }
            ],
            "badges": [
                {
                    "badge_name": "TX",
                    "years": {"start": 2004, "end": 2005},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "RWD / AWD",
                    "transmissions": ["4-speed automatic"],
                    "msrp_aud_min": 38990,
                    "msrp_aud_max": 42990,
                    "fuel_consumption_l_100km": 12.2,
                    "kerb_weight_kg": 2015,
                    "standard_features": ["Air conditioning", "4-wheel disc brakes with ABS", "Electronic Stability Control (standard on AWD)", "Dual airbags", "30 interior storage compartments"],
                    "notes": "Entry family model."
                },
                {
                    "badge_name": "Ghia",
                    "years": {"start": 2004, "end": 2005},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "RWD / AWD",
                    "transmissions": ["4-speed automatic"],
                    "msrp_aud_min": 49290,
                    "msrp_aud_max": 53290,
                    "fuel_consumption_l_100km": 12.5,
                    "kerb_weight_kg": 2085,
                    "standard_features": ["Leather upholstery", "7-seat configuration", "Dual-zone climate control", "Rear-seat colour DVD screen", "17-inch alloy wheels"],
                    "notes": "Luxury family hauler."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Ghia AWD",
                    "body_style": "5-door SUV",
                    "engine_code": "Barra-182-Territory",
                    "transmission": "4-speed automatic",
                    "drivetrain": "AWD",
                    "msrp_aud": 53290,
                    "power_kw": 182.0,
                    "torque_nm": 380.0,
                    "fuel_l_100km": 12.5,
                    "towing_braked_kg": 2300,
                    "notes": "Wheels Car of the Year 2004."
                }
            ]
        },
        {
            "series_code": "SY",
            "generation_name": "Territory SY & SY II Series",
            "years": {"start": 2005, "end": 2011},
            "body_styles": ["5-door SUV"],
            "platform": "Ford EA169 modified SUV platform",
            "ancap_rating": "4 Stars",
            "summary": "Introduced the German ZF 6-speed automatic transmission, Barra 190 I6, and the blisteringly fast 245kW Territory Turbo and Turbo Ghia.",
            "engines": [
                {
                    "engine_code": "Barra-245T-Territory",
                    "name": "Barra 245T 4.0L DOHC 24V Turbo Inline-6",
                    "displacement_cc": 3984,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol (Premium Unleaded)",
                    "power_kw": 245.0,
                    "power_rpm": "5250",
                    "torque_nm": 480.0,
                    "torque_rpm": "2000-4500",
                    "compression_ratio": "8.7:1",
                    "valvetrain": "DOHC 24V DIVCT Garrett Turbo",
                    "notes": "Fitted exclusively with AWD and ZF 6-speed auto; 0-100 km/h in 6.7 seconds."
                }
            ],
            "badges": [
                {
                    "badge_name": "Turbo / Turbo Ghia",
                    "years": {"start": 2006, "end": 2011},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "AWD",
                    "transmissions": ["ZF 6-speed automatic"],
                    "msrp_aud_min": 53990,
                    "msrp_aud_max": 65490,
                    "fuel_consumption_l_100km": 14.2,
                    "kerb_weight_kg": 2145,
                    "standard_features": ["245kW Turbo engine", "Bonnet scoop", "18-inch alloys", "High-performance brake package", "Leather seating (Turbo Ghia)"],
                    "notes": "Fastest family SUV in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Turbo Ghia",
                    "body_style": "5-door SUV",
                    "engine_code": "Barra-245T-Territory",
                    "transmission": "ZF 6-speed automatic",
                    "drivetrain": "AWD",
                    "msrp_aud": 65490,
                    "power_kw": 245.0,
                    "torque_nm": 480.0,
                    "fuel_l_100km": 14.2,
                    "towing_braked_kg": 2300,
                    "notes": "High performance luxury family cruiser."
                }
            ]
        },
        {
            "series_code": "SZ",
            "generation_name": "Territory SZ & SZ II Series",
            "years": {"start": 2011, "end": 2016},
            "body_styles": ["5-door SUV"],
            "platform": "Ford Orion SUV platform",
            "ancap_rating": "5 Stars",
            "summary": "Major redesign introducing the long-awaited 2.7L Duratorq V6 Turbo Diesel (TDCi) with 440Nm of torque, 5-star ANCAP safety, electric power-assisted steering, and SYNC infotainment.",
            "engines": [
                {
                    "engine_code": "Duratorq-2.7-TDCi",
                    "name": "Ford Duratorq 2.7L V6 Turbo Diesel (TDCi)",
                    "displacement_cc": 2720,
                    "displacement_litres": 2.7,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 140.0,
                    "power_rpm": "4000",
                    "torque_nm": 440.0,
                    "torque_rpm": "1900",
                    "compression_ratio": "17.3:1",
                    "valvetrain": "DOHC 24V Variable Geometry Turbo",
                    "notes": "Compacted graphite iron (CGI) block; 8.2 L/100km (RWD) and 9.0 L/100km (AWD)."
                },
                {
                    "engine_code": "Barra-195-Territory",
                    "name": "Barra 195 4.0L DOHC Inline-6",
                    "displacement_cc": 3984,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Unleaded)",
                    "power_kw": 195.0,
                    "power_rpm": "6000",
                    "torque_nm": 391.0,
                    "torque_rpm": "3250",
                    "compression_ratio": "10.3:1",
                    "valvetrain": "DOHC 24V DIVCT",
                    "notes": "Standard petrol engine; matched with ZF 6-speed auto."
                }
            ],
            "badges": [
                {
                    "badge_name": "Titanium",
                    "years": {"start": 2011, "end": 2016},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "RWD / AWD",
                    "transmissions": ["ZF 6-speed automatic (6R80 / 6HP26)"],
                    "msrp_aud_min": 54990,
                    "msrp_aud_max": 62740,
                    "fuel_consumption_l_100km": 8.8,
                    "kerb_weight_kg": 2167,
                    "standard_features": ["7 seats standard", "Leather trim", "Alpine ceiling-mounted DVD", "8-inch touchscreen with navigation and SYNC2", "18-inch alloy wheels", "Reversing camera"],
                    "notes": "Top-of-the-range luxury family specification."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Titanium TDCi AWD",
                    "body_style": "5-door SUV",
                    "engine_code": "Duratorq-2.7-TDCi",
                    "transmission": "ZF 6-speed automatic",
                    "drivetrain": "AWD",
                    "msrp_aud": 62740,
                    "power_kw": 140.0,
                    "torque_nm": 440.0,
                    "fuel_l_100km": 9.0,
                    "towing_braked_kg": 2700,
                    "notes": "Outstanding long-distance touring economy and towing."
                }
            ]
        }
    ]
}
