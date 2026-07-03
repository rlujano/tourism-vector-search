USE tourism;

INSERT INTO attractions (name, description, location, latitude, longitude, category, image_url) VALUES

('Chan Chan',
'Chan Chan es la ciudad de adobe más grande de América precolombina. Fue la capital del reino Chimú y destaca por sus enormes muros decorados con relieves geométricos que representan peces, aves y redes de pesca. Su planificación urbana refleja un avanzado conocimiento de organización social y manejo del territorio.',
'Trujillo, La Libertad', -8.1116, -79.0505, 'arqueológico', 'https://example.com/chanchan.jpg'),

('Huaca del Sol y la Luna',
'Este complejo ceremonial mochica destaca por sus impresionantes murales policromados que narran rituales religiosos, sacrificios y deidades. La Huaca de la Luna aún conserva colores originales gracias a su enterramiento por siglos.',
'Trujillo, La Libertad', -8.1169, -79.0299, 'arqueológico', 'https://example.com/huaca_sol_luna.jpg'),

('Playa Huanchaco',
'Famosa por sus caballitos de totora, embarcaciones tradicionales usadas desde tiempos mochicas. Es un lugar ideal para surf y para observar la cultura viva de los pescadores locales.',
'Huanchaco, La Libertad', -8.0833, -79.1222, 'playa', 'https://example.com/huanchaco.jpg'),

('Cumbemayo',
'Complejo arqueológico con canales de agua tallados en roca volcánica con más de 3000 años de antigüedad. Su ingeniería hidráulica sigue siendo un misterio fascinante.',
'Cajamarca', -7.1631, -78.5126, 'arqueológico', 'https://example.com/cumbemayo.jpg'),

('Baños del Inca',
'Complejo termal utilizado desde tiempos del Inca Atahualpa. Sus aguas geotermales poseen propiedades medicinales y fueron centro de descanso del imperio inca.',
'Cajamarca', -7.1556, -78.5106, 'termal', 'https://example.com/banosinca.jpg'),

('Kuelap',
'Ciudadela fortificada de la cultura Chachapoyas, ubicada en la cima de una montaña. Sus murallas de hasta 20 metros de altura muestran una ingeniería defensiva impresionante.',
'Amazonas', -6.4275, -77.9247, 'arqueológico', 'https://example.com/kuelap.jpg'),

('Gocta Catarata',
'Una de las cataratas más altas del mundo con más de 770 metros. Rodeada de bosque nuboso, es hogar de aves exóticas como el gallito de las rocas.',
'Amazonas', -6.0261, -77.8886, 'naturaleza', 'https://example.com/gocta.jpg'),

('Sarcófagos de Karajía',
'Estatuas funerarias chachapoyas ubicadas en acantilados inaccesibles. Representan entierros ceremoniales de élite.',
'Luya, Amazonas', -6.3544, -77.9431, 'arqueológico', 'https://example.com/karajia.jpg'),

('Museo Tumbas Reales de Sipán',
'Contiene los tesoros del Señor de Sipán, uno de los hallazgos arqueológicos más importantes de América.',
'Lambayeque', -6.7629, -79.9355, 'museo', 'https://example.com/sipan.jpg'),

('Bosque de Pómac',
'Área protegida que conserva pirámides de la cultura Sicán rodeadas de un bosque seco único en el mundo.',
'Lambayeque', -6.4845, -79.7717, 'naturaleza', 'https://example.com/pomac.jpg'),

('Caral',
'La civilización más antigua de América con más de 5000 años. Sus pirámides muestran el origen de la organización social compleja en el continente.',
'Supe, Lima', -10.8911, -77.5200, 'arqueológico', 'https://example.com/caral.jpg'),

('Lunahuaná',
'Distrito turístico conocido por el canotaje en el río Cañete, bodegas de vino y deportes de aventura.',
'Lima', -12.9723, -76.1234, 'aventura', 'https://example.com/lunahuana.jpg'),

('Huacachina',
'Oasis natural en medio del desierto de Ica, famoso por sandboarding y paseos en buggies sobre dunas gigantes.',
'Ica', -14.0875, -75.7630, 'naturaleza', 'https://example.com/huacachina.jpg'),

('Nazca Lines',
'Geoglifos gigantes dibujados en el desierto cuyo propósito aún es objeto de debate científico.',
'Ica', -14.7390, -75.1300, 'arqueológico', 'https://example.com/nazca.jpg'),

('Paracas Reserva Nacional',
'Área natural protegida con biodiversidad marina, playas y formaciones rocosas impresionantes como La Catedral.',
'Ica', -13.8667, -76.2667, 'naturaleza', 'https://example.com/paracas.jpg'),

('Islas Ballestas',
'Conocidas como “las Galápagos del Perú” por su fauna marina: lobos marinos, pingüinos de Humboldt y aves guaneras.',
'Paracas', -13.7350, -76.3950, 'naturaleza', 'https://example.com/ballestas.jpg'),

('Huaytapallana',
'Nevado sagrado con lagunas de colores turquesa y rutas de trekking de alta montaña.',
'Junín', -11.9180, -75.1060, 'naturaleza', 'https://example.com/huaytapallana.jpg'),

('Cordillera Blanca',
'Cadena montañosa tropical con picos nevados como el Huascarán, ideal para alpinismo.',
'Áncash', -9.1333, -77.6000, 'montaña', 'https://example.com/cordillera_blanca.jpg'),

('Chavín de Huántar',
'Centro ceremonial preincaico con galerías subterráneas y el famoso Lanzón Monolítico.',
'Áncash', -9.5833, -77.1772, 'arqueológico', 'https://example.com/chavin.jpg'),

('Laguna 69',
'Laguna de color turquesa intensa rodeada de montañas nevadas en la Cordillera Blanca.',
'Áncash', -9.0000, -77.6000, 'naturaleza', 'https://example.com/laguna69.jpg'),

('Machu Picchu',
'Ciudadela inca ubicada en lo alto de los Andes. Es una obra maestra de ingeniería y arquitectura, rodeada de montañas y considerada una de las siete maravillas del mundo moderno.',
'Cusco', -13.1631, -72.5450, 'arqueológico', 'https://example.com/machupicchu.jpg'),

('Valle Sagrado',
'Región fértil con sitios arqueológicos como Pisac, Ollantaytambo y terrazas agrícolas incas.',
'Cusco', -13.3415, -72.1940, 'cultural', 'https://example.com/valle_sagrado.jpg'),

('Sacsayhuamán',
'Fortaleza inca con enormes bloques de piedra perfectamente ensamblados sin mortero.',
'Cusco', -13.5083, -71.9781, 'arqueológico', 'https://example.com/sacsayhuaman.jpg'),

('Montaña de 7 Colores',
'Formación geológica con estratos minerales que generan colores naturales en la montaña.',
'Cusco', -13.8760, -71.3010, 'naturaleza', 'https://example.com/vinicunca.jpg'),

('Laguna Humantay',
'Laguna turquesa ubicada al pie del nevado Humantay, rodeada de montañas sagradas.',
'Cusco', -13.3790, -72.6180, 'naturaleza', 'https://example.com/humantay.jpg'),

('Colca Canyon',
'Uno de los cañones más profundos del mundo, hogar del cóndor andino.',
'Arequipa', -15.6220, -71.9756, 'naturaleza', 'https://example.com/colca.jpg'),

('Monasterio Santa Catalina',
'Ciudad dentro de la ciudad en Arequipa, con calles, plazas y claustros coloniales.',
'Arequipa', -16.3989, -71.5369, 'cultural', 'https://example.com/santacatalina.jpg'),

('Volcán Misti',
'Volcán icónico de Arequipa que domina el paisaje de la ciudad blanca.',
'Arequipa', -16.2900, -71.4070, 'montaña', 'https://example.com/misti.jpg'),

('Uros Islands',
'Islas flotantes construidas con totora en el lago Titicaca.',
'Puno', -15.8167, -69.9667, 'cultural', 'https://example.com/uros.jpg'),

('Taquile Island',
'Isla del lago Titicaca conocida por sus textiles y tradiciones ancestrales.',
'Puno', -15.7667, -69.6833, 'cultural', 'https://example.com/taquile.jpg'),
('Tambopata Reserve',
'Reserva natural con gran biodiversidad, hogar de guacamayos, jaguares y ríos amazónicos.',
'Madre de Dios', -12.7333, -69.1833, 'naturaleza', 'https://example.com/tambopata.jpg'),

('Manu National Park',
'Uno de los parques con mayor biodiversidad del planeta, declarado Patrimonio de la Humanidad.',
'Madre de Dios', -12.2500, -71.2500, 'naturaleza', 'https://example.com/manu.jpg'),

('Iquitos Amazon River',
'Puerta de entrada a la selva amazónica peruana y el río más caudaloso del mundo.',
'Loreto', -3.7437, -73.2516, 'naturaleza', 'https://example.com/iquitos.jpg'),

('Pacaya Samiria',
'Reserva nacional conocida como la selva de los espejos por sus ríos reflejantes.',
'Loreto', -5.3167, -75.1833, 'naturaleza', 'https://example.com/pacaya.jpg'),

('Laguna Azul Tarapoto',
'Laguna tropical rodeada de vegetación exuberante en la selva alta.',
'San Martín', -6.4833, -76.3667, 'naturaleza', 'https://example.com/laguna_azul.jpg');