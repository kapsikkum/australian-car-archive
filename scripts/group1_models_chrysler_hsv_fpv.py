"""
Deep-dive model data for Chrysler Valiant, Chrysler Valiant Charger, HSV ClubSport/GTS, and FPV GT/F6.
"""
from typing import Any, Dict

VALIANT_DATA: Dict[str, Any] = {
    "make_slug": "chrysler-valiant",
    "model_slug": "valiant",
    "name": "Chrysler Valiant",
    "vehicle_type": "Sedan / Wagon",
    "segment": "Large",
    "years_sold_au": {"start": 1962, "end": 1981},
    "locally_built": True,
    "assembly_plants_au": [
        "Tonsley Park, South Australia",
        "Mile End, South Australia"
    ],
    "overview": "The Chrysler Valiant was the spirited contender of the Australian family car triumvirate alongside the Holden Kingswood and Ford Falcon. Manufactured at Chrysler Australia's sprawling Tonsley Park complex in Adelaide from 1962 to 1981 across 13 series (R, S, AP5, AP6, VC, VE, VF, VG, VH, VJ, VK, CL, CM), the Valiant established an enduring reputation for unmatched horsepower, introducing the 145 hp Slant-6 in 1962, Australia's first family car V8 in 1965, the world-renowned Australian-engineered HEMI-6 in 1970, and pioneering Electronic Lean Burn (ELB) computer management.",
    "australian_market_notes": "When Chrysler assembled 1,008 R-Series Valiants in Adelaide in early 1962, their 225ci Slant-6 engine developed nearly double the power of the contemporary Holden EK, creating queues around dealership blocks. In 1965, the AP6 debuted the 273ci Fireball V8, sparking the Australian V8 era. Under chief engineer David Giles, Chrysler Australia invested $22 million developing the legendary HEMI-6 engine, which debuted in the 1970 VG series with hemispherical combustion chambers in 215ci, 245ci, and 265ci displacements. The 1971 VH was the first Valiant designed and styled completely in Australia. In 1978, the CM series introduced Electronic Lean Burn (ELB) computer spark advance, providing remarkable fuel efficiency before production ceased in August 1981.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "R-S",
            "generation_name": "R and S Series",
            "years": {"start": 1962, "end": 1963},
            "body_styles": ["4-door sedan"],
            "platform": "Chrysler unibody",
            "ancap_rating": None,
            "summary": "The car that changed Australian family performance. 225ci Slant-6 producing 145 bhp; torsion bar front suspension; push-button Torqueflite automatic.",
            "engines": [
                {
                    "engine_code": "Slant-6-225",
                    "name": "Chrysler 225ci (3.7L) Slant-6",
                    "displacement_cc": 3687,
                    "displacement_litres": 3.7,
                    "cylinders": 6,
                    "configuration": "Inline inclined 30 degrees",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 108.0,
                    "power_rpm": "4000",
                    "torque_nm": 292.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "8.2:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Single-barrel Carter carburettor; 145 gross horsepower."
                }
            ],
            "badges": [
                {
                    "badge_name": "Valiant",
                    "years": {"start": 1962, "end": 1963},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual floor shift", "Torqueflite 3-speed push-button auto"],
                    "msrp_aud_min": 2450,
                    "msrp_aud_max": 2850,
                    "fuel_consumption_l_100km": 13.0,
                    "kerb_weight_kg": 1240,
                    "standard_features": ["Torsion-Aire front suspension", "145hp Slant-6 engine", "Padded dash", "12-volt electrical system"],
                    "notes": "Instant sell-out sensation across Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Valiant",
                    "body_style": "4-door sedan",
                    "engine_code": "Slant-6-225",
                    "transmission": "Torqueflite 3-speed push-button auto",
                    "drivetrain": "RWD",
                    "msrp_aud": 2680,
                    "power_kw": 108.0,
                    "torque_nm": 292.0,
                    "fuel_l_100km": 13.0,
                    "towing_braked_kg": 1200,
                    "notes": "Out-accelerated all rivals in 1962."
                }
            ]
        },
        {
            "series_code": "VG-VJ",
            "generation_name": "VG to VJ Series (The Hemi-6 Era)",
            "years": {"start": 1970, "end": 1975},
            "body_styles": ["4-door sedan", "5-door Safari wagon", "2-door hardtop"],
            "platform": "Chrysler Australia wide-body chassis",
            "ancap_rating": None,
            "summary": "Introduced the legendary Australian-designed and engineered HEMI-6 engine (215, 245, 265ci) with hemispherical combustion chambers, alongside 318ci Fireball V8.",
            "engines": [
                {
                    "engine_code": "Hemi-245",
                    "name": "Chrysler Hemi-6 245ci (4.0L) Inline-6",
                    "displacement_cc": 4015,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 123.0,
                    "power_rpm": "4400",
                    "torque_nm": 325.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "OHV 12V Hemispherical chambers",
                    "notes": "Carter 2-barrel carburettor; 165 gross hp; massive low-end torque."
                },
                {
                    "engine_code": "Hemi-265",
                    "name": "Chrysler Hemi-6 265ci (4.3L) Inline-6",
                    "displacement_cc": 4342,
                    "displacement_litres": 4.3,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 151.0,
                    "power_rpm": "4800",
                    "torque_nm": 355.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "OHV 12V Hemispherical chambers",
                    "notes": "2-barrel Carter BBD; 203 gross hp; standard in Regal 770."
                },
                {
                    "engine_code": "Fireball-318-V8",
                    "name": "Chrysler 318ci (5.2L) Fireball V8",
                    "displacement_cc": 5211,
                    "displacement_litres": 5.2,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 172.0,
                    "power_rpm": "4400",
                    "torque_nm": 461.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Carter 2-barrel; smooth, effortless cruiser."
                }
            ],
            "badges": [
                {
                    "badge_name": "Regal 770",
                    "years": {"start": 1970, "end": 1975},
                    "body_styles": ["4-door sedan", "2-door hardtop"],
                    "drivetrain": "RWD",
                    "transmissions": ["Torqueflite 3-speed automatic"],
                    "msrp_aud_min": 3950,
                    "msrp_aud_max": 4890,
                    "fuel_consumption_l_100km": 14.5,
                    "kerb_weight_kg": 1440,
                    "standard_features": ["265 Hemi-6 or 318 V8", "Buffalo grain vinyl roof", "Reclining bucket seats with center console", "Full woodgrain dash", "Front power disc brakes"],
                    "notes": "High luxury executive flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Regal 770",
                    "body_style": "4-door sedan",
                    "engine_code": "Hemi-265",
                    "transmission": "Torqueflite 3-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 4350,
                    "power_kw": 151.0,
                    "torque_nm": 355.0,
                    "fuel_l_100km": 14.2,
                    "towing_braked_kg": 1500,
                    "notes": "The great Aussie Hemi six cruiser."
                }
            ]
        },
        {
            "series_code": "CM",
            "generation_name": "CM Series (Electronic Lean Burn)",
            "years": {"start": 1978, "end": 1981},
            "body_styles": ["4-door sedan", "5-door Safari wagon"],
            "platform": "Chrysler Australia chassis",
            "ancap_rating": None,
            "summary": "Final Australian Valiant series. Introduced Electronic Lean Burn (ELB) computer-controlled spark timing on the 4.0L and 4.3L Hemi-6, delivering unmatched large-car fuel efficiency.",
            "engines": [
                {
                    "engine_code": "Hemi-265-ELB",
                    "name": "Chrysler Hemi-6 4.3L (265ci) ELB",
                    "displacement_cc": 4342,
                    "displacement_litres": 4.3,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 120.0,
                    "power_rpm": "4400",
                    "torque_nm": 318.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 12V with Electronic Spark Control",
                    "notes": "Spark Advance computer adjusts timing; 10.5 L/100km highway."
                }
            ],
            "badges": [
                {
                    "badge_name": "Regal",
                    "years": {"start": 1978, "end": 1981},
                    "body_styles": ["4-door sedan", "Safari wagon"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual (Borg-Warner)", "Torqueflite 3-speed auto"],
                    "msrp_aud_min": 7990,
                    "msrp_aud_max": 9850,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 1460,
                    "standard_features": ["Electronic Lean Burn", "Cloth seat trim", "Power steering", "Air conditioning option"],
                    "notes": "Final Australian Valiant."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Regal",
                    "body_style": "4-door sedan",
                    "engine_code": "Hemi-265-ELB",
                    "transmission": "Torqueflite 3-speed auto",
                    "drivetrain": "RWD",
                    "msrp_aud": 8950,
                    "power_kw": 120.0,
                    "torque_nm": 318.0,
                    "fuel_l_100km": 11.5,
                    "towing_braked_kg": 1500,
                    "notes": "The last Valiant made at Tonsley Park on 28 August 1981."
                }
            ]
        }
    ]
}

CHARGER_DATA: Dict[str, Any] = {
    "make_slug": "chrysler-valiant",
    "model_slug": "charger",
    "name": "Chrysler Valiant Charger",
    "vehicle_type": "Coupe",
    "segment": "Sports Coupe / Muscle Car",
    "years_sold_au": {"start": 1971, "end": 1978},
    "locally_built": True,
    "assembly_plants_au": [
        "Tonsley Park, South Australia"
    ],
    "overview": "The Chrysler Valiant Charger is one of the most charismatic muscle cars in Australian history. Launched in August 1971 with the memorable 'Hey Charger!' television advertising campaign, the Charger was built on a shortened 105-inch wheelbase with stunning fastback proportions, winning the 1971 Wheels Car of the Year award. Immortalized by the legendary Bathurst homologation specials—the E38 (280 bhp) and the triple-Weber E49 'Six Pack' (302 bhp)—the Charger was the fastest-accelerating Australian production car for over a decade, holding the standing quarter-mile record at 14.4 seconds.",
    "australian_market_notes": "Engineered under John Ellis by chopping 6 inches out of the VH sedan wheelbase and styling an aerodynamic fastback tail, the Charger captured 50% of all Australian sports coupe sales in its first year. The racing program was developed in secret with Italian carburettor masters Weber: the E49 engine featured three twin-choke Weber 45 DCOE carburettors, a high-lift camshaft, tuned exhaust headers, and a heavy-duty Borg-Warner 4-speed manual gearbox. Production continued through VJ, VK, and CL series, concluding with the colorful 1977-78 Charger Drifter.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "VH",
            "generation_name": "VH Charger Series",
            "years": {"start": 1971, "end": 1973},
            "body_styles": ["2-door sports coupe"],
            "platform": "Chrysler Australia short-wheelbase chassis",
            "ancap_rating": None,
            "summary": "1971 Wheels Car of the Year winner; 'Hey Charger!' advertising icon; Charger XL, 770, R/T (E37, E38 280 bhp), and the ultimate E49 Six Pack (302 bhp, 3x Weber, 4-speed manual).",
            "engines": [
                {
                    "engine_code": "Hemi-265-E38",
                    "name": "Chrysler Hemi-6 265ci 'Six Pack' (E38 R/T)",
                    "displacement_cc": 4342,
                    "displacement_litres": 4.3,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (100 Octane)",
                    "power_kw": 209.0,
                    "power_rpm": "5000",
                    "torque_nm": 420.0,
                    "torque_rpm": "3700",
                    "compression_ratio": "9.7:1",
                    "valvetrain": "OHV 12V with High-Lift Cam",
                    "notes": "Triple twin-choke Weber 45 DCOE carburettors; 280 bhp; 3-speed manual."
                },
                {
                    "engine_code": "Hemi-265-E49",
                    "name": "Chrysler Hemi-6 265ci 'Six Pack' (E49 R/T)",
                    "displacement_cc": 4342,
                    "displacement_litres": 4.3,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (100 Octane)",
                    "power_kw": 225.0,
                    "power_rpm": "5600",
                    "torque_nm": 441.0,
                    "torque_rpm": "4100",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "OHV 12V Competition Cam and Valve Springs",
                    "notes": "Triple twin-choke Weber 45 DCOE; 302 bhp; Borg-Warner 4-speed manual; fastest accelerating Australian production car for over a decade."
                }
            ],
            "badges": [
                {
                    "badge_name": "Charger R/T (E49)",
                    "years": {"start": 1972, "end": 1973},
                    "body_styles": ["2-door sports coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed close-ratio manual (Borg-Warner)"],
                    "msrp_aud_min": 3975,
                    "msrp_aud_max": 4500,
                    "fuel_consumption_l_100km": 16.0,
                    "kerb_weight_kg": 1365,
                    "standard_features": ["302 bhp Hemi-6 engine", "Triple Weber carburettors", "35-gallon long-range fuel tank option", "Alloy sports wheels", "R/T side body decals and blackouts"],
                    "notes": "Only 149 units produced; standing quarter-mile in 14.4 seconds."
                },
                {
                    "badge_name": "Charger 770",
                    "years": {"start": 1971, "end": 1973},
                    "body_styles": ["2-door sports coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["Torqueflite 3-speed auto", "4-speed manual"],
                    "msrp_aud_min": 3395,
                    "msrp_aud_max": 4200,
                    "fuel_consumption_l_100km": 14.0,
                    "kerb_weight_kg": 1380,
                    "standard_features": ["265 Hemi or 318 V8", "High-back bucket seats", "Woodgrain dash", "Alloy wheels"],
                    "notes": "Luxury grand tourer variant."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Charger R/T (E49)",
                    "body_style": "2-door sports coupe",
                    "engine_code": "Hemi-265-E49",
                    "transmission": "4-speed close-ratio manual (Borg-Warner)",
                    "drivetrain": "RWD",
                    "msrp_aud": 4250,
                    "power_kw": 225.0,
                    "torque_nm": 441.0,
                    "fuel_l_100km": 16.0,
                    "towing_braked_kg": 1200,
                    "notes": "0-100 km/h in 6.1s; 0-400m in 14.4s; Bathurst legend."
                }
            ]
        },
        {
            "series_code": "CL",
            "generation_name": "CL Charger Series",
            "years": {"start": 1976, "end": 1978},
            "body_styles": ["2-door sports coupe"],
            "platform": "Chrysler Australia chassis",
            "ancap_rating": None,
            "summary": "Final Charger generation. 770 luxury sports and the iconic Drifter pack with bold side striping, roof-mounted spoiler, and 4.3L Hemi 4-speed manual.",
            "engines": [
                {
                    "engine_code": "Hemi-265-CL",
                    "name": "Chrysler Hemi-6 4.3L (265ci) 4-Barrel",
                    "displacement_cc": 4342,
                    "displacement_litres": 4.3,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 151.0,
                    "power_rpm": "4800",
                    "torque_nm": 355.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Carter 4-barrel option on E48 engine."
                }
            ],
            "badges": [
                {
                    "badge_name": "Charger Drifter",
                    "years": {"start": 1977, "end": 1978},
                    "body_styles": ["2-door sports coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual (Borg-Warner)"],
                    "msrp_aud_min": 6890,
                    "msrp_aud_max": 7650,
                    "fuel_consumption_l_100km": 14.5,
                    "kerb_weight_kg": 1410,
                    "standard_features": ["Bold rainbow Drifter side graphics", "W56 sports wheels in body colour", "Sports steering wheel", "Radial Tuned Suspension", "265 Hemi or 318 V8"],
                    "notes": "Final edition cult classic."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Charger Drifter",
                    "body_style": "2-door sports coupe",
                    "engine_code": "Hemi-265-CL",
                    "transmission": "4-speed manual (Borg-Warner)",
                    "drivetrain": "RWD",
                    "msrp_aud": 7150,
                    "power_kw": 151.0,
                    "torque_nm": 355.0,
                    "fuel_l_100km": 14.5,
                    "towing_braked_kg": 1300,
                    "notes": "The last Aussie Charger."
                }
            ]
        }
    ]
}

HSV_CLUBSPORT_GTS_DATA: Dict[str, Any] = {
    "make_slug": "hsv",
    "model_slug": "clubsport-gts",
    "name": "HSV ClubSport & GTS",
    "vehicle_type": "Sedan",
    "segment": "High-Performance Muscle Car",
    "years_sold_au": {"start": 1990, "end": 2017},
    "locally_built": True,
    "assembly_plants_au": [
        "Clayton, Victoria"
    ],
    "overview": "The HSV ClubSport and GTS formed the beating heart of Holden Special Vehicles from 1990 to 2017. Developed at HSV's performance facility in Clayton, Victoria, the ClubSport was HSV's top-selling performance sedan, while the GTS served as the technological flagship. From the original VN ClubSport and VP GTS (with 4-bolt mains and IRS) to the stroker 5.7L V8s, the 300kW Callaway C4B in the VT/VX, the E-Series Magnetic Ride Control, the supercharged 430kW LSA in GEN-F, and the crowning 2017 GTSR W1 (powered by the dry-sump 474kW Corvette ZR1 LS9 supercharged V8), this model line represents the pinnacle of Australian rear-wheel-drive muscle car engineering.",
    "australian_market_notes": "Created following HSV's successful homologation of the 1988 VL Walkinshaw, the ClubSport brought race-proven V8 power to everyday Australian enthusiasts. The GTS was introduced in 1992 on the VP series as the ultimate technology and speed flagship. Milestones included the 1996 VS GTS-R in 'XU3 Yellah' with carbon-fibre rear wing, the 2000 VT II GTS featuring a hand-built Callaway C4B 300kW V8, the 2006 E-Series Magnetic Ride Control active dampers, and the 2017 GTSR W1, which set the Australian production car power record with 474 kW (636 bhp) and 815 Nm of torque.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "VN-VP",
            "generation_name": "VN & VP Series",
            "years": {"start": 1990, "end": 1993},
            "body_styles": ["4-door performance sedan"],
            "platform": "GM V-body modified by HSV",
            "ancap_rating": None,
            "summary": "Birth of the ClubSport (VN, 180kW Holden 5.0L EFI V8) and the flagship VP GTS (200kW Holden/Walkinshaw V8 with 4-bolt mains, IRS, and AP brakes).",
            "engines": [
                {
                    "engine_code": "Holden-5.0L-HSV-180",
                    "name": "Holden/HSV 5.0L (304ci) EFI V8 (VN ClubSport)",
                    "displacement_cc": 4987,
                    "displacement_litres": 5.0,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Unleaded)",
                    "power_kw": 180.0,
                    "power_rpm": "4600",
                    "torque_nm": 400.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "OHV 16V",
                    "notes": "HSV cold-air intake and tuned Delco engine management."
                },
                {
                    "engine_code": "Holden-5000i-200kW",
                    "name": "Holden/Walkinshaw 5000i 5.0L V8 (VP GTS)",
                    "displacement_cc": 4987,
                    "displacement_litres": 5.0,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Premium)",
                    "power_kw": 200.0,
                    "power_rpm": "4800",
                    "torque_nm": 410.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "OHV 16V with 4-bolt main bearing caps",
                    "notes": "Bespoke high-performance 4-bolt main block; 200kW."
                }
            ],
            "badges": [
                {
                    "badge_name": "ClubSport",
                    "years": {"start": 1990, "end": 1993},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual (T5)", "4-speed automatic (TH700)"],
                    "msrp_aud_min": 33320,
                    "msrp_aud_max": 38900,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1410,
                    "standard_features": ["180kW V8", "HSV sports suspension", "16-inch alloy wheels", "Sports seats", "HSV body styling"],
                    "notes": "HSV's perennial volume champion."
                },
                {
                    "badge_name": "GTS",
                    "years": {"start": 1992, "end": 1993},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual (T5G)", "4-speed auto"],
                    "msrp_aud_min": 53750,
                    "msrp_aud_max": 58000,
                    "fuel_consumption_l_100km": 13.5,
                    "kerb_weight_kg": 1475,
                    "standard_features": ["200kW 5000i V8 with 4-bolt mains", "Independent Rear Suspension (IRS)", "ABS brakes", "17-inch alloy wheels", "Devon leather trim"],
                    "notes": "First HSV GTS; 130 units produced."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GTS",
                    "body_style": "4-door sedan",
                    "engine_code": "Holden-5000i-200kW",
                    "transmission": "5-speed manual (T5G)",
                    "drivetrain": "RWD",
                    "msrp_aud": 53750,
                    "power_kw": 200.0,
                    "torque_nm": 410.0,
                    "fuel_l_100km": 13.5,
                    "towing_braked_kg": 1500,
                    "notes": "0-100 km/h in 6.5s; 240 km/h top speed."
                }
            ]
        },
        {
            "series_code": "E-Series",
            "generation_name": "E-Series (E1, E2, E3)",
            "years": {"start": 2006, "end": 2013},
            "body_styles": ["4-door sedan", "5-door Sportwagon (Tourer)"],
            "platform": "GM Zeta platform modified by HSV",
            "ancap_rating": "5 Stars",
            "summary": "Zeta platform flagship; LS2 6.0L (307kW) and LS3 6.2L (317kW/325kW) V8s; groundbreaking Magnetic Ride Control (MRC) suspension; bi-modal exhaust system.",
            "engines": [
                {
                    "engine_code": "LS3-6.2-HSV-325",
                    "name": "Chevrolet LS3 6.2L V8 (GTS E3)",
                    "displacement_cc": 6162,
                    "displacement_litres": 6.2,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 325.0,
                    "power_rpm": "6000",
                    "torque_nm": 550.0,
                    "torque_rpm": "4600",
                    "compression_ratio": "10.7:1",
                    "valvetrain": "OHV 16V with Bi-Modal Intake & Exhaust",
                    "notes": "High-output LS3 V8; 0-100 km/h in 4.9s."
                }
            ],
            "badges": [
                {
                    "badge_name": "ClubSport R8",
                    "years": {"start": 2006, "end": 2013},
                    "body_styles": ["4-door sedan", "5-door Sportwagon"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual (Tremec TR-6060)", "6-speed automatic (6L80-E)"],
                    "msrp_aud_min": 65990,
                    "msrp_aud_max": 73500,
                    "fuel_consumption_l_100km": 13.9,
                    "kerb_weight_kg": 1800,
                    "standard_features": ["317kW/325kW LS3 V8", "AP Racing 4-piston brakes", "19-inch alloys", "Competition Mode ESC", "Sports bucket seats"],
                    "notes": "The standard of Australian high-performance."
                },
                {
                    "badge_name": "GTS",
                    "years": {"start": 2006, "end": 2013},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual (TR-6060)", "6-speed auto"],
                    "msrp_aud_min": 78990,
                    "msrp_aud_max": 86500,
                    "fuel_consumption_l_100km": 14.2,
                    "kerb_weight_kg": 1830,
                    "standard_features": ["325kW LS3 V8", "Magnetic Ride Control (MRC) active dampers", "20-inch forged wheels", "HSV Performance Data Interface (EDI)", "Bi-modal active exhaust"],
                    "notes": "Advanced technological muscle flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GTS",
                    "body_style": "4-door sedan",
                    "engine_code": "LS3-6.2-HSV-325",
                    "transmission": "6-speed manual (TR-6060)",
                    "drivetrain": "RWD",
                    "msrp_aud": 82990,
                    "power_kw": 325.0,
                    "torque_nm": 550.0,
                    "fuel_l_100km": 14.2,
                    "towing_braked_kg": 2100,
                    "notes": "MRC suspension and track-ready performance."
                }
            ]
        },
        {
            "series_code": "GEN-F",
            "generation_name": "GEN-F & GEN-F2 (GTS & GTSR W1)",
            "years": {"start": 2013, "end": 2017},
            "body_styles": ["4-door performance sedan"],
            "platform": "GM Zeta platform lightened by HSV",
            "ancap_rating": "5 Stars",
            "summary": "The ultimate Australian high-performance era. Supercharged 6.2L LSA V8 (430kW/740Nm) in GTS, and the crowning GTSR W1 powered by the Corvette ZR1's dry-sump 474kW (636hp) supercharged LS9 V8, Tremec TR-6060 manual, and Supashock racing suspension.",
            "engines": [
                {
                    "engine_code": "Supercharged-6.2-LSA",
                    "name": "Chevrolet 6.2L Supercharged LSA V8 (GTS)",
                    "displacement_cc": 6162,
                    "displacement_litres": 6.2,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Supercharged",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 430.0,
                    "power_rpm": "6150",
                    "torque_nm": 740.0,
                    "torque_rpm": "3850",
                    "compression_ratio": "9.1:1",
                    "valvetrain": "OHV 16V with Eaton 1.9L Roots Supercharger",
                    "notes": "Integrated liquid-to-air intercooler; 0-100 km/h in 4.4 seconds."
                },
                {
                    "engine_code": "Supercharged-6.2-LS9",
                    "name": "Chevrolet 6.2L Supercharged LS9 V8 (GTSR W1)",
                    "displacement_cc": 6162,
                    "displacement_litres": 6.2,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Supercharged",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 474.0,
                    "power_rpm": "6500",
                    "torque_nm": 815.0,
                    "torque_rpm": "3900",
                    "compression_ratio": "9.1:1",
                    "valvetrain": "OHV 16V Titanium Intake Valves & Connecting Rods",
                    "notes": "Hand-built dry-sump LS9 with 2.3L Eaton supercharger; 636 bhp / 815 Nm; most powerful Australian production car in history."
                }
            ],
            "badges": [
                {
                    "badge_name": "GTS",
                    "years": {"start": 2013, "end": 2017},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual (TR-6060)", "6-speed heavy-duty auto (6L90-E)"],
                    "msrp_aud_min": 92990,
                    "msrp_aud_max": 99990,
                    "fuel_consumption_l_100km": 15.3,
                    "kerb_weight_kg": 1886,
                    "standard_features": ["430kW LSA Supercharged V8", "AP Racing 6-piston front brakes", "Generation 3 Magnetic Ride Control", "Torque Vectoring", "20-inch forged alloys", "Head-Up Display"],
                    "notes": "World-class supercar performance sedan."
                },
                {
                    "badge_name": "GTSR W1",
                    "years": {"start": 2017, "end": 2017},
                    "body_styles": ["4-door supercar sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed close-ratio manual (Tremec TR-6060 MH3)"],
                    "msrp_aud_min": 169990,
                    "msrp_aud_max": 180000,
                    "fuel_consumption_l_100km": 16.5,
                    "kerb_weight_kg": 1895,
                    "standard_features": ["474kW LS9 dry-sump V8", "Supashock motorsport dampers", "AP Racing 410mm front disc brakes", "Pirelli P-Zero Trofeo R semi-slick tyres", "Carbon-fibre airbox, front fender vents, and rear spoiler", "Alcantara/leather racing seats"],
                    "notes": "The apex of Australian automotive manufacturing; only 275 produced; 0-100 km/h in 4.2s."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GTSR W1",
                    "body_style": "4-door supercar sedan",
                    "engine_code": "Supercharged-6.2-LS9",
                    "transmission": "6-speed close-ratio manual (Tremec TR-6060 MH3)",
                    "drivetrain": "RWD",
                    "msrp_aud": 169990,
                    "power_kw": 474.0,
                    "torque_nm": 815.0,
                    "fuel_l_100km": 16.5,
                    "towing_braked_kg": 1600,
                    "notes": "474kW / 815Nm; Australia's ultimate road and track masterpiece."
                }
            ]
        }
    ]
}

FPV_GT_F6_DATA: Dict[str, Any] = {
    "make_slug": "fpv",
    "model_slug": "gt-f6",
    "name": "FPV GT & F6",
    "vehicle_type": "Sedan",
    "segment": "High-Performance Muscle Car",
    "years_sold_au": {"start": 2003, "end": 2014},
    "locally_built": True,
    "assembly_plants_au": [
        "Campbellfield, Victoria"
    ],
    "overview": "The FPV GT and F6 were Ford Performance Vehicles' crowning high-performance icons. Developed in Campbellfield, Victoria by Ford Australia and Prodrive, this duo formed the greatest domestic performance confrontation in Australian history against HSV. The GT revived Ford's iconic muscle heritage with the quad-cam 32-valve Boss 290 and Boss 315 V8s, before adopting the supercharged 5.0L 'Miami' V8 and culminating in the 2014 GT-F 351 (delivering over 400kW on overboost). Concurrently, the F6 Typhoon transformed Australian performance perceptions with its devastating turbocharged Barra 4.0-litre straight-six, producing up to 565Nm of flat-line torque and supercar acceleration.",
    "australian_market_notes": "The BA GT launched in March 2003 with the Boss 290—an engine created specifically for Australia by marrying an American 5.4L cast-iron block with quad-cam 32-valve heads from the Mustang Cobra R. In October 2004, FPV shocked the Australian market with the F6 Typhoon, packing an enormous front-mount intercooler and 270kW/550Nm of Barra Turbo grunt that out-torqued contemporary V8s. In 2010, FPV engineered the 'Miami' supercharged 5.0L V8 in Melbourne at a cost of $40 million, featuring an Australian Harrop supercharger with inverted manifold and twin water-to-air intercoolers. The FPV journey signed off in 2014 with 500 numbered GT-F 351 sedans.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "BA-BF",
            "generation_name": "BA & BF Series (Boss 290 & F6 Typhoon)",
            "years": {"start": 2003, "end": 2008},
            "body_styles": ["4-door performance sedan"],
            "platform": "Ford EA169 modified by FPV",
            "ancap_rating": "4 Stars",
            "summary": "Inaugural FPV generation. Boss 290 5.4L quad-cam 32V V8 (290kW/520Nm), Tremec T56 manual and ZF 6-speed auto; introduction of the legendary F6 Typhoon (270kW/550Nm).",
            "engines": [
                {
                    "engine_code": "Boss-290",
                    "name": "Boss 290 5.4L DOHC 32V Modular V8",
                    "displacement_cc": 5408,
                    "displacement_litres": 5.4,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 290.0,
                    "power_rpm": "5500",
                    "torque_nm": 520.0,
                    "torque_rpm": "4500",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 32V Quad-Cam",
                    "notes": "Hand-assembled in Campbellfield; high-flow Cobra R cylinder heads."
                },
                {
                    "engine_code": "Barra-270T-F6",
                    "name": "Barra 270T 4.0L DOHC Turbo Inline-6 (F6)",
                    "displacement_cc": 3984,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 270.0,
                    "power_rpm": "5250",
                    "torque_nm": 550.0,
                    "torque_rpm": "2000-4250",
                    "compression_ratio": "8.7:1",
                    "valvetrain": "DOHC 24V DIVCT Garrett GT3582R Turbo",
                    "notes": "Class-leading 550Nm torque; 0-100 km/h in 5.4s."
                }
            ],
            "badges": [
                {
                    "badge_name": "GT / GT-P",
                    "years": {"start": 2003, "end": 2008},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed/6-speed manual (Tremec T56)", "4-speed auto / ZF 6-speed auto"],
                    "msrp_aud_min": 59810,
                    "msrp_aud_max": 71990,
                    "fuel_consumption_l_100km": 15.0,
                    "kerb_weight_kg": 1825,
                    "standard_features": ["Boss 290 V8", "Brembo brakes (4-piston front on GT; 6-piston on GT-P)", "19-inch alloy wheels", "FPV sports seats", "FPV sports steering wheel", "Historic 1970s GT side stripes"],
                    "notes": "Revived the legendary Ford Falcon GT."
                },
                {
                    "badge_name": "F6 Typhoon",
                    "years": {"start": 2004, "end": 2008},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual (T56)", "ZF 6-speed automatic"],
                    "msrp_aud_min": 58990,
                    "msrp_aud_max": 65990,
                    "fuel_consumption_l_100km": 12.5,
                    "kerb_weight_kg": 1780,
                    "standard_features": ["270kW Barra Turbo six", "Massive front-mount intercooler", "AP Racing / Brembo brakes", "F6 sports instrumentation with turbo boost gauge", "18-inch/19-inch alloys"],
                    "notes": "Australia's six-cylinder muscle king."
                }
            ],
            "configurations": [
                {
                    "badge_name": "F6 Typhoon",
                    "body_style": "4-door sedan",
                    "engine_code": "Barra-270T-F6",
                    "transmission": "ZF 6-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 61990,
                    "power_kw": 270.0,
                    "torque_nm": 550.0,
                    "fuel_l_100km": 12.5,
                    "towing_braked_kg": 2300,
                    "notes": "Devastating real-world acceleration."
                }
            ]
        },
        {
            "series_code": "FG-II",
            "generation_name": "FG Series II & GT-F 351 (Supercharged Miami V8 & F6 310)",
            "years": {"start": 2010, "end": 2014},
            "body_styles": ["4-door performance sedan"],
            "platform": "Ford Orion platform modified by FPV",
            "ancap_rating": "5 Stars",
            "summary": "Peak of FPV engineering. Australian-developed 5.0L Supercharged 'Miami' V8 (335kW in GT; 351kW / 400kW+ overboost in GT-F 351), alongside the F6 310 (310kW/565Nm) with Garrett GT3576R turbo.",
            "engines": [
                {
                    "engine_code": "Miami-Supercharged-335",
                    "name": "Miami 5.0L Supercharged 32V V8 (GT & GT-P)",
                    "displacement_cc": 4951,
                    "displacement_litres": 5.0,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Supercharged",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 335.0,
                    "power_rpm": "5750",
                    "torque_nm": 570.0,
                    "torque_rpm": "2200-5500",
                    "compression_ratio": "9.25:1",
                    "valvetrain": "DOHC 32V with Harrop HTV 1900 Supercharger",
                    "notes": "All-aluminium block, twin high-efficiency water-to-air intercoolers."
                },
                {
                    "engine_code": "Miami-GT-F-351",
                    "name": "Miami 5.0L Supercharged 32V V8 (GT-F 351)",
                    "displacement_cc": 4951,
                    "displacement_litres": 5.0,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Supercharged",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 351.0,
                    "power_rpm": "6000",
                    "torque_nm": 570.0,
                    "torque_rpm": "2500-5500",
                    "compression_ratio": "9.25:1",
                    "valvetrain": "DOHC 32V Supercharged",
                    "notes": "351kW paying homage to the 351 Cleveland; delivers over 400kW and 650Nm on overboost; 0-100 km/h in 4.5 seconds."
                },
                {
                    "engine_code": "Barra-310T-F6",
                    "name": "Barra 310T 4.0L DOHC 24V Turbo Inline-6",
                    "displacement_cc": 3984,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 310.0,
                    "power_rpm": "5500",
                    "torque_nm": 565.0,
                    "torque_rpm": "1950-5200",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "DOHC 24V Garrett GT3576R Turbocharger",
                    "notes": "Massive 565Nm flat torque plateau; 0-100 km/h in 4.9s."
                }
            ],
            "badges": [
                {
                    "badge_name": "GT-F 351",
                    "years": {"start": 2014, "end": 2014},
                    "body_styles": ["4-door performance sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual (Tremec TR-6060)", "ZF 6-speed automatic"],
                    "msrp_aud_min": 77990,
                    "msrp_aud_max": 82000,
                    "fuel_consumption_l_100km": 13.6,
                    "kerb_weight_kg": 1827,
                    "standard_features": ["351kW Miami Supercharged V8", "Overboost to 400kW+", "Brembo 6-piston front brakes", "Staggered 9-inch rear alloy wheels with 275 tyres", "Historic black matte stripes", "Numbered build badge"],
                    "notes": "Final FPV Falcon GT; 500 numbered units for Australia; sold out in hours."
                },
                {
                    "badge_name": "F6",
                    "years": {"start": 2008, "end": 2014},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual (TR-6060)", "ZF 6-speed automatic (6HP26)"],
                    "msrp_aud_min": 64890,
                    "msrp_aud_max": 68990,
                    "fuel_consumption_l_100km": 12.1,
                    "kerb_weight_kg": 1805,
                    "standard_features": ["310kW Barra Turbo six", "Brembo brakes", "Launch control", "Graphite accents", "Dual-zone climate control"],
                    "notes": "The fastest accelerating Australian six-cylinder sedan."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GT-F 351",
                    "body_style": "4-door performance sedan",
                    "engine_code": "Miami-GT-F-351",
                    "transmission": "ZF 6-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 77990,
                    "power_kw": 351.0,
                    "torque_nm": 570.0,
                    "fuel_l_100km": 13.6,
                    "towing_braked_kg": 2300,
                    "notes": "400kW+ overboost; the ultimate Falcon GT."
                },
                {
                    "badge_name": "F6",
                    "body_style": "4-door sedan",
                    "engine_code": "Barra-310T-F6",
                    "transmission": "ZF 6-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 66890,
                    "power_kw": 310.0,
                    "torque_nm": 565.0,
                    "fuel_l_100km": 12.1,
                    "towing_braked_kg": 2300,
                    "notes": "565Nm of turbocharged torque."
                }
            ]
        }
    ]
}
