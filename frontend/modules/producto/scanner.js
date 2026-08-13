import { BrowserMultiFormatReader } from "@zxing/browser";

export class Scanner {

    constructor() {

        this.reader = new BrowserMultiFormatReader();

    }

    async escanear() {

        const video = document.createElement(
            "video",
        );

        video.setAttribute(
            "playsinline",
            true,
        );

        document.body.appendChild(
            video,
        );

        const resultado =
            await this.reader.decodeOnceFromVideoDevice(
                undefined,
                video,
            );

        video.remove();

        return resultado.text;

    }

}