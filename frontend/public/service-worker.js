const CACHE_NAME = "cloud-conta-v1";

const ARCHIVOS_INICIALES = [
    "/",
    "/index.html",
];

self.addEventListener(
    "install",
    event => {

        event.waitUntil(

            caches
                .open(CACHE_NAME)
                .then(
                    cache =>
                        cache.addAll(
                            ARCHIVOS_INICIALES,
                        ),
                ),

        );

        self.skipWaiting();

    },
);


self.addEventListener(
    "activate",
    event => {

        event.waitUntil(

            caches
                .keys()
                .then(
                    nombres =>

                        Promise.all(

                            nombres
                                .filter(
                                    nombre =>
                                        nombre !==
                                        CACHE_NAME,
                                )
                                .map(
                                    nombre =>
                                        caches.delete(
                                            nombre,
                                        ),
                                ),

                        ),
                ),

        );

        self.clients.claim();

    },
);


self.addEventListener(
    "fetch",
    event => {

        const request =
            event.request;

        // Sólo interceptamos GET.
        if (
            request.method !==
            "GET"
        ) {
            return;
        }

        const url =
            new URL(
                request.url,
            );

        // El backend de Render
        // NO se cachea.
        if (
            url.hostname ===
            "cloud-conta-backend.onrender.com"
        ) {
            return;
        }

        // Tampoco intentamos
        // cachear APIs externas.
        if (
            url.origin !==
            self.location.origin
        ) {
            return;
        }

        event.respondWith(

            caches.match(
                request,
            )
            .then(
                respuestaCache => {

                    if (
                        respuestaCache
                    ) {

                        return respuestaCache;

                    }

                    return fetch(
                        request,
                    )
                    .then(
                        respuesta => {

                            if (
                                !respuesta ||
                                respuesta.status !==
                                    200 ||
                                respuesta.type ===
                                    "opaque"
                            ) {

                                return respuesta;

                            }

                            const copia =
                                respuesta.clone();

                            caches
                                .open(
                                    CACHE_NAME,
                                )
                                .then(
                                    cache =>
                                        cache.put(
                                            request,
                                            copia,
                                        ),
                                );

                            return respuesta;

                        },
                    );

                },
            ),

        );

    },
);