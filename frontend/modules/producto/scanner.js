import { BrowserMultiFormatReader } from "@zxing/browser";

export class Scanner {

    constructor() {

        this.reader =
            new BrowserMultiFormatReader();

        this.video = null;
    }

    async escanear() {

        this.video =
            document.createElement("video");

        this.video.setAttribute(
            "playsinline",
            true,
        );

        this.video.style.width = "100%";
        this.video.style.maxWidth = "500px";
        this.video.style.display = "block";
        this.video.style.margin = "20px auto";

        document.body.appendChild(
            this.video,
        );

        try {

            const resultado =
                await this.reader.decodeOnceFromVideoDevice(
                    undefined,
                    this.video,
                );

            return resultado.text;

        }

        finally {

            this.detener();

        }

    }

    detener() {

        if (!this.video) {
            return;
        }

        const stream =
            this.video.srcObject;

        if (stream) {

            stream
                .getTracks()
                .forEach(
                    track => track.stop(),
                );

        }

        this.video.remove();

        this.video = null;

    }

}