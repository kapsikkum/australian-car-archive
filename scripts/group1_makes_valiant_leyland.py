"""
Chrysler/Valiant Australia and Leyland/BMC Australia historical data and complete model catalogs.
"""
from typing import Any, Dict

CHRYSLER_VALIANT_DATA: Dict[str, Any] = {
    "make_slug": "chrysler-valiant",
    "name": "Chrysler / Valiant Australia",
    "country_of_origin": "Australia",
    "years_active_au": {"start": 1951, "end": 2021},
    "currently_sold_au": False,
    "local_manufacturer": True,
    "overview": "Chrysler Australia Ltd was established in June 1951 following Chrysler Corporation's acquisition of Adelaide coachbuilder Richards Industries. Operating from its monumental manufacturing complex at Tonsley Park and engine foundry at Lonsdale in South Australia, Chrysler was the third of the 'Big Three' Australian domestic automakers alongside Holden and Ford. In January 1962, Chrysler launched the revolutionary Valiant (R-Series), whose 145 hp Slant-6 engine instantly out-accelerated and outperformed every rival on Australian roads. In 1970, Chrysler Australia's local engineering team created the iconic HEMI-6 engine, featuring hemispherical combustion chambers and producing massive torque. The following year, Chrysler introduced the VH Valiant Charger—backed by the unforgettable 'Hey Charger!' advertising campaign—whose triple-Weber E49 'Six Pack' became the fastest-accelerating Australian production car for over a decade. Facing financial distress in the late 1970s, Chrysler Australia sold its operations to Mitsubishi Motors Corporation in 1980, creating Mitsubishi Motors Australia Limited (MMAL). The Chrysler brand was later re-introduced as an American import arm (300C, PT Cruiser, Voyager) before departing Australia in 2021.",
    "australian_history": "Chrysler's Australian heritage began in the 1920s through T.J. Richards & Sons, an Adelaide coachbuilder constructing bodies for Dodge, DeSoto, and Plymouth chassis. In June 1951, Chrysler Corporation acquired Richards Industries to establish Chrysler Australia Ltd, based initially at Mile End and Keswick. In 1957, Chrysler introduced the Chrysler Royal (AP1, AP2, AP3), an Australian-unique evolution of 1953-54 Plymouth architecture featuring flamboyant tail fins and push-button automatic transmissions.\n\nIn January 1962, Chrysler dramatically altered the Australian automotive landscape by assembling 1,008 units of the American compact Plymouth Valiant as the 'R-Series'. Powered by a 225 cubic-inch (3.7-litre) 'Slant-6' engine producing 145 bhp, it completely outclassed the 75 bhp Holden EK and 85 bhp Ford Falcon, selling out within days. In 1963, Chrysler opened its sprawling, billion-dollar Tonsley Park plant in suburban Adelaide and introduced the first fully manufactured Australian Valiant, the AP5 (Australian Production 5), followed by the AP6 which introduced the 273ci V8—the first V8 offered in an Australian family car.\n\nUnder chief engineer David Giles, Chrysler Australia invested $22 million developing an all-new six-cylinder engine tailored for Australian conditions. Debuting in the 1970 VG series, the HEMI-6 (available in 215ci, 245ci, and 265ci displacements) eliminated the pushrod angles of conventional OHV engines and incorporated hemispherical combustion chambers, yielding immense volumetric efficiency. In August 1971, Chrysler launched the VH series—the first Valiant designed and styled completely in Australia—headlined by the short-wheelbase Valiant Charger coupe. Engineered by John Ellis, the Charger won the 1971 Wheels Car of the Year and spawned the homologation specials E38 (280 bhp) and the legendary E49 (302 bhp, triple twin-choke Weber 45 DCOE carburettors, 4-speed Borg-Warner manual). The E49 Charger held the Australian production car quarter-mile record (14.4 seconds) for over a decade.\n\nIn the mid-1970s, Chrysler introduced the Centura (KB/KC), grafting the Australian Hemi-6 into the French Simca 180 bodyshell. However, high development costs, the 1973 oil crisis, and parent Chrysler Corporation's financial crisis forced restructuring. In 1979-1980, Mitsubishi Corporation acquired Chrysler Australia's Tonsley Park and Lonsdale facilities, transitioning production to the Chrysler Sigma and Colt before renaming the company Mitsubishi Motors Australia Limited (MMAL) in October 1980. The last Australian Valiant—a silver CM Regal sedan—rolled off the Tonsley Park line on 28 August 1981. In 1994, Chrysler returned to Australia as an importer under Chrysler/DaimlerChrysler/FCA, enjoying major success with the Chrysler 300C large sedan, PT Cruiser, Crossfire, and Grand Voyager before retiring the brand in Australia in November 2021.",
    "models_catalog": [
        {
            "model_slug": "chrysler-royal",
            "name": "Chrysler Royal",
            "vehicle_type": "Sedan / Wagon",
            "segment": "Large / Luxury",
            "years_sold_au": {"start": 1957, "end": 1963},
            "locally_built": True,
            "overview": "Locally developed luxury flagship combining 1954 Plymouth body pressings with sweeping tail fins, dual headlamps, and push-button automatic transmission across AP1, AP2, and AP3 series.",
            "generations": [
                {
                    "series_code": "AP1-AP3",
                    "generation_name": "Royal AP1, AP2, AP3 Series",
                    "years": {"start": 1957, "end": 1963},
                    "body_styles": ["4-door sedan", "5-door wagon (Plainsman)", "Coupe utility (Wayfarer)"],
                    "summary": "230ci/250ci side-valve inline-six and 313ci Canadian polyspheric V8; push-button PowerFlite/TorqueFlite automatic."
                }
            ]
        },
        {
            "model_slug": "dodge-phoenix",
            "name": "Dodge Phoenix",
            "vehicle_type": "Sedan / Hardtop",
            "segment": "Upper Luxury",
            "years_sold_au": {"start": 1960, "end": 1972},
            "locally_built": True,
            "overview": "Full-size American cruiser assembled in Adelaide from Canadian CKD kits with factory RHD dashboards, serving as Chrysler Australia's prestige competitor to the Ford Galaxie and Chevrolet Impala.",
            "generations": [
                {
                    "series_code": "PD4-DH",
                    "generation_name": "Dodge Phoenix Series",
                    "years": {"start": 1960, "end": 1972},
                    "body_styles": ["4-door sedan", "4-door hardtop"],
                    "summary": "318ci and 383ci V8 engines, Torqueflite automatic, opulent American luxury proportions."
                }
            ]
        },
        {
            "model_slug": "valiant",
            "name": "Chrysler Valiant",
            "vehicle_type": "Sedan / Wagon",
            "segment": "Large",
            "years_sold_au": {"start": 1962, "end": 1981},
            "locally_built": True,
            "overview": "The great challenger of the Australian family car market. Spanning R, S, AP5, AP6, VC, VE, VF, VG, VH, VJ, VK, CL, and CM series, powered by the mighty Slant-6 and Australian-engineered Hemi-6.",
            "generations": [
                {
                    "series_code": "R-S",
                    "generation_name": "R and S Series",
                    "years": {"start": 1962, "end": 1963},
                    "body_styles": ["4-door sedan"],
                    "summary": "Introduced the 225ci (3.7L) Slant-6 with 145 hp, setting new Australian performance benchmarks."
                },
                {
                    "series_code": "AP5-AP6",
                    "generation_name": "AP5 & AP6 Series",
                    "years": {"start": 1963, "end": 1966},
                    "body_styles": ["Sedan", "Safari Wagon"],
                    "summary": "First completely Australian-manufactured Valiant at Tonsley Park; AP6 introduced first V8 in an Australian family car (273ci V8)."
                },
                {
                    "series_code": "VC-VE",
                    "generation_name": "VC & VE Series",
                    "years": {"start": 1966, "end": 1969},
                    "body_styles": ["Sedan", "Wagon"],
                    "summary": "Crisp modern lines; VC won 1966 Wheels Car of the Year; VE introduced the luxury VIP nameplate."
                },
                {
                    "series_code": "VF-VG",
                    "generation_name": "VF & VG Series",
                    "years": {"start": 1969, "end": 1971},
                    "body_styles": ["Sedan", "Wagon", "Hardtop Coupe"],
                    "summary": "VF introduced the 2-door Hardtop and Regal 770; VG debuted the revolutionary Australian-engineered HEMI-6 (215 and 245ci)."
                },
                {
                    "series_code": "VH-VJ",
                    "generation_name": "VH & VJ Series",
                    "years": {"start": 1971, "end": 1975},
                    "body_styles": ["Sedan", "Wagon"],
                    "summary": "All-Australian wide-body design; Hemi 215, 245, 265, and 318/340 V8s; Ranger, Regal, and Regal 770."
                },
                {
                    "series_code": "VK-CM",
                    "generation_name": "VK, CL & CM Series",
                    "years": {"start": 1975, "end": 1981},
                    "body_styles": ["Sedan", "Wagon"],
                    "summary": "CL restyled front; CM introduced Electronic Lean Burn (ELB) computer-controlled spark advance on Hemi 4.0L and 4.3L sixes with exceptional fuel economy."
                }
            ]
        },
        {
            "model_slug": "charger",
            "name": "Chrysler Valiant Charger",
            "vehicle_type": "Coupe",
            "segment": "Sports Coupe / Muscle Car",
            "years_sold_au": {"start": 1971, "end": 1978},
            "locally_built": True,
            "overview": "One of Australia's most charismatic muscle cars. Built on a shortened 105-inch wheelbase with sensational fastback styling, winning 1971 Wheels Car of the Year and immortalized by the 302 bhp E49 Six Pack.",
            "generations": [
                {
                    "series_code": "VH",
                    "generation_name": "VH Charger Series",
                    "years": {"start": 1971, "end": 1973},
                    "body_styles": ["2-door sports coupe"],
                    "summary": "1971 Wheels COTY winner; 'Hey Charger!' phenomenon; E37, E38 (280 bhp) and Bathurst homologation E49 (302 bhp, 3x Weber, 4-speed manual)."
                },
                {
                    "series_code": "VJ-VK",
                    "generation_name": "VJ & VK Charger Series",
                    "years": {"start": 1973, "end": 1976},
                    "body_styles": ["2-door sports coupe"],
                    "summary": "Round headlamps, Sportsman special edition, E48 4-speed 265 Hemi, and 318 V8."
                },
                {
                    "series_code": "CL",
                    "generation_name": "CL Charger Series",
                    "years": {"start": 1976, "end": 1978},
                    "body_styles": ["2-door sports coupe"],
                    "summary": "Final Charger generation; 770 trim and bold Drifter pack with side stripes and roof rack; 265 Hemi and 318 V8."
                }
            ]
        },
        {
            "model_slug": "valiant-utility",
            "name": "Chrysler Valiant Utility",
            "vehicle_type": "Coupe Utility",
            "segment": "Commercial",
            "years_sold_au": {"start": 1965, "end": 1979},
            "locally_built": True,
            "overview": "Chrysler Australia's rugged coupe utility (Wayfarer and Valiant Utility) matching Holden and Falcon utes with superior Slant-6 and Hemi-6 hauling power.",
            "generations": [
                {
                    "series_code": "AP5-CL-Ute",
                    "generation_name": "Valiant Utility (AP5 to CL)",
                    "years": {"start": 1965, "end": 1979},
                    "body_styles": ["2-door coupe utility"],
                    "summary": "Spanned 14 years with Slant-6, Hemi-6 (245/265), and 318 V8 engines; famous Dodge Utility and CL Drifter Ute packs."
                }
            ]
        },
        {
            "model_slug": "centura",
            "name": "Chrysler Centura",
            "vehicle_type": "Sedan",
            "segment": "Mid-size",
            "years_sold_au": {"start": 1975, "end": 1978},
            "locally_built": True,
            "overview": "Mid-size sedan mating French Chrysler-Simca 180 bodies with Australia's massive 3.5L (215) and 4.0L (245) Hemi-6 engines, creating an accidental muscle car.",
            "generations": [
                {
                    "series_code": "KB-KC",
                    "generation_name": "Centura KB & KC Series",
                    "years": {"start": 1975, "end": 1978},
                    "body_styles": ["4-door sedan"],
                    "summary": "Simca 2.0L 4-cylinder and Australian 3.5L/4.0L Hemi-6 engines; GL and sporty GLX trims."
                }
            ]
        },
        {
            "model_slug": "galant",
            "name": "Chrysler Galant",
            "vehicle_type": "Sedan / Coupe / Wagon",
            "segment": "Compact",
            "years_sold_au": {"start": 1971, "end": 1977},
            "locally_built": True,
            "overview": "First collaboration between Chrysler Australia and Mitsubishi Motors, assembled at Tonsley Park with Saturn and Astron 4-cylinder engines.",
            "generations": [
                {
                    "series_code": "GA-GD",
                    "generation_name": "Galant GA, GB, GC, GD Series",
                    "years": {"start": 1971, "end": 1977},
                    "body_styles": ["4-door sedan", "2-door hardtop coupe", "5-door wagon"],
                    "summary": "1.3L, 1.4L, and 1.6L Saturn engines, followed by 2.0L Astron; high build quality and rallying success."
                }
            ]
        },
        {
            "model_slug": "sigma",
            "name": "Chrysler Sigma",
            "vehicle_type": "Sedan / Wagon",
            "segment": "Mid-size",
            "years_sold_au": {"start": 1977, "end": 1980},
            "locally_built": True,
            "overview": "Sensational sales hit engineered by Chrysler Australia and Mitsubishi, featuring the silky smooth counterbalanced 'Silent Shaft' Astron engine.",
            "generations": [
                {
                    "series_code": "GE-GH",
                    "generation_name": "Chrysler Sigma (GE, GH)",
                    "years": {"start": 1977, "end": 1980},
                    "body_styles": ["4-door sedan", "5-door wagon"],
                    "summary": "1.6L Saturn and 1.85L/2.0L/2.6L Astron engines; SE and Peter Brown special editions; paved the way for MMAL."
                }
            ]
        },
        {
            "model_slug": "scorpion",
            "name": "Chrysler Scorpion",
            "vehicle_type": "Coupe",
            "segment": "Sports Coupe",
            "years_sold_au": {"start": 1978, "end": 1980},
            "locally_built": False,
            "overview": "Stylish 2-door pillarless sports coupe based on the Mitsubishi Sapporo, offering luxury grand-touring features.",
            "generations": [
                {
                    "series_code": "GE-GH",
                    "generation_name": "Chrysler Scorpion (GE, GH)",
                    "years": {"start": 1978, "end": 1980},
                    "body_styles": ["2-door coupe"],
                    "summary": "2.0L and 2.6L Astron engines with balance shafts, 5-speed manual or 3-speed auto, 4-wheel disc brakes."
                }
            ]
        },
        {
            "model_slug": "chrysler-300c",
            "name": "Chrysler 300C",
            "vehicle_type": "Sedan / Wagon",
            "segment": "Large / Luxury",
            "years_sold_au": {"start": 2005, "end": 2021},
            "locally_built": False,
            "overview": "Brawny American rear-wheel-drive luxury sedan with gangsta proportions, packing 5.7L Hemi V8 and 6.4L SRT-8 performance.",
            "generations": [
                {
                    "series_code": "LX-LD",
                    "generation_name": "Chrysler 300C (LX & LD)",
                    "years": {"start": 2005, "end": 2021},
                    "body_styles": ["4-door sedan", "Touring wagon"],
                    "summary": "3.5L/3.6L Pentastar V6, 3.0L CRD diesel, 5.7L Hemi V8, and 350kW 6.4L Hemi V8 SRT; final rear-drive V8 rival to Falcon and Commodore."
                }
            ]
        },
        {
            "model_slug": "pt-cruiser",
            "name": "Chrysler PT Cruiser",
            "vehicle_type": "Hatchback",
            "segment": "Retro Compact",
            "years_sold_au": {"start": 2000, "end": 2010},
            "locally_built": False,
            "overview": "Retro-styled multi-purpose hatchback inspired by 1930s American hot rods, featuring versatile seating and cabriolet option.",
            "generations": [
                {
                    "series_code": "PT",
                    "generation_name": "PT Cruiser Series",
                    "years": {"start": 2000, "end": 2010},
                    "body_styles": ["5-door hatchback", "2-door cabriolet"],
                    "summary": "2.0L and 2.4L petrol engines, 2.4L Turbo GT (164kW), 25-way interior seat combinations."
                }
            ]
        },
        {
            "model_slug": "crossfire",
            "name": "Chrysler Crossfire",
            "vehicle_type": "Coupe / Roadster",
            "segment": "Sports Car",
            "years_sold_au": {"start": 2003, "end": 2008},
            "locally_built": False,
            "overview": "Striking German-built sports car manufactured by Karmann in Osnabruck, sharing 80% of its components with the Mercedes-Benz SLK (R170).",
            "generations": [
                {
                    "series_code": "ZH",
                    "generation_name": "Crossfire ZH Series",
                    "years": {"start": 2003, "end": 2008},
                    "body_styles": ["2-door coupe", "2-door roadster"],
                    "summary": "Mercedes 3.2L 18-valve V6 (160kW) and supercharged SRT-6 (246kW), speed-sensitive deployable rear spoiler."
                }
            ]
        },
        {
            "model_slug": "voyager",
            "name": "Chrysler Voyager / Grand Voyager",
            "vehicle_type": "People Mover",
            "segment": "Large MPV",
            "years_sold_au": {"start": 1997, "end": 2014},
            "locally_built": False,
            "overview": "The pioneer of the modern minivan, offering Stow 'n Go fold-into-the-floor seating and power sliding doors across GS, RG, and RT generations.",
            "generations": [
                {
                    "series_code": "GS-RT",
                    "generation_name": "Voyager GS, RG, RT Series",
                    "years": {"start": 1997, "end": 2014},
                    "body_styles": ["5-door people mover"],
                    "summary": "3.3L and 3.8L V6 petrol, 2.8L CRD turbo-diesel, Stow 'n Go seating system."
                }
            ]
        },
        {
            "model_slug": "sebring",
            "name": "Chrysler Sebring",
            "vehicle_type": "Sedan / Cabriolet",
            "segment": "Mid-size",
            "years_sold_au": {"start": 2007, "end": 2010},
            "locally_built": False,
            "overview": "American mid-size car offered in four-door sedan and two-door cabriolet featuring a three-piece folding steel hardtop.",
            "generations": [
                {
                    "series_code": "JS",
                    "generation_name": "Sebring JS Series",
                    "years": {"start": 2007, "end": 2010},
                    "body_styles": ["4-door sedan", "2-door cabriolet"],
                    "summary": "2.4L World Gas Engine and 2.7L V6 petrol; retractable hardtop cabriolet."
                }
            ]
        },
        {
            "model_slug": "neon",
            "name": "Chrysler Neon",
            "vehicle_type": "Sedan",
            "segment": "Small",
            "years_sold_au": {"start": 1996, "end": 2002},
            "locally_built": False,
            "overview": "Cab-forward American compact car with perky performance from its standard 2.0L 16-valve engine.",
            "generations": [
                {
                    "series_code": "PL",
                    "generation_name": "Neon PL Series",
                    "years": {"start": 1996, "end": 2002},
                    "body_styles": ["4-door sedan"],
                    "summary": "2.0L SOHC (98kW) and DOHC (112kW) engines, frameless door glass, SE and LE trims."
                }
            ]
        }
    ]
}

LEYLAND_AUSTRALIA_DATA: Dict[str, Any] = {
    "make_slug": "leyland-australia",
    "name": "Leyland / BMC Australia",
    "country_of_origin": "Australia",
    "years_active_au": {"start": 1950, "end": 1982},
    "currently_sold_au": False,
    "local_manufacturer": True,
    "overview": "The British Motor Corporation (Australia) and later Leyland Australia was a major domestic automotive manufacturer operating from its sprawling, integrated 60-acre manufacturing plant at Victoria Park / Zetland in Sydney, New South Wales. In the 1950s and 1960s, BMC Australia was the third major force in Australian motoring, engineering unique local adaptations like the Morris Major, Austin Freeway, Austin 1800 'Landcrab' and Ute, and the iconic Australian-designed Mini Moke. In the early 1970s, under managing director Peter North, Leyland Australia invested $21 million to take on Holden and Ford directly with a clean-sheet Australian full-size car: the Leyland P76. Designed by Michelotti with an advanced all-alloy 4.4-litre V8, McPherson strut suspension, and a boot capable of swallowing a 44-gallon drum, the P76 won the 1973 Wheels Car of the Year. However, quality issues during early production, component supply strikes, the 1973 oil crisis, and parent company British Leyland's UK collapse forced the closure of Zetland in late 1974, ending one of Australia's most daring manufacturing chapters.",
    "australian_history": "BMC's Australian presence solidified in 1952 when the British Motor Corporation was formed by the merger of Austin and Morris. BMC took over the former Victoria Park racecourse in Zetland, Sydney, transforming it into a complete vehicle production complex with press shops, engine machining, and assembly lines. BMC Australia developed vehicles specifically for harsh local conditions, debuting the Morris Major and Austin Lancer in 1958, and the 1962 Austin Freeway powered by a local 2.4-litre 'Blue Streak' six-cylinder derived from the B-series.\n\nZetland also built the legendary Alec Issigonis-designed Mini from 1961, with local innovations including wind-up windows (long before the UK), rotating front quarter-vent windows, and cable-operated door openers on the Mini K ('Kangaroo'). The Zeta plant was the sole global production site for the Mini Moke from 1966 to 1982, developing the larger-wheeled 13-inch Moke Californian for Australian outback conditions.\n\nIn 1969, following British mergers, BMC Australia became Leyland Motor Corporation of Australia. Seeking to break the Holden-Ford-Chrysler stranglehold on the large-car market, Leyland embarked on 'Project P76'. Styled by Italian master Giovanni Michelotti, the P76 was wider and roomier than the HQ Holden, offering superior handling and safety (side-impact door intrusion bars and front disc brakes standard). Under the bonnet was an enlarged 4.4-litre (269ci) all-aluminium derivative of the Rover V8, weighing less than the six-cylinder cast-iron engines of rivals. In late 1973, the P76 won Wheels Car of the Year and an endurance rally victory in the 1974 World Cup Rally across the Sahara.\n\nHowever, the P76's launch coincided with severe supplier strikes, early assembly rattles, and the October 1973 global oil embargo. In the UK, parent company British Leyland slipped into insolvency and was nationalized. In October 1974, Leyland announced the closure of the Zetland factory, with the site acquired by the Australian Commonwealth for naval stores. The sensational 2-door coupe variant, the Force 7, was scrapped with only around 10 pre-production models escaping to collectors. Leyland Australia continued for several years as an importer of Rover, Triumph, and Jaguar before dissolving.",
    "models_catalog": [
        {
            "model_slug": "morris-minor",
            "name": "Morris Minor",
            "vehicle_type": "Sedan / Tourer / Van / Ute",
            "segment": "Small",
            "years_sold_au": {"start": 1949, "end": 1962},
            "locally_built": True,
            "overview": "Alec Issigonis's brilliant small car, assembled at Zetland with high local content in sedan, convertible, commercial van, and uniquely Australian coupe utility forms.",
            "generations": [
                {
                    "series_code": "MM-1000",
                    "generation_name": "Morris Minor MM, Series II, 1000",
                    "years": {"start": 1949, "end": 1962},
                    "body_styles": ["2-door sedan", "4-door sedan", "Tourer", "Coupe utility", "Van"],
                    "summary": "Torsion bar front suspension, rack-and-pinion steering, side-valve 918cc followed by 803cc, 948cc, and 1098cc A-Series engines."
                }
            ]
        },
        {
            "model_slug": "morris-major",
            "name": "Morris Major",
            "vehicle_type": "Sedan",
            "segment": "Compact",
            "years_sold_au": {"start": 1958, "end": 1964},
            "locally_built": True,
            "overview": "Australian-unique compact car developed by BMC Australia at Zetland from the Wolseley 1500, tailored with heavy-duty suspension for Australian country roads.",
            "generations": [
                {
                    "series_code": "Series-I-Elite",
                    "generation_name": "Major Series I, Series II, Elite",
                    "years": {"start": 1958, "end": 1964},
                    "body_styles": ["4-door sedan"],
                    "summary": "BMC 1.5L and 1.6L B-Series OHV engines, high ground clearance, robust unibody construction."
                }
            ]
        },
        {
            "model_slug": "austin-lancer",
            "name": "Austin Lancer",
            "vehicle_type": "Sedan",
            "segment": "Compact",
            "years_sold_au": {"start": 1958, "end": 1962},
            "locally_built": True,
            "overview": "The Austin-badged twin of the Morris Major featuring a traditional Austin chrome crinkle grille and horseshoe motif.",
            "generations": [
                {
                    "series_code": "Series-I-II",
                    "generation_name": "Lancer Series I & Series II",
                    "years": {"start": 1958, "end": 1962},
                    "body_styles": ["4-door sedan"],
                    "summary": "1,489cc B-Series 4-cylinder engine, 4-speed manual gearbox, distinct Austin styling cues."
                }
            ]
        },
        {
            "model_slug": "austin-freeway",
            "name": "Austin Freeway",
            "vehicle_type": "Sedan / Station Wagon",
            "segment": "Medium / Large",
            "years_sold_au": {"start": 1962, "end": 1965},
            "locally_built": True,
            "overview": "BMC Australia's contender against the Holden EJ and Falcon XK, created by stretching the Cambridge body and fitting the local 2.4L 'Blue Streak' inline-six.",
            "generations": [
                {
                    "series_code": "Mk-I-II",
                    "generation_name": "Freeway Mark I & Mark II",
                    "years": {"start": 1962, "end": 1965},
                    "body_styles": ["4-door sedan", "5-door station wagon"],
                    "summary": "2,433cc Blue Streak six-cylinder engine (80 bhp), Borg-Warner 35 automatic option, heavy-duty Australian suspension."
                }
            ]
        },
        {
            "model_slug": "mini",
            "name": "Morris / BMC Mini",
            "vehicle_type": "Sedan / Van",
            "segment": "Micro / Small",
            "years_sold_au": {"start": 1961, "end": 1978},
            "locally_built": True,
            "overview": "The revolutionary front-wheel-drive transverse marvel, built at Zetland with Australian-developed innovations including wind-up windows, Mini K, and Cooper S (1966 Bathurst 1-2-3-4-5-6-7-8-9 finish).",
            "generations": [
                {
                    "series_code": "Mini-AU",
                    "generation_name": "Australian Mini (850, Cooper, Cooper S, Mini K, Clubman)",
                    "years": {"start": 1961, "end": 1978},
                    "body_styles": ["2-door sedan", "Panel van"],
                    "summary": "848cc, 998cc, 1098cc, and 1275cc Cooper S engines; Hydrolastic suspension; clean sweep of the 1966 Bathurst 500."
                }
            ]
        },
        {
            "model_slug": "moke",
            "name": "Morris / Leyland Mini Moke",
            "vehicle_type": "Open Utility / Recreational",
            "segment": "Recreational Utility",
            "years_sold_au": {"start": 1966, "end": 1982},
            "locally_built": True,
            "overview": "The cheerful open-air doorless beach utility. When UK production ended in 1968, Australia became the worldwide manufacturing home, creating the 13-inch wheel Californian.",
            "generations": [
                {
                    "series_code": "Moke-AU",
                    "generation_name": "Australian Moke & Californian",
                    "years": {"start": 1966, "end": 1982},
                    "body_styles": ["Open utility with soft top"],
                    "summary": "998cc and 1275cc A-Series engines, 13-inch road wheels for ground clearance, tubular bullbars, denim seat covers."
                }
            ]
        },
        {
            "model_slug": "morris-1100-1500-nomad",
            "name": "Morris 1100 / 1500 / Nomad",
            "vehicle_type": "Sedan / Hatchback",
            "segment": "Small / Compact",
            "years_sold_au": {"start": 1964, "end": 1972},
            "locally_built": True,
            "overview": "Advanced Pininfarina-styled front-wheel-drive family car featuring Hydrolastic interconnected fluid suspension, culminating in the Australian-exclusive 1500 OHC engine and 5-door Nomad hatchback.",
            "generations": [
                {
                    "series_code": "1100-Nomad",
                    "generation_name": "Morris 1100, 1500 & Nomad",
                    "years": {"start": 1964, "end": 1972},
                    "body_styles": ["4-door sedan", "5-door hatchback (Nomad)"],
                    "summary": "1,098cc A-Series and Australian 1,485cc E-Series OHC engine with 5-speed manual gearbox; pioneering 5-door hatchback configuration."
                }
            ]
        },
        {
            "model_slug": "austin-1800",
            "name": "Austin 1800 (Landcrab & Ute)",
            "vehicle_type": "Sedan / Utility",
            "segment": "Mid-size",
            "years_sold_au": {"start": 1965, "end": 1971},
            "locally_built": True,
            "overview": "Cavernous Alec Issigonis front-wheel-drive sedan ('Landcrab') with extraordinary torsional rigidity, winning 1965 European COTY and spawning a unique Australian coupe utility.",
            "generations": [
                {
                    "series_code": "Mk-I-II",
                    "generation_name": "Austin 1800 Mark I & II",
                    "years": {"start": 1965, "end": 1971},
                    "body_styles": ["4-door sedan", "2-door coupe utility"],
                    "summary": "1,798cc B-Series engine, Hydrolastic suspension, remarkable cabin space, Australian-designed utility version."
                }
            ]
        },
        {
            "model_slug": "austin-kimberley-tasman",
            "name": "Austin Kimberley & Tasman (X6)",
            "vehicle_type": "Sedan",
            "segment": "Mid-size / Large",
            "years_sold_au": {"start": 1970, "end": 1973},
            "locally_built": True,
            "overview": "Australian-styled evolution of the 1800 platform (Project X6) powered by an Australian-developed transverse 2.2L E-Series overhead-cam six-cylinder engine.",
            "generations": [
                {
                    "series_code": "X6",
                    "generation_name": "Kimberley & Tasman X6",
                    "years": {"start": 1970, "end": 1973},
                    "body_styles": ["4-door sedan"],
                    "summary": "2,227cc transverse 6-cylinder OHC engine (single carb Tasman, twin-carb Kimberley), front-wheel drive, Hydrolastic suspension."
                }
            ]
        },
        {
            "model_slug": "leyland-marina",
            "name": "Leyland Marina",
            "vehicle_type": "Sedan / Coupe",
            "segment": "Compact / Mid-size",
            "years_sold_au": {"start": 1972, "end": 1975},
            "locally_built": True,
            "overview": "Rear-wheel-drive compact car built at Zetland, uniquely adapted for Australia with the 2.6L OHC E-series six-cylinder ('Marina Red Six').",
            "generations": [
                {
                    "series_code": "Marina-AU",
                    "generation_name": "Leyland Marina (4-cyl & Six)",
                    "years": {"start": 1972, "end": 1975},
                    "body_styles": ["4-door sedan", "2-door coupe"],
                    "summary": "1.5L and 1.75L OHC 4-cylinders and the heavy 2,622cc 6-cylinder in the Marina Six."
                }
            ]
        },
        {
            "model_slug": "leyland-p76",
            "name": "Leyland P76",
            "vehicle_type": "Sedan",
            "segment": "Full-size",
            "years_sold_au": {"start": 1973, "end": 1975},
            "locally_built": True,
            "overview": "Australia's great tragic masterpiece. Designed by Michelotti to beat Holden and Ford, featuring an all-alloy 4.4L V8, standard front disc brakes, cavernous boot, and 1973 Wheels Car of the Year crown.",
            "generations": [
                {
                    "series_code": "P76",
                    "generation_name": "Leyland P76 Series",
                    "years": {"start": 1973, "end": 1975},
                    "body_styles": ["4-door full-size sedan"],
                    "summary": "Deluxe, Super, and Executive trims; 2.6L OHC six and 4,416cc all-aluminium V8; MacPherson strut front suspension; rack-and-pinion steering."
                }
            ]
        },
        {
            "model_slug": "leyland-force-7",
            "name": "Leyland Force 7",
            "vehicle_type": "Hatchback Coupe",
            "segment": "Sports Coupe",
            "years_sold_au": {"start": 1974, "end": 1974},
            "locally_built": True,
            "overview": "Sensational 2-door hatchback coupe variant of the P76 with full rear tailgate and 4.4L V8. Almost all were crushed when Zetland closed, making surviving cars among the rarest Australian collector vehicles.",
            "generations": [
                {
                    "series_code": "Force-7",
                    "generation_name": "Force 7 & Force 7V",
                    "years": {"start": 1974, "end": 1974},
                    "body_styles": ["2-door hatchback coupe"],
                    "summary": "Pioneering large hatchback coupe styling; 4.4L all-alloy V8 and 4-speed manual; only ~10 survived the crusher."
                }
            ]
        }
    ]
}
