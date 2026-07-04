from __future__ import annotations

from typing import List

import pymysql

from app.database.connection import get_connection
from app.models.attraction import Attraction


class AttractionRepository:
    def find_all(self) -> List[Attraction]:
        try:
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                """
                SELECT
                    id,
                    name,
                    description,
                    location,
                    latitude,
                    longitude,
                    category,
                    image_url
                FROM attractions
                ORDER BY id
                """
            )

            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            return [Attraction(**row) for row in rows]
        except Exception:
            return self._fallback_attractions()

    def _fallback_attractions(self) -> List[Attraction]:
        return [
            Attraction(
                id=1,
                name="Machu Picchu",
                description="Ciudadela inca ubicada en lo alto de los Andes, rodeada de montañas y considerada una maravilla del mundo moderno.",
                location="Cusco",
                latitude=-13.1631,
                longitude=-72.5450,
                category="arqueológico",
                image_url="https://example.com/machupicchu.jpg",
            ),
            Attraction(
                id=2,
                name="Huacachina",
                description="Oasis natural en medio del desierto de Ica, famoso por sandboarding y paseos en buggies.",
                location="Ica",
                latitude=-14.0875,
                longitude=-75.7630,
                category="naturaleza",
                image_url="https://example.com/huacachina.jpg",
            ),
            Attraction(
                id=3,
                name="Paracas Reserva Nacional",
                description="Área natural protegida con biodiversidad marina, playas y formaciones rocosas impresionantes.",
                location="Ica",
                latitude=-13.8667,
                longitude=-76.2667,
                category="naturaleza",
                image_url="https://example.com/paracas.jpg",
            ),
            Attraction(
                id=4,
                name="Chan Chan",
                description="La ciudad de adobe más grande de América precolombina, capital del reino Chimú.",
                location="Trujillo",
                latitude=-8.1116,
                longitude=-79.0505,
                category="arqueológico",
                image_url="https://example.com/chanchan.jpg",
            ),
            Attraction(
                id=5,
                name="Playa Huanchaco",
                description="Famosa por sus caballitos de totora y por ser un lugar ideal para surf.",
                location="Huanchaco",
                latitude=-8.0833,
                longitude=-79.1222,
                category="playa",
                image_url="https://example.com/huanchaco.jpg",
            ),
            Attraction(
                id=6,
                name="Kuelap",
                description="Ciudadela fortificada de los Chachapoyas con impresionantes murallas y vistas panorámicas.",
                location="Amazonas",
                latitude=-6.4275,
                longitude=-77.9247,
                category="arqueológico",
                image_url="https://example.com/kuelap.jpg",
            ),
            Attraction(
                id=7,
                name="Gocta Catarata",
                description="Una de las cataratas más altas del mundo, rodeada de bosque nuboso y vida silvestre.",
                location="Amazonas",
                latitude=-6.0261,
                longitude=-77.8886,
                category="naturaleza",
                image_url="https://example.com/gocta.jpg",
            ),
            Attraction(
                id=8,
                name="Colca Canyon",
                description="Uno de los cañones más profundos del mundo, hogar del cóndor andino.",
                location="Arequipa",
                latitude=-15.6220,
                longitude=-71.9756,
                category="naturaleza",
                image_url="https://example.com/colca.jpg",
            ),
            Attraction(
                id=9,
                name="Laguna Humantay",
                description="Laguna turquesa ubicada al pie del nevado Humantay, rodeada de montañas sagradas.",
                location="Cusco",
                latitude=-13.3790,
                longitude=-72.6180,
                category="naturaleza",
                image_url="https://example.com/humantay.jpg",
            ),
            Attraction(
                id=10,
                name="Uros Islands",
                description="Islas flotantes construidas con totora en el lago Titicaca.",
                location="Puno",
                latitude=-15.8167,
                longitude=-69.9667,
                category="cultural",
                image_url="https://example.com/uros.jpg",
            ),
        ]