from bs4 import BeautifulSoup

# Código HTML de entrada (reemplaza esto con tu código HTML)
html_input = '''
<table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/61efa74c998e05a9f5248c534a6c6fe5697654195.png" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Mosin%20Nagant.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_MosinnagantSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Mosing Nagant</div>
                        </div>
                    </a>
                    <a href="./characters/Peritya.html">
                        <div class=" text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_PerityaSSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Peritya</div>
                        </div>
                    </a>
                    <a href="./characters/Tololo.html">
                        <div class="me-3 text-center">
                            <img class="character-bgS" src="public/img/Avatar_Bust_TololoSSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Tololo</div>
                        </div>
                    </a>
                    <a href="./characters/Sabrina.html">
                        <div class="me-3 text-center">
                            <img class="character-bgS" src="public/img/Avatar_Bust_SabrinaSSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Sabrina</div>
                        </div>
                    </a>
                    <a href="./characters/Qiongjiu.html">
                        <div class="me-3 text-center">
                            <img class="character-bgS" src="public/img/Avatar_Bust_QiongjiuSSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Qiongjiu</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>Game Release</td>
        </tr>
    </table>

    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/3fbcad72eb6eea0b39bca3ab67f3b502697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Daiyan.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_DaiyanSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Daiyan</div>
                        </div>
                    </a>
                    <a href="./characters/Nagant.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_NagantSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Nagant</div>
                        </div>
                    </a>
                    <a href="./characters/Colphne.html">
                        <div class="character-bg text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_ColphneSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Colphne</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>25/12/2023 - 22/01/2024</td>
        </tr>
    </table>

    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/a32eef1c3205c73bfe63c0fc00ab189d697654195.png" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Sabrina.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_SabrinaSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Sabrina</div>
                        </div>
                    </a>
                    <a href="./characters/Cheeta.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_CheetaSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Cheeta</div>
                        </div>
                    </a>
                    <a href="./characters/Nemesis.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_NemesisSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Nemesis</div>
                        </div>
                    </a>

                </div>
            </td>
            <td>16/01/2023 - 30/01/2023</td>
        </tr>
    </table>

    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/40f53dab6d23764338ee5b9bf3da86f3697654195.png" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Centaureissi.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_CentaureissiSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Centaureissi</div>
                        </div>
                    </a>
                    <a href="./characters/Sharkry.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_SharkrySR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Sharkry</div>
                        </div>
                    </a>
                    <a href="./characters/Krolik.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_CharolicSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Krolik</div>
                        </div>
                    </a>

                </div>
            </td>
            <td>16/01/2023 - 30/01/2023</td>
        </tr>
    </table>

    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/224078482e8e0c994076e21643666ff3697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Qiongjiu.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_QiongjiuSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Qiongjiu</div>
                        </div>
                    </a>
                    <a href="./characters/Cheeta.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_CheetaSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Cheeta</div>
                        </div>
                    </a>
                    <a href="./characters/Nagant.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_NagantSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Nagant</div>
                        </div>
                    </a>

                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/bb98231ffc82d4e1fad059446472f1b0697654195.png" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Lenna.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_LennaSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Lenna</div>
                        </div>
                    </a>
                    <a href="./characters/Littara.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_LittaraSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Littara</div>
                        </div>
                    </a>
                    <a href="./characters/Ksenia.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_KseniaSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Ksenia</div>
                        </div>
                    </a>

                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/5a539d85ed05257665b72a8719260396697654195.png" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Jiangyu.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_JiangyuSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Jiangyu</div>
                        </div>
                    </a>
                    <a href="./characters/Cheeta.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_CheetaSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Cheeta</div>
                        </div>
                    </a>
                    <a href="./characters/Nemesis.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_NemesisSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Nemesis</div>
                        </div>
                    </a>

                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/788bdfd6c194f01983d77297408a258a697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Peritya.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_PerityaSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Peritya</div>
                        </div>
                    </a>
                    <a href="./characters/Littara.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_LittaraSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Littara</div>
                        </div>
                    </a>
                    <a href="./characters/Ksenia.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_KseniaSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Ksenia</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/262b263bad4affeac79bddc3d148e530697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Daiyan.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_DaiyanSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Daiyan</div>
                        </div>
                    </a>
                    <a href="./characters/Groza.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_GrozaSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Groza</div>
                        </div>
                    </a>
                    <a href="./characters/Colphne.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_ColphneSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Colphne</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/763a2d998017a8abb929765f98daa925697654195.png" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Macchiato.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_MacqiatoSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Macqiato</div>
                        </div>
                    </a>
                    <a href="./characters/Krolik.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_CharolicSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Krolik</div>
                        </div>
                    </a>
                    <a href="./characters/Colphne.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_ColphneSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Colphne</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/2a57bbc7bf1371d2d8bc235ea4aae503697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Centaureissi.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_CentaureissiSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Centaureissi</div>
                        </div>
                    </a>
                    <a href="./characters/Sharkry.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_SharkrySR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Sharkry</div>
                        </div>
                    </a>
                    <a href="./characters/Nagant.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_NagantSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Nagant</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/eb1ad21d687b70c6e289b5ae1378a82b697654195.png" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Ullrid.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_UllridSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Ullrid</div>
                        </div>
                    </a>
                    <a href="./characters/Cheeta.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_CheetaSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Cheeta</div>
                        </div>
                    </a>
                    <a href="./characters/Nemesis.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_NemesisSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Nemesis</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/98e4976f781285c9054ce913cf801666697654195.png" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Lenna.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_LennaSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Lenna</div>
                        </div>
                    </a>
                    <a href="./characters/Littara.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_LittaraSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Littara</div>
                        </div>
                    </a>
                    <a href="./characters/Ksenia.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_KseniaSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Ksenia</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/0714dd0bc84b5068926b2e8edd99160b697654195.png" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Daiyan.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_DaiyanSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Daiyan</div>
                        </div>
                    </a>
                    <a href="./characters/Centaureissi.html">
                        <div class=" text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_CentaureissiSSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Centaureissi</div>
                        </div>
                    </a>
                    <a href="./characters/Lenna.html">
                        <div class="me-3 text-center">
                            <img class="character-bgS" src="public/img/Avatar_Bust_LennaSSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Lenna</div>
                        </div>
                    </a>
                    <a href="./characters/Jiangyu.html">
                        <div class="me-3 text-center">
                            <img class="character-bgS" src="public/img/Avatar_Bust_JiangyuSSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Jiangyu</div>
                        </div>
                    </a>
                    <a href="./characters/Sharkry.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_SharkrySR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Sharkry</div>
                        </div>
                    </a>
                    <a href="./characters/Littara.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_LittaraSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Littara</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>20/06/2024 - 04/07/2024</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/53cce6e667d9392ca99fb5dd36e67c22697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Suomi.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_SuomiSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Suomi</div>
                        </div>
                    </a>
                    <a href="./characters/Groza.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_GrozaSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Groza</div>
                        </div>
                    </a>
                    <a href="./characters/Colphne.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_ColphneSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Colphne</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/d4d071f159390d401e01797c489de3bb697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Jiangyu.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_JiangyuSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Jiangyu</div>
                        </div>
                    </a>
                    <a href="./characters/Sharkry.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_SharkrySR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Sharkry</div>
                        </div>
                    </a>
                    <a href="./characters/Nagant.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_NagantSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Nagant</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/8ae1a019b7d3eab4b64bfcff57b39b34697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Dushevnaya.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_DusevnyjSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Dushevnaya</div>
                        </div>
                    </a>
                    <a href="./characters/Krolik.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_CharolicSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Krolik</div>
                        </div>
                    </a>
                    <a href="./characters/Nemesis.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_NemesisSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Nemesis</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/76790546783923f9ab12a82cc0d254c9697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Macchiato.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_MacqiatoSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Macchiato</div>
                        </div>
                    </a>
                    <a href="./characters/Littara.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_LittaraSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Littara</div>
                        </div>
                    </a>
                    <a href="./characters/Ksenia.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_KseniaSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Ksenia</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/fe24ba09ebfba5156110c6e4fcee409e697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Zhaohui.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_ZhaohuiSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Zhaohui</div>
                        </div>
                    </a>
                    <a href="./characters/Groza.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_GrozaSR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Groza</div>
                        </div>
                    </a>
                    <a href="./characters/Colphne.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_ColphneSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Colphne</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/af98e44b03800e6ad120839996c18a21697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Papasha.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_PapashaSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Papasha</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>06/08/2024 - 09/10/2024</td>
        </tr>
    </table>
    <table class="desktop-table">
        <tr>
            <td rowspan="2">
                <img src="public/img/banners/88e2c8ba7f6d47e5fbbba1665800dd0c697654195.jpg" alt="Imagen" style="width:100%;height:auto;">
            </td>
            <td><strong>Rated characters</strong></td>
            <td><strong>Date</strong></td>
        </tr>
        <tr>
            <td>
                <div class="d-flex justify-content-center">
                    <a href="./characters/Ullrid.html">
                        <div class="character-bg text-center me-3">
                            <img class="character-bgS" src="public/img/Avatar_Bust_UllridSSR.png" alt="Character 1" style="width:100px;height:auto;">
                            <div class="text-bg">Ullrid</div>
                        </div>
                    </a>
                    <a href="./characters/Sharkry.html">
                        <div class=" text-center me-3">
                            <img class="character-bgA" src="public/img/Avatar_Bust_SharkrySR.png" alt="Character 2" style="width:100px;height:auto;">
                            <div class="text-bg">Sharkry</div>
                        </div>
                    </a>
                    <a href="./characters/Nagant.html">
                        <div class="me-3 text-center">
                            <img class="character-bgA" src="public/img/Avatar_Bust_NagantSR.png" alt="Character 3" style="width:100px;height:auto;">
                            <div class="text-bg">Nagant</div>
                        </div>
                    </a>
                </div>
            </td>
            <td>08/02/2023 - 23/02/2023</td>
        </tr>
    </table>
'''

# Nombre del archivo de salida
output_filename = 'tablas_transformadas.html'

# Parseamos el HTML de entrada
soup = BeautifulSoup(html_input, 'html.parser')

# Encontramos todas las tablas con clase "desktop-table"
desktop_tables = soup.find_all('table', class_='desktop-table')

# Variable para almacenar las tablas transformadas
mobile_tables_html = ''

for table in desktop_tables:
    # Creamos una nueva tabla con clase "mobile-table"
    mobile_table = BeautifulSoup('<table class="mobile-table"></table>', 'html.parser')
    new_table = mobile_table.table

    # Extraemos la imagen principal
    img_tag = table.find('img')
    img_html = f'''
    <tr>
        <td>
            {str(img_tag)}
        </td>
    </tr>
    '''
    new_table.append(BeautifulSoup(img_html, 'html.parser'))

    # Extraemos la fecha (buscamos el último <td> que contiene la fecha)
    date_td = table.find_all('td')[-1]
    date_text = date_td.get_text(strip=True)
    date_html = f'''
    <tr>
        <td>
            <strong>Date</strong><br>
            {date_text}
        </td>
    </tr>
    '''
    new_table.append(BeautifulSoup(date_html, 'html.parser'))

    # Buscamos el div que contiene los personajes
    characters_div = table.find('div', class_='d-flex')
    if characters_div is None:
        print("No se encontró el div con clase 'd-flex' en la tabla. Saltando esta tabla.")
        continue

    character_links = characters_div.find_all('a')

    characters_html = '''
    <tr>
        <td>
            <strong>Rated characters</strong><br>
            <div class="character-container">
    '''

    for a in character_links:
        character_div = a.find('div')
        img_tag = character_div.find('img')
        character_name = character_div.find('div', class_='text-bg').get_text(strip=True)
        href = a['href']

        # Determinamos la clase del personaje
        img_classes = img_tag.get('class', [])
        if 'character-bgS' in img_classes:
            character_class = 'character-bgS'
        elif 'character-bgA' in img_classes:
            character_class = 'character-bgA'
        else:
            character_class = ''

        character_html = f'''
        <a href="{href}">
            <div class="character-item {character_class}">
                {str(img_tag)}
            </div>
            <div class="text-bg">{character_name}</div>
        </a>
        '''
        characters_html += character_html

    characters_html += '''
            </div>
        </td>
    </tr>
    '''
    new_table.append(BeautifulSoup(characters_html, 'html.parser'))

    # Añadimos la tabla transformada al resultado final
    mobile_tables_html += str(new_table) + '\n\n'

# Guardamos el HTML de las tablas transformadas en un archivo
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(mobile_tables_html)

print(f"Las tablas transformadas se han guardado en '{output_filename}'.")