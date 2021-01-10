#adapted from https://en.wikipedia.org/wiki/Outline_of_herbs_and_spices
inputList = ['ANGELICA',
'BASIL',
'HOLY BASIL',
'THAI BASIL',
'BAY LEAF',
'BOLDO',
'BOLIVIAN CORIANDER',
'BORAGE',
'CHERVIL',
'CHIVES',
'CICELY',
'CORIANDER LEAF',
'CRESS',
'CURRY LEAF',
'DILL',
'ELSHOLTZIA CILIATA',
'EPAZOTE',
'ERYNGIUM FOETIDUM',
'HEMP',
'HOJA SANTA',
'HOUTTUYNIA CORDATA',
'HYSSOP',
'JIMBU',
'LAVENDER',
'LEMON BALM',
'LEMON GRASS',
'LEMON MYRTLE',
'LEMON VERBENA',
'LIMNOPHILA AROMATICA',
'LOVAGE',
'MARJORAM',
'MINT',
'MUGWORT',
'MITSUBA',
'OREGANO',
'PARSLEY',
'PERILLA',
'ROSEMARY',
'RUE',
'SAGE',
'SAVORY',
'SANSHŌ',
'SHISO',
'SORREL',
'TARRAGON',
'THYME',
'VIETNAMESE CORIANDER',
'WOODRUFF',
'AONORI',
'AJWAIN',
'ALEPPO PEPPER',
'ALLIGATOR PEPPER',
'ALLSPICE',
'ANISE',
'AROMATIC GINGER',
'ASAFOETIDA',
'CAMPHOR',
'CARAWAY',
'CARDAMOM',
'BLACK CARDAMOM',
'CASSIA',
'CAYENNE PEPPER',
'CELERY SEED',
'CHAROLI',
'CHENPI',
'CHILI PEPPER',
'CINNAMON',
'CLOVE',
'CORIANDER SEED',
'CUBEB',
'CUMIN',
'BLACK CUMIN',
'DILL AND DILL SEED',
'FENNEL',
'FENUGREEK',
'FINGERROOT',
'GREATER GALANGAL',
'LESSER GALANGAL',
'GARLIC',
'GINGER',
'GOLPAR',
'GRAINS OF PARADISE',
'GRAINS OF SELIM',
'HORSERADISH',
'JUNIPER BERRY',
'KAEMPFERIA GALANGA',
'KOKUM',
'KORARIMA',
'BLACK LIME',
'LIQUORICE',
'LITSEA CUBEBA',
'MACE',
'MANGO-GINGER',
'MAHLAB',
'MALABATHRUM',
'BLACK MUSTARD',
'BROWN MUSTARD',
'WHITE MUSTARD',
'NIGELLA',
'PAPRIKA',
'BRAZILIAN PEPPER',
'PERUVIAN PEPPER',
'Long PEPPER',
'PEPPERCORN',
'POMEGRANATE SEED',
'POPPY SEED',
'RADHUNI',
'ROSE',
'SAFFRON',
'SALT',
'SARSAPARILLA',
'SANSHŌ',
'SASSAFRAS',
'SESAME',
'SHISO',
'SICHUAN PEPPER',
'STAR ANISE',
'SUMAC',
'TAMARIND',
'TASMANIAN PEPPER',
'TONKA BEAN',
'TURMERIC',
'UZAZI',
'VANILLA',
'VOATSIPERIFERY',
'WASABI',
'YUZU (ZEST)',
'ZEDOARY',
'ZERESHK',
'ZEST '

]
#adapted from https://www.thekitchn.com/quick-guide-to-every-herb-and-spice-in-the-cupboard-108770
inputPhraseList=['This is used as a digestive aid in Indian cooking, asafoetida has a strong odor that mellows out into a garlic-onion flavor.',
'This is a Reddish-brown paste or powder ground from annatto seeds with an earthy flavor. Used primarily in Latin American dishes like mole sauce, cochinita pibil, and tamales.',
'This is Similar to cloves, but more pungent and deeply flavored. Best used in spice mixes.',
'This Adds a woodsy background note to soups and sauces.',
'This is anise-tasting seeds which are essential for soda bread, sauerkraut, and potato salad.',
'This warm, aromatic spice is widely used in Indian cuisine. It’s also great in baked goods when used in combination with spices like clove and cinnamon.',
'This is Made from dried and ground red chili peppers. Adds a sweet heat to soups, braises, and spice mixes.',
'This is Nearly flavorless, they can be ground into smoothies, cereals, and baked goods for extra nutrition and texture, or even used as a vegan egg substitute.',
'This is Found in almost every world cuisine, it serves double duty as spice in both sweet and savory dishes.',
'This is a Sweet and warming spice. Used most often in baking, but also good with braised meat.',
'This has Earthy, lemony flavor. Used in a lot of Mexican and Indian dishes.',
'This is Smoky and earthy. Used in a lot of Southwestern U.S. and Mexican cuisine, as well as North African, Middle Eastern, and Indian.',
'This is Lightly sweet and licorice flavored. It’s excellent with meat dishes, or even chewed on its own as a breath freshener and digestion aid!',
'This herb smells like maple syrup while cooking, it has a rather bitter, burnt sugar flavor. Found in a lot of Indian and Middle Eastern dishes.',
'This is made from dehydrated garlic cloves and can be used to give dishes a sweeter, softer garlic flavor.',
'This is made from dehydrated fresh ginger and has a spicy, zesty bite.',
'This Korean red pepper spice is hot, sweet, and ever-so-slightly smoky.',
'This tastes like a cross between cardamom, citrus, and black pepper. They add a warming note to many North African dishes.',
'This is Used to flavor curries and many Thai dishes. Can be sold fresh, dry, or frozen.',
'This is ground from dried limes. Adds a sour kick to many Middle Eastern dishes.',
'This is From the same plant as nutmeg, but tastes more subtle and delicate. Great in savory dishes, especially stews and homemade sausages.',
'This is Ground from sour cherry pits, this spice has a nutty and somewhat sour flavor. It’s used in a lot of sweet breads throughout the Middle East.',
'This is Sweet and pungent. Great in baked goods, but also adds a warm note to savory dishes.',
'This is Very different from bread yeast, this can be sprinkled onto or into sauces, pastas, and other dishes to add a nutty, cheesy, savory flavor.',
'This has Robust, somewhat lemony flavor. Used in a lot of Mexican and Mediterranean dishes.',
'This Adds a sweet note and a red color. Used in stews and spice blends. There is also a spicy version labeled hot paprika.',
'This can come in a variety of colors (black, white, pink, and green being the most popular). These are pungent and pack a mild heat.',
'This is Strong and piney. Great with eggs, beans, and potatoes, as well as grilled meats.',
'This has a subtle but distinct floral flavor and aroma, and it also gives foods a bright yellow color.',
'This has Pine-like flavor, with more lemony and eucalyptus notes than rosemary. Found in a lot of northern Italian cooking.',
'This Adds sweet smokiness to dishes, as well as a red color.',
'This can be used to add a sweet licorice flavor to sauces and soups.',
'This is a Middle Eastern spice that’s great in marinades and spice rubs.',
'This is Sometimes used more for its yellow color than its flavor, it has a mild woodsy flavor. Can be used in place of saffron in a pinch or for those of us on a budget.',
'This  Adds a pungent, woodsy flavor. Great as an all-purpose seasoning.',
'This is Sweet and spicy. Can be used in both sweet baked goods and to add depth to savory dishes.',

'This is Highly aromatic with a robust licorice flavor. Excellent in pestos, as a finishing touch on pasta dishes, or stuffed into sandwiches.',
'This has Delicate anise flavor. Great raw in salads or as a finishing garnish.',
'This has Delicate onion flavor, great as a garnish.',
'This is From the coriander plant,  leaves and stems have a pungent, herbaceous flavor. Used in Caribbean, Latin American, and Asian cooking.',
'This is pungent leaves which are not related to curry powder but impart a similar flavor. Used in Indian, Malaysian, Sri Lankan, Singaporean, and Pakistani cuisine. Used to flavor curries, soups, stews, and chutneys.',
'This is a Light and feathery herb with a pungent herb flavor. Use it for pickling, with fish, and over potatoes.',
'This has Sweet lemon aroma and a fresh lemony-herbal flavor. this is excellent with poultry and in vinaigrettes.',
'This Tastes like a cross between celery and parsley. Great with seafood or to flavor stocks and soups.',
'This is Floral and woodsy. Try it in sauces, vinaigrettes, and marinades.',
'This is Surprisingly versatile for such an intensely flavored herb. Try it paired with lamb, peas, potatoes, and of course, with chocolate!',
'This has Robust, somewhat lemony flavor. Used in a lot of Mexican and Mediterranean dishes.',
'This is  Available in flat-leaf (Italian) or curly varieties, this very popular herb is light and grassy in flavor.',
'This is Small and sweet berries which are fantastic when marinated with olives or simply sprinkled on shortbread.',
'This has Peppery green flavor similar to thyme. Mostly used in roasted meat dishes and stuffing, but also goes well with beans.',
'This is A member of the mint family, this herb is used extensively in Japanese, Korean, and Southeast Asian cooking as a wrap for steaming fish and vegetables, in soups, and as a general seasoning.',
'This has Strong anise flavor. Can be eaten raw in salads or used to flavor tomato dishes, chicken, seafood, or eggs.',
'This is A spicy, edgier cousin to sweet Italian basil. A must-have for Thai stir-fries, Vietnamese pho, spring rolls, and other South Asian dishes.',
'This  Adds a pungent, woodsy flavor. Great as an all-purpose seasoning.'

]
