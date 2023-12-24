# 🫛 坂本アヒル「[ずんだもん立ち絵素材](https://seiga.nicovideo.jp/seiga/im10788496)」のヴェクター化 🫛

## 🔨 作業工程

### 🌐 ダウンロード

まず、[ここ](https://ux.getuploader.com/s_ahiru/download/59)から
`ずんだもん立ち絵素材V3.2.zip`をダウンロードしてZIPを展開したのだ。
パスワードは`zunda`なのだ。unzipじゃ文字化けするからp7zip使えなのだ。
あと、Torからはアクセスできないのだ。

`7z x ./ずんだもん立ち絵素材2.3.zip`

### 🔀 変換

[inkscape編集向けの改造版のpsd2svg](https://github.com/eownerdead/psd2svg/)で
PSDからSVGに変換したのだ。

`psd2svg --resource-path ./assets/ ./ずんだもん立ち絵素材2.3.psd`

### 〰 ヴェクター化

`./assets/*.png`をInkscapeで手作業でトレースするのだ。

最初は、[VTracer](https://github.com/visioncortex/vtracer)でトレースして、
修正していたけど、結局、速そうなのは手作業なのだ。思ったより時間もかかるし、面倒くさいのだ。

## ⏳ 進捗

* 🫛 尻尾的なアレ (tail)
* ❌ パーカー裏地 (hoodie-lining)
* 服装2 (clothes2)
  * ❌ 素体 (clothes2-naked)
  * ❌ ぱんつ (clothes2-underpants)
  * ❌ スク水 (clothes2-swimwear)
  * ❌ バスタオル (clothes2-bath-towel)
* 右腕 (clothes2-rarm)
  * ❌ 胸元 (clothes2-rarm-on-chest)
  * ❌ マイク (clothes2-rarm-with-microphone)
  * ❌ 指差し (clothes2-rarm-pointing)
  * ❌ 苦しむ (clothes2-rarm-distressed)
  * ❌ 口元 (clothes2-rarm-near-mouse)
  * ❌ 手を挙げる (clothes2-rarm-raised)
  * ❌ 腰 (clothes2-rarm-on-hips)
  * ❌ 基本 (clothes2-rarm-normal)
* 左腕 (clothes2-larm)
  * ❌ ひそひそ (clothes2-larm-whispering)
  * ❌ 胸元 (clothes2-larm-on-chest)
  * ❌ 考える (clothes2-larm-thinking)
  * ❌ 苦しむ (clothes2-larm-distressed)
  * ❌ 口元 (clothes2-larm-near-mouse)
  * ❌ 手を挙げる (clothes2-larm-raised)
  * ❌ 腰 (clothes2-larm-on-hips)
  * ❌ 基本 (clothes2-larm-normal)
* 服装1 (clothes1)
  * ❌ 制服 (clothes1-uniform)
  * 🫛 いつもの服 (clothes1-normal)
* 左腕 (clothes1-larm)
  * ❌ ひそひそ (clothes1-larm-whispering)
  * ❌ 考える (clothes1-larm-thinking)
  * ❌ 苦しむ (clothes1-larm-distressed)
  * ❌ 口元 (clothes1-larm-near-mouse)
  * ❌ 手を挙げる (clothes1-larm-raised)
  * ❌ 腰 (clothes1-larm-on-hips)
  * 🫛 基本 (clothes1-larm-normal)
* 右腕 (clothes1-rarm)
  * ❌ マイク (clothes1-rarm-microphone)
  * ❌ 指差し (clothes1-rarm-pointing)
  * ❌ 苦しむ (clothes1-rarm-distressed)
  * ❌ 口元 (clothes1-rarm-near-mouse)
  * ❌ 手を挙げる (clothes1-rarm-raised)
  * ❌ 腰 (clothes1-rarm-on-hips)
  * 🫛 基本 (clothes1-rarm-normal)
* 口 (mouse)
  * 🫛 ほあー (hoaa)
  * ❌ ほあ (hoa)
  * ❌ ほー (ho)
  * ❌ むふ (mufu)
  * ❌ △ (delta)
  * ❌ んあー (na)
  * ❌ んへー (nhe)
  * ❌ んー (n)
  * ❌ はへえ (hahe)
  * ❌ おほお (oho)
  * ❌ お (o)
  * ❌ ゆ (yu)
  * ❌ むー (mu)
* 顔色 (g506)
  * ❌ かげり (complexion-dark)
  * ❌ (非表示) (complexion-none)
  * ❌ 青ざめ (complexion-pallid)
  * ❌ ほっぺ赤め (cheek-blushing)
  * ❌ ほっぺ2 (cheek2)
  * 🫛 ほっぺ (cheek)
* 目 (eyes)
  * ❌ ぐるぐる (eyes-spiral)
  * ❌ 〇〇 (eyes-white)
  * ❌ >< (eyes-crossed)
  * ❌ UU (eyes-pensive)
  * ❌ にっこり2 (eyes-smiled2)
  * ❌ にっこり (eyes-smiled)
  * ❌ なごみ目 (eyes-clamed)
  * ❌ ジト目 (eyes-scornful)
  * ❌ 細め目 (eyes-squinting)
  * ❌ 細め目ハート (eyes-squinting-heart)
  * ❌ 上向き3 (eyes-looking-up3)
  * ❌ 上向き2 (eyes-looking-up2)
  * ❌ 上向き (eyes-looking-up)
* 目セット (eyes-set)
  * ❌ 見開き白目 (eyes-set-white-open)
  * ❌ ジト白目 (eyes-set-white-scornful)
  * 🫛 普通白目 (eyes-set-white-normal)
* 黒目 (iris)
  * ❌ 目逸らし3 (iris-away3)
  * ❌ 目逸らし2 (iris-away2)
  * ❌ 目逸らし (iris-away)
  * ❌ カメラ目線3 (iris-at-view3)
  * ❌ カメラ目線2 (iris-at-view2)
  * ❌ カメラ目線 (iris-at-view)
  * ❌ 普通目3 (iris-normal3)
  * ❌ 普通目2 (iris-normal2)
  * 🫛 普通目 (iris-normal)
* 眉 (eyebrows)
  * ❌ 困り眉2 (eyebrows-troubled2)
  * ❌ 困り眉1 (eyebrows-troubled1)
  * ❌ 上がり眉 (eyebrows-raised)
  * 🫛 怒り眉 (eyebrows-angry)
  * ❌ 普通眉 (eyebrows-normal)
* 枝豆 (edamame)
  * ❌ 枝豆萎え (edamame-wilted)
  * 🫛 枝豆通常 (edamame-normal)
  * ❌ パーカー(裏地とセットで使用) (hoodie)
* 記号など (signs)
  * ❌ 汗3 (sweat3)
  * ❌ 汗2 (sweat2)
  * ❌ 汗1 (sweat1)
  * ❌ 涙 (tears)
  * ❌ アヒルちゃん (duckling)

## 🤝 利用規約

私(EOWNERDEAD)は何に使っても問題ないのだ。
ただし、私(EOWNERDEAD)は使用によって生じる責任は一切を負わないのだ。
あとは[東北ずん子・ずんだもんプロジェクト](https://zunko.jp)
([キャラクター利用の手引き](https://zunko.jp/guideline.html))と
坂本アヒルさん([readme.txtの注意書き](./readme-original.txt))次第なのだ。

## ❤️ 謝辞

* [ずんだもん立ち絵素材](https://seiga.nicovideo.jp/seiga/im10788496)
* [東北ずん子・ずんだもんプロジェクト](https://zunko.jp)
* [psd2svg](https://github.com/kyamagu/psd2svg)
* [Inkscape](https://inkscape.org)
* [VTracer](https://github.com/visioncortex/vtracer)
