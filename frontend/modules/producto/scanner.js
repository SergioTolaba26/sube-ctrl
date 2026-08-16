import { BrowserMultiFormatReader } from "@zxing/browser";

export class Scanner {

    constructor() {

        this.reader =
            new BrowserMultiFormatReader();

        this.video = null;
        this.controlador = null;

    }


    async escanear(
        callback,
    ) {

        this.video =
            document.createElement(
                "video",
            );

        this.video.setAttribute(
            "playsinline",
            true,
        );

        this.video.setAttribute(
            "autoplay",
            true,
        );

        this.video.style.width =
            "100%";

        this.video.style.maxWidth =
            "500px";

        this.video.style.display =
            "block";

        this.video.style.margin =
            "20px auto";

        document.body.appendChild(
            this.video,
        );


        try {

            this.controlador =
                await this.reader
                    .decodeFromVideoDevice(

                        undefined,

                        this.video,

                        (
                            resultado,
                            error,
                        ) => {

                            if (!resultado) {
                                return;
                            }


                            const codigo =
                                resultado.text;


                            console.log(
                                "SCANNER LEYÓ:",
                                codigo,
                            );


                            this.detener();


                            if (
                                callback
                            ) {

                                callback(
                                    codigo,
                                );

                            }

                        },

                    );

        }
        catch (
            error
        ) {

            console.error(
                "SCANNER ERROR:",
                error,
            );

            this.detener();

            throw error;

        }

    }


    detener() {

        if (
            this.controlador
        ) {

            this.controlador.stop();

            this.controlador =
                null;

        }


        if (
            this.video
        ) {

            const stream =
                this.video.srcObject;


            if (
                stream
            ) {

                stream
                    .getTracks()
                    .forEach(
                        (
                            track,
                        ) => {

                            track.stop();

                        },
                    );

            }


            this.video.remove();

            this.video =
                null;

        }


        this.reader.reset();

    }

}