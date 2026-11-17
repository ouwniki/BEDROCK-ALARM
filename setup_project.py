import os
import wave
import math
import struct

def generate_signature_alarm_wav(filepath):
    """Membangkitkan audio sirine tinju + ritme ketukan khas IronWake secara offline."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    sample_rate = 22050
    duration = 4.0
    num_samples = int(sample_rate * duration)

    with wave.open(filepath, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)

        frames = bytearray()
        for i in range(num_samples):
            t = i / sample_rate
            cycle = t % 1.0
            if cycle < 0.22:
                freq = 880.0 + (cycle * 1400.0)
                env = 0.95
            elif 0.28 <= cycle < 0.50:
                freq = 980.0 + ((cycle - 0.28) * 1600.0)
                env = 0.95
            elif 0.56 <= cycle < 0.88:
                freq = 1150.0 - ((cycle - 0.56) * 900.0)
                env = 1.0
            else:
                freq = 220.0
                env = 0.15

            val = (
                0.65 * math.sin(2.0 * math.pi * freq * t) +
                0.25 * math.sin(2.0 * math.pi * (freq * 1.5) * t) +
                0.10 * math.sin(2.0 * math.pi * 110.0 * t)
            ) * env

            sample = max(-32767, min(32767, int(val * 32767)))
            frames.extend(struct.pack('<h', sample))

        wav_file.writeframes(bytes(frames))

generate_signature_alarm_wav("app/src/main/res/raw/wake_up_speech.wav")

files = {
    "settings.gradle.kts": r"""pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "IronWake"
include(":app")
""",

    "build.gradle.kts": r"""plugins {
    id("com.android.application") version "8.2.2" apply false
    id("org.jetbrains.kotlin.android") version "1.9.22" apply false
}
""",

    "gradle.properties": r"""org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
kotlin.code.style=official
android.nonTransitiveRClass=true
""",

    "app/build.gradle.kts": r"""plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.example.ironwake"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.ironwake"
        minSdk = 26
        targetSdk = 34
        versionCode = 6
        versionName = "5.1-NopjekDLC"
    }

    buildFeatures {
        compose = true
    }
    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.8"
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = "17"
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.7.0")
    implementation("androidx.activity:activity-compose:1.8.2")
    implementation(platform("androidx.compose:compose-bom:2024.02.00"))
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.ui:ui-graphics")
    implementation("androidx.compose.ui:ui-tooling-preview")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.compose.material:material-icons-extended")
}
""",

    "app/src/main/res/values/strings.xml": r"""<resources>
    <string name="app_name">IronWake Alarm</string>
</resources>
""",

    "app/src/main/res/xml/device_admin_policies.xml": r"""<?xml version="1.0" encoding="utf-8"?>
<device-admin xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-policies>
        <force-lock />
    </uses-policies>
</device-admin>
""",

    "app/src/main/res/drawable/ic_launcher_background.xml": r"""<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <path android:fillColor="#0D0D10" android:pathData="M0,0h108v108h-108z" />
    <path android:fillColor="#26FFD700" android:pathData="M54,54m-42,0a42,42 0,1 1,84 0a42,42 0,1 1,-84 0" />
    <path android:strokeColor="#D32F2F" android:strokeWidth="3" android:pathData="M54,54m-44,0a44,44 0,1 1,88 0a44,44 0,1 1,-88 0" />
</vector>
""",

    "app/src/main/res/drawable/ic_launcher_foreground.xml": r"""<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <path
        android:fillColor="#D32F2F"
        android:strokeColor="#FFD700"
        android:strokeWidth="2.5"
        android:pathData="M34,42 C34,28 74,28 74,42 C78,54 71,70 54,70 C37,70 30,54 34,42 Z" />
    <path
        android:strokeColor="#FF8A80"
        android:strokeWidth="2"
        android:pathData="M40,42 Q54,36 68,42" />
    <path
        android:fillColor="#FFD700"
        android:pathData="M41,68 L67,68 L64,78 L44,78 Z" />
    <path
        android:fillColor="#FFFFFF"
        android:pathData="M56,22 L47,38 L54,38 L50,52 L63,35 L55,35 Z" />
</vector>
""",

    "app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml": r"""<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_launcher_foreground" />
</adaptive-icon>
""",

    "app/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml": r"""<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_launcher_foreground" />
</adaptive-icon>
""",

    "app/src/main/res/drawable/bg_boxer_punch.xml": r"""<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="400dp"
    android:height="800dp"
    android:viewportWidth="400"
    android:viewportHeight="800">
    <path android:fillColor="#0D0D0D" android:pathData="M0,0h400v800h-400z" />
    <path android:strokeColor="#33D32F2F" android:strokeWidth="6" android:pathData="M200,380 L0,100 M200,380 L400,100 M200,380 L0,680 M200,380 L400,680 M200,380 L200,0 M200,380 L200,800" />
    <path android:fillColor="#26FFD700" android:pathData="M200,380m-140,0a140,140 0,1 1,280 0a140,140 0,1 1,-280 0" />
    <path android:fillColor="#1C1C1C" android:pathData="M270,580 L380,750 L230,780 L170,480 Z" />
    <path android:fillColor="#B71C1C" android:strokeColor="#FFD700" android:strokeWidth="5" android:pathData="M110,330 C110,260 290,260 290,330 C305,390 275,465 200,465 C125,465 95,390 110,330 Z" />
    <path android:strokeColor="#FF5252" android:strokeWidth="4" android:pathData="M135,325 Q200,300 265,325" />
    <path android:fillColor="#D4AF37" android:pathData="M145,455 L255,455 L245,495 L155,495 Z" />
</vector>
""",

    "app/src/main/AndroidManifest.xml": r"""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
    <uses-permission android:name="android.permission.USE_EXACT_ALARM" />
    <uses-permission android:name="android.permission.USE_FULL_SCREEN_INTENT" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@android:style/Theme.Material.NoActionBar">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:screenOrientation="portrait">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <activity
            android:name=".AlarmRingingActivity"
            android:exported="false"
            android:excludeFromRecents="true"
            android:launchMode="singleInstance"
            android:screenOrientation="portrait"
            android:showWhenLocked="true"
            android:turnScreenOn="true" />

        <receiver
            android:name=".receiver.AlarmReceiver"
            android:enabled="true"
            android:exported="false" />

        <receiver
            android:name=".receiver.IronWakeAdminReceiver"
            android:description="@string/app_name"
            android:label="IronWake Anti-Cheat Protection"
            android:permission="android.permission.BIND_DEVICE_ADMIN"
            android:exported="true">
            <meta-data
                android:name="android.app.device_admin"
                android:resource="@xml/device_admin_policies" />
            <intent-filter>
                <action android:name="android.app.action.DEVICE_ADMIN_ENABLED" />
                <action android:name="android.app.action.DEVICE_ADMIN_DISABLE_REQUESTED" />
                <action android:name="android.app.action.DEVICE_ADMIN_DISABLED" />
            </intent-filter>
        </receiver>

        <service
            android:name=".service.AlarmService"
            android:enabled="true"
            android:exported="false"
            android:foregroundServiceType="mediaPlayback" />

    </application>
</manifest>
""",

    "app/src/main/java/com/example/ironwake/ui/theme/Theme.kt": r"""package com.example.ironwake.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

val IronBlack = Color(0xFF0B0B0D)
val IronSurface = Color(0xFF16161A)
val IronRed = Color(0xFFD32F2F)
val IronCrimson = Color(0xFFFF1744)
val IronGold = Color(0xFFFFD700)
val IronEmerald = Color(0xFF00E676)
val IronCyan = Color(0xFF00E5FF)

private val IronDarkColorScheme = darkColorScheme(
    primary = IronRed,
    onPrimary = Color.White,
    secondary = IronGold,
    onSecondary = Color.Black,
    background = IronBlack,
    surface = IronSurface,
    onBackground = Color.White,
    onSurface = Color.White,
    error = IronCrimson
)

@Composable
fun IronWakeTheme(content: @Composable () -> Unit) {
    MaterialTheme(colorScheme = IronDarkColorScheme, content = content)
}
""",

    "app/src/main/java/com/example/ironwake/model/MathProblem.kt": r"""package com.example.ironwake.model

enum class MathTopic(val displayName: String) {
    NOPJEK_DLC("Nopjek DLC (Kedokteran Gigi Umum)"),
    QUADRATIC("Persamaan Kuadrat & Akar"),
    LOG_EXP("Logaritma & Eksponen"),
    CALCULUS("Turunan & Integral Dasar"),
    SEQUENCE("Barisan & Deret (Aritmatika/Geometri)"),
    TRIG_MATRIX("Trigonometri & Matriks 2x2")
}

enum class Difficulty(val label: String, val durationSeconds: Int) {
    NORMAL("Standar (90 dtk)", 90),
    HARD("Intensif (60 dtk)", 60)
}

data class MathProblem(
    val topic: MathTopic,
    val question: String,
    val correctAnswer: Int,
    val hint: String,
    val tutorSteps: List<String>
)
""",

    "app/src/main/java/com/example/ironwake/util/MathGenerator.kt": r"""package com.example.ironwake.util

import com.example.ironwake.model.Difficulty
import com.example.ironwake.model.MathProblem
import com.example.ironwake.model.MathTopic
import kotlin.math.pow
import kotlin.random.Random

object MathGenerator {
    fun generateProblem(enabledTopics: Set<MathTopic>, difficulty: Difficulty): MathProblem {
        val pool = if (enabledTopics.isEmpty()) MathTopic.entries else enabledTopics.toList()
        return when (pool.random()) {
            MathTopic.NOPJEK_DLC -> generateNopjekDental(difficulty)
            MathTopic.QUADRATIC -> generateQuadratic(difficulty)
            MathTopic.LOG_EXP -> generateLogExp(difficulty)
            MathTopic.CALCULUS -> generateCalculus(difficulty)
            MathTopic.SEQUENCE -> generateSequence(difficulty)
            MathTopic.TRIG_MATRIX -> generateTrigOrMatrix(difficulty)
        }
    }

    private fun generateNopjekDental(difficulty: Difficulty): MathProblem {
        val dentalBank = listOf(
            // 1. Nomenklatur FDI
            MathProblem(
                topic = MathTopic.NOPJEK_DLC,
                question = "[NOPJEK DLC - ANATOMI GIGI]\nDalam sistem penomoran FDI, gigi Molar Pertama Permanen Kanan Bawah memiliki kode nomor berapa?",
                correctAnswer = 46,
                hint = "Kuadran 4 = kanan bawah permanen, gigi ke-6 dari garis median",
                tutorSteps = listOf(
                    "Sistem FDI terdiri dari 2 digit: digit pertama = kuadran, digit kedua = urutan gigi dari garis tengah (median).",
                    "Kuadran gigi permanen: 1 (kanan atas), 2 (kiri atas), 3 (kiri bawah), 4 (kanan bawah).",
                    "Urutan gigi dari median: 1 (insisivus sentral), 2 (insisivus lateral), 3 (kaninus), 4 (premolar 1), 5 (premolar 2), 6 (molar 1).",
                    "Gabungkan kuadran kanan bawah (4) dan urutan molar pertama (6)!"
                )
            ),
            MathProblem(
                topic = MathTopic.NOPJEK_DLC,
                question = "[NOPJEK DLC - ANATOMI GIGI]\nDalam sistem FDI, gigi Kaninus Permanen Kiri Atas memiliki nomor berapa?",
                correctAnswer = 23,
                hint = "Kuadran 2 = kiri atas permanen, kaninus = urutan ke-3",
                tutorSteps = listOf(
                    "Identifikasi kuadran gigi permanen: Kiri atas adalah kuadran 2.",
                    "Urutan gigi dari garis tengah: 1 = Insisivus 1, 2 = Insisivus 2, 3 = Kaninus.",
                    "Gabungkan kode kuadran (2) dengan posisi kaninus (3)!"
                )
            ),
            MathProblem(
                topic = MathTopic.NOPJEK_DLC,
                question = "[NOPJEK DLC - PEDODONSIA]\nDalam sistem FDI, gigi Molar Kedua Sulung (Gigi Susu) Kiri Bawah memiliki kode nomor berapa?",
                correctAnswer = 75,
                hint = "Kuadran gigi sulung: 5, 6, 7 (kiri bawah), 8; molar kedua = urutan ke-5",
                tutorSteps = listOf(
                    "Kuadran gigi sulung dimulai dari angka 5 sampai 8 searah jarum jam:",
                    "5 = kanan atas, 6 = kiri atas, 7 = kiri bawah, 8 = kanan bawah.",
                    "Urutan gigi sulung per kuadran hanya ada 5 gigi (1–5), di mana nomor 5 adalah Molar Kedua Sulung.",
                    "Gabungkan kuadran kiri bawah sulung (7) dengan urutan ke-5!"
                )
            ),
            // 2. Jumlah Gigi & Morfologi
            MathProblem(
                topic = MathTopic.NOPJEK_DLC,
                question = "[NOPJEK DLC - ODONTOLOGI]\nBerapa total jumlah seluruh gigi sulung (gigi susu) lengkap pada anak-anak?",
                correctAnswer = 20,
                hint = "Setiap kuadran memiliki 5 gigi (2 insisivus, 1 kaninus, 2 molar)",
                tutorSteps = listOf(
                    "Pada periode gigi sulung, belum terdapat gigi premolar maupun molar ketiga.",
                    "Setiap kuadran terdiri dari: 2 insisivus + 1 kaninus + 2 molar = 5 gigi.",
                    "Kalikan jumlah gigi per kuadran (5) dengan total 4 kuadran rahang!"
                )
            ),
            MathProblem(
                topic = MathTopic.NOPJEK_DLC,
                question = "[NOPJEK DLC - ODONTOLOGI]\nBerapa total jumlah seluruh gigi permanen lengkap pada manusia dewasa (termasuk M3)?",
                correctAnswer = 32,
                hint = "Setiap kuadran memiliki 8 gigi × 4 kuadran",
                tutorSteps = listOf(
                    "Pada periode gigi permanen lengkap, setiap kuadran memiliki 8 gigi:",
                    "2 insisivus + 1 kaninus + 2 premolar + 3 molar = 8 gigi per kuadran.",
                    "Kalikan 8 gigi dengan 4 kuadran (kanan/kiri, atas/bawah)!"
                )
            ),
            // 3. Karies & Konservasi Gigi
            MathProblem(
                topic = MathTopic.NOPJEK_DLC,
                question = "[NOPJEK DLC - KONSERVASI]\nMenurut klasifikasi G.V. Black, karies yang mengenai permukaan proksimal (mesial/distal) gigi posterior termasuk Kelas berapa?",
                correctAnswer = 2,
                hint = "Kelas I = pit & fisura; Kelas II = proksimal posterior; Kelas III = proksimal anterior",
                tutorSteps = listOf(
                    "Ingat urutan klasifikasi karies G.V. Black:",
                    "Kelas I: Pit dan fisura oklusal posterior / foramen caecum.",
                    "Kelas II: Permukaan proksimal (mesial/distal) gigi posterior (premolar dan molar).",
                    "Kelas III: Permukaan proksimal gigi anterior tanpa melibatkan tepi insisal."
                )
            ),
            MathProblem(
                topic = MathTopic.NOPJEK_DLC,
                question = "[NOPJEK DLC - KONSERVASI]\nKaries pada 1/3 servikal bagian fasial atau lingual semua gigi (baik anterior maupun posterior) menurut G.V. Black termasuk Kelas berapa?",
                correctAnswer = 5,
                hint = "Kelas IV = sudut insisal anterior; Kelas V = servikal gigi",
                tutorSteps = listOf(
                    "Ingat klasifikasi G.V. Black untuk lesi di dekat gusi (servikal):",
                    "Kelas IV melibatkan tepi/sudut insisal gigi anterior.",
                    "Kelas V berada pada 1/3 servikal (leher gigi) permukaan bukal/labial maupun lingual/palatal."
                )
            ),
            // 4. Farmakologi & Hitungan Klinis Dokter Gigi
            MathProblem(
                topic = MathTopic.NOPJEK_DLC,
                question = "[NOPJEK DLC - FARMAKOLOGI KLINIS]\nDosis maksimal Lidokain dengan vasokonstriktor adalah 7 mg/kgBB. Berapa mg dosis maksimal untuk pasien dengan berat 50 kg?",
                correctAnswer = 350,
                hint = "Dosis maksimal = 7 mg × berat badan pasien (kg)",
                tutorSteps = listOf(
                    "Diketahui dosis maksimal aman Lidokain (+ epinefrin) adalah 7 mg per kg berat badan.",
                    "Berat badan pasien adalah 50 kg.",
                    "Kalikan 7 mg/kg × 50 kg untuk memperoleh batas maksimal dalam miligram (mg)!"
                )
            ),
            MathProblem(
                topic = MathTopic.NOPJEK_DLC,
                question = "[NOPJEK DLC - FARMAKOLOGI KLINIS]\nSatu karpul anestesi lokal berisi 1,8 mL Lidokain 2% (20 mg/mL). Berapa mg kandungan Lidokain dalam 1 karpul tersebut?",
                correctAnswer = 36,
                hint = "2% = 20 mg/mL. Kalikan 20 mg × 1,8 mL",
                tutorSteps = listOf(
                    "Larutan konsentrasi 2% berarti terdapat 2 gram zat dalam 100 mL, atau sama dengan 20 mg/mL.",
                    "Volume 1 karpul standar kedokteran gigi adalah 1,8 mL.",
                    "Kalikan konsentrasi (20 mg/mL) dengan volume (1,8 mL)!"
                )
            ),
            // 5. IKGM (Indeks DMF-T)
            MathProblem(
                topic = MathTopic.NOPJEK_DLC,
                question = "[NOPJEK DLC - IKGM]\nHasil pemeriksaan odontogram pasien: 4 gigi karies (D), 2 gigi dicabut karena karies (M), dan 3 gigi ditambal baik (F). Berapa skor DMF-T pasien?",
                correctAnswer = 9,
                hint = "DMF-T = Decayed (D) + Missing (M) + Filled (F)",
                tutorSteps = listOf(
                    "Indeks DMF-T menghitung total pengalaman karies gigi permanen individu.",
                    "Rumus: DMF-T = D (Decayed/karies) + M (Missing/hilang) + F (Filled/tumpatan).",
                    "Jumlahkan seluruh komponen: 4 + 2 + 3!"
                )
            )
        )
        return dentalBank.random()
    }

    private fun generateQuadratic(difficulty: Difficulty): MathProblem {
        val x1 = Random.nextInt(-6, 8).let { if (it == 0) 2 else it }
        val x2 = Random.nextInt(-5, 9).let { if (it == 0) 3 else it }
        val b = -(x1 + x2)
        val c = x1 * x2
        val bStr = if (b >= 0) "+ ${b}x" else "- ${-b}x"
        val cStr = if (c >= 0) "+ $c" else "- ${-c}"

        return if (difficulty == Difficulty.NORMAL) {
            MathProblem(
                topic = MathTopic.QUADRATIC,
                question = "Jika x₁ dan x₂ akar dari:\nx² $bStr $cStr = 0\nTentukan nilai (x₁ + x₂)!",
                correctAnswer = x1 + x2,
                hint = "Gunakan rumus jumlah akar Vieta: x₁ + x₂ = -b / a",
                tutorSteps = listOf(
                    "Identifikasi koefisien persamaan kuadrat ax² + bx + c = 0:",
                    "Didapat a = 1, b = $b, dan c = $c.",
                    "Gunakan rumus Vieta untuk jumlah akar: x₁ + x₂ = -b / a.",
                    "Substitusikan nilai: x₁ + x₂ = -($b) / 1.",
                    "Hitung hasil akhirnya dan masukkan ke kolom jawaban!"
                )
            )
        } else {
            MathProblem(
                topic = MathTopic.QUADRATIC,
                question = "Akar persamaan x² $bStr $cStr = 0 adalah x₁ dan x₂.\nHitung nilai x₁² + x₂²!",
                correctAnswer = (x1 * x1) + (x2 * x2),
                hint = "Ubah bentuk menjadi (x₁ + x₂)² - 2(x₁·x₂)",
                tutorSteps = listOf(
                    "Dari x² $bStr $cStr = 0, tentukan a = 1, b = $b, c = $c.",
                    "Cari jumlah akar: x₁ + x₂ = -b/a = ${-b}.",
                    "Cari hasil kali akar: x₁ · x₂ = c/a = $c.",
                    "Gunakan identitas aljabar: x₁² + x₂² = (x₁ + x₂)² - 2(x₁ · x₂).",
                    "Substitusi: (${-b})² - 2($c), lalu hitung hasil akhirnya!"
                )
            )
        }
    }

    private fun generateLogExp(difficulty: Difficulty): MathProblem {
        return if (Random.nextBoolean()) {
            val base1 = listOf(2, 3, 5).random()
            val exp1 = Random.nextInt(2, 5)
            val val1 = base1.toDouble().pow(exp1).toInt()
            val base2 = listOf(2, 3, 4).random()
            val exp2 = Random.nextInt(1, 4)
            val val2 = base2.toDouble().pow(exp2).toInt()
            MathProblem(
                topic = MathTopic.LOG_EXP,
                question = "Hitung nilai:\n^${base1}log($val1) + ^${base2}log($val2) = ...",
                correctAnswer = exp1 + exp2,
                hint = "Ingat sifat dasar logaritma: ᵃlog(aⁿ) = n",
                tutorSteps = listOf(
                    "Ubah angka di dalam logaritma menjadi bentuk pangkat dari basisnya:",
                    "Suku pertama: $val1 = $base1 pangkat berapa? ($base1^$exp1 = $val1), sehingga ^${base1}log($val1) = $exp1.",
                    "Suku kedua: $val2 = $base2 pangkat berapa? ($base2^$exp2 = $val2), sehingga ^${base2}log($val2) = $exp2.",
                    "Jumlahkan kedua hasil pangkat tersebut ($exp1 + $exp2)!"
                )
            )
        } else {
            val base = listOf(2, 3, 5).random()
            val x = Random.nextInt(2, 7)
            val k = Random.nextInt(1, 5)
            val expRes = (2 * x) - k
            val rhs = base.toDouble().pow(expRes).toInt()
            MathProblem(
                topic = MathTopic.LOG_EXP,
                question = "Tentukan nilai x:\n$base^(2x - $k) = $rhs",
                correctAnswer = x,
                hint = "Samakan basis pangkat di ruas kiri dan kanan (${base}^n)",
                tutorSteps = listOf(
                    "Ubah ruas kanan ($rhs) menjadi bilangan berpangkat dengan basis $base:",
                    "Karena $base^$expRes = $rhs, maka persamaan menjadi: $base^(2x - $k) = $base^$expRes.",
                    "Karena basis sudah sama, samakan pangkatnya: 2x - $k = $expRes.",
                    "Pindahkan -$k ke ruas kanan: 2x = $expRes + $k = ${expRes + k}.",
                    "Bagi kedua ruas dengan 2 untuk mendapatkan nilai x!"
                )
            )
        }
    }

    private fun generateCalculus(difficulty: Difficulty): MathProblem {
        return if (Random.nextBoolean()) {
            val a = Random.nextInt(1, 4)
            val b = Random.nextInt(2, 7)
            val c = Random.nextInt(1, 10)
            val k = if (difficulty == Difficulty.NORMAL) Random.nextInt(1, 3) else Random.nextInt(2, 5)
            MathProblem(
                topic = MathTopic.CALCULUS,
                question = "Diketahui f(x) = ${a}x³ + ${b}x² + ${c}x.\nTentukan f'($k)!",
                correctAnswer = (3 * a * k * k) + (2 * b * k) + c,
                hint = "Turunan axⁿ adalah (a·n)xⁿ⁻¹",
                tutorSteps = listOf(
                    "Turunkan setiap suku f(x) menggunakan aturan pangkat d/dx(xⁿ) = n·xⁿ⁻¹:",
                    "Turunan ${a}x³ adalah ${3 * a}x².",
                    "Turunan ${b}x² adalah ${2 * b}x, dan turunan ${c}x adalah $c.",
                    "Diperoleh f'(x) = ${3 * a}x² + ${2 * b}x + $c.",
                    "Substitusikan x = $k: ${3 * a}($k)² + ${2 * b}($k) + $c, lalu jumlahkan!"
                )
            )
        } else {
            val a = Random.nextInt(1, 3)
            val c = Random.nextInt(1, 5)
            val upper = Random.nextInt(2, 4)
            MathProblem(
                topic = MathTopic.CALCULUS,
                question = "Hitung integral tentu:\n∫ (0 sampai $upper) (${3 * a}x² + ${2 * c}x) dx",
                correctAnswer = (a * upper * upper * upper) + (c * upper * upper),
                hint = "Integral axⁿ dx = [a/(n+1)]xⁿ⁺¹",
                tutorSteps = listOf(
                    "Cari anti-turunan (integral tak tentu) dari (${3 * a}x² + ${2 * c}x):",
                    "∫ ${3 * a}x² dx = (${3 * a}/3)x³ = ${a}x³.",
                    "∫ ${2 * c}x dx = (${2 * c}/2)x² = ${c}x².",
                    "Masukkan batas atas x = $upper dan batas bawah x = 0 ke F(x) = ${a}x³ + ${c}x².",
                    "Hitung F($upper) - F(0) = [${a}($upper)³ + ${c}($upper)²] - 0!"
                )
            )
        }
    }

    private fun generateSequence(difficulty: Difficulty): MathProblem {
        return if (Random.nextBoolean()) {
            val a = Random.nextInt(3, 15)
            val b = Random.nextInt(3, 9)
            val n = if (difficulty == Difficulty.NORMAL) Random.nextInt(8, 15) else Random.nextInt(15, 25)
            MathProblem(
                topic = MathTopic.SEQUENCE,
                question = "Barisan aritmatika a = $a dan b = $b.\nTentukan suku ke-$n (U$n)!",
                correctAnswer = a + (n - 1) * b,
                hint = "Gunakan rumus suku ke-n aritmatika: Un = a + (n - 1)b",
                tutorSteps = listOf(
                    "Diketahui suku pertama a = $a, beda b = $b, dan n = $n.",
                    "Tuliskan rumus suku ke-n barisan aritmatika: Un = a + (n - 1) · b.",
                    "Substitusikan angka: U$n = $a + ($n - 1) · $b.",
                    "Hitung dalam kurung terlebih dahulu: ($n - 1) = ${n - 1}, lalu kalikan dengan $b.",
                    "Tambahkan hasilnya dengan suku pertama ($a)!"
                )
            )
        } else {
            val a = Random.nextInt(2, 6)
            val r = listOf(2, 3).random()
            val n = Random.nextInt(4, 6)
            MathProblem(
                topic = MathTopic.SEQUENCE,
                question = "Barisan geometri a = $a dan r = $r.\nTentukan suku ke-$n (U$n)!",
                correctAnswer = a * r.toDouble().pow(n - 1).toInt(),
                hint = "Gunakan rumus suku ke-n geometri: Un = a · rⁿ⁻¹",
                tutorSteps = listOf(
                    "Diketahui suku pertama a = $a, rasio r = $r, dan n = $n.",
                    "Gunakan rumus suku ke-n barisan geometri: Un = a · r^(n - 1).",
                    "Substitusikan: U$n = $a · $r^($n - 1) = $a · $r^${n - 1}.",
                    "Hitung nilai perpangkatan $r^${n - 1} terlebih dahulu.",
                    "Kalikan hasil pangkat tersebut dengan $a!"
                )
            )
        }
    }

    private fun generateTrigOrMatrix(difficulty: Difficulty): MathProblem {
        return if (Random.nextBoolean()) {
            val a = Random.nextInt(2, 9)
            val b = Random.nextInt(1, 7)
            val c = Random.nextInt(1, 7)
            val d = Random.nextInt(2, 9)
            MathProblem(
                topic = MathTopic.TRIG_MATRIX,
                question = "Matriks A = [ [$a, $b], [$c, $d] ].\nTentukan det(A)!",
                correctAnswer = (a * d) - (b * c),
                hint = "Determinan matriks 2x2 = (a · d) - (b · c)",
                tutorSteps = listOf(
                    "Untuk matriks 2x2 berbentuk [ [a, b], [c, d] ]:",
                    "Diagonal utama adalah a = $a dan d = $d. Kalikan keduanya: $a × $d = ${a * d}.",
                    "Diagonal samping adalah b = $b dan c = $c. Kalikan keduanya: $b × $c = ${b * c}.",
                    "Kurangkan hasil diagonal utama dengan diagonal samping: (${a * d}) - (${b * c})!"
                )
            )
        } else {
            val variants = listOf(
                Triple(
                    "Hitung: 4·sin(30°) + 6·cos(60°)!",
                    5,
                    listOf(
                        "Ingat tabel sudut istimewa trigonometri:",
                        "Nilai sin(30°) = 1/2, dan cos(60°) = 1/2.",
                        "Substitusikan ke soal: 4 × (1/2) + 6 × (1/2).",
                        "Hitung masing-masing perkalian (2 + 3) dan jumlahkan!"
                    )
                ),
                Triple(
                    "Hitung: 3·tan(45°) + 2·sin(90°)!",
                    5,
                    listOf(
                        "Ingat nilai sudut istimewa trigonometri:",
                        "Nilai tan(45°) = 1, dan sin(90°) = 1.",
                        "Substitusikan ke persamaan: 3 × (1) + 2 × (1).",
                        "Jumlahkan kedua hasilnya!"
                    )
                ),
                Triple(
                    "Hitung: 8·cos(60°) + 5·tan(45°) - cos(0°)!",
                    8,
                    listOf(
                        "Ingat nilai sudut istimewa trigonometri:",
                        "cos(60°) = 1/2, tan(45°) = 1, dan cos(0°) = 1.",
                        "Substitusikan: 8 × (1/2) + 5 × (1) - 1.",
                        "Sederhanakan menjadi: 4 + 5 - 1, lalu hitung hasilnya!"
                    )
                )
            )
            val chosen = variants.random()
            MathProblem(
                topic = MathTopic.TRIG_MATRIX,
                question = chosen.first,
                correctAnswer = chosen.second,
                hint = "Gunakan nilai sudut istimewa 0°, 30°, 45°, 60°, 90°",
                tutorSteps = chosen.third
            )
        }
    }
}
""",

    "app/src/main/java/com/example/ironwake/util/AlarmScheduler.kt": r"""package com.example.ironwake.util

import android.app.AlarmManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.os.Build
import com.example.ironwake.receiver.AlarmReceiver
import java.util.Calendar

object AlarmScheduler {
    fun scheduleAlarm(context: Context, hour: Int, minute: Int) {
        val alarmManager = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val calendar = Calendar.getInstance().apply {
            set(Calendar.HOUR_OF_DAY, hour)
            set(Calendar.MINUTE, minute)
            set(Calendar.SECOND, 0)
            set(Calendar.MILLISECOND, 0)
            if (timeInMillis <= System.currentTimeMillis()) add(Calendar.DAY_OF_YEAR, 1)
        }
        val intent = Intent(context, AlarmReceiver::class.java).apply {
            putExtra("IS_TEST_MODE", false)
        }
        val pendingIntent = PendingIntent.getBroadcast(context, 1001, intent, PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE)

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S && !alarmManager.canScheduleExactAlarms()) return
        alarmManager.setExactAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, calendar.timeInMillis, pendingIntent)
    }

    fun cancelAlarm(context: Context) {
        val alarmManager = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val intent = Intent(context, AlarmReceiver::class.java)
        val pendingIntent = PendingIntent.getBroadcast(context, 1001, intent, PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE)
        alarmManager.cancel(pendingIntent)
    }
}
""",

    "app/src/main/java/com/example/ironwake/receiver/AlarmReceiver.kt": r"""package com.example.ironwake.receiver

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.os.Build
import com.example.ironwake.service.AlarmService

class AlarmReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent?) {
        val isTestMode = intent?.getBooleanExtra("IS_TEST_MODE", false) ?: false
        val serviceIntent = Intent(context, AlarmService::class.java).apply {
            putExtra("IS_TEST_MODE", isTestMode)
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) context.startForegroundService(serviceIntent)
        else context.startService(serviceIntent)
    }
}
""",

    "app/src/main/java/com/example/ironwake/receiver/IronWakeAdminReceiver.kt": r"""package com.example.ironwake.receiver

import android.app.admin.DeviceAdminReceiver
import android.content.Context
import android.content.Intent
import android.widget.Toast
import com.example.ironwake.service.AlarmService

class IronWakeAdminReceiver : DeviceAdminReceiver() {
    override fun onEnabled(context: Context, intent: Intent) {
        super.onEnabled(context, intent)
        Toast.makeText(context, "Proteksi Anti-Kabur AKTIF!", Toast.LENGTH_SHORT).show()
    }

    override fun onDisableRequested(context: Context, intent: Intent): CharSequence {
        if (AlarmService.isAlarmRinging && !AlarmService.isTestMode) {
            runCatching { getManager(context).lockNow() }
            return "CURANG TERDETEKSI! Selesaikan 5 soal misi!"
        }
        return "Menonaktifkan proteksi ini membuka kunci Force Stop & Uninstall."
    }
}
""",

    "app/src/main/java/com/example/ironwake/service/AlarmService.kt": r"""package com.example.ironwake.service

import android.app.*
import android.content.Context
import android.content.Intent
import android.media.AudioAttributes
import android.media.AudioManager
import android.media.MediaPlayer
import android.media.RingtoneManager
import android.os.*
import android.speech.tts.TextToSpeech
import androidx.core.app.NotificationCompat
import com.example.ironwake.AlarmRingingActivity
import java.util.Locale

class AlarmService : Service(), TextToSpeech.OnInitListener {
    private var mediaPlayer: MediaPlayer? = null
    private var tts: TextToSpeech? = null
    private var isTtsReady = false
    private lateinit var audioManager: AudioManager
    private var vibrator: Vibrator? = null
    private val handler = Handler(Looper.getMainLooper())

    companion object {
        const val CHANNEL_ID = "IRON_WAKE_ALARM_CHANNEL"
        const val NOTIFICATION_ID = 999
        const val ACTION_PAUSE_FOR_STUDY = "com.example.ironwake.ACTION_PAUSE_FOR_STUDY"
        const val ACTION_RESUME_ALARM = "com.example.ironwake.ACTION_RESUME_ALARM"
        const val ACTION_CELEBRATE = "com.example.ironwake.ACTION_CELEBRATE"

        var isAlarmRinging = false
        var isPausedForStudy = false
        var isTestMode = false
        var isCelebrating = false
    }

    private val enforcementRunnable = object : Runnable {
        override fun run() {
            if (!isAlarmRinging || isPausedForStudy || isCelebrating) return
            forceMaxAlarmVolume()
            if (isTtsReady) speakMotivation()
            handler.postDelayed(this, 4200L)
        }
    }

    override fun onCreate() {
        super.onCreate()
        audioManager = getSystemService(Context.AUDIO_SERVICE) as AudioManager
        vibrator = getSystemService(Context.VIBRATOR_SERVICE) as Vibrator
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(CHANNEL_ID, "IronWake Alarm", NotificationManager.IMPORTANCE_HIGH).apply {
                setBypassDnd(true)
            }
            getSystemService(NotificationManager::class.java).createNotificationChannel(channel)
        }
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        when (intent?.action) {
            ACTION_PAUSE_FOR_STUDY -> {
                pauseAudioForStudy()
                return START_STICKY
            }
            ACTION_RESUME_ALARM -> {
                resumeAlarmAudio()
                return START_STICKY
            }
            ACTION_CELEBRATE -> {
                triggerCelebrationAudio()
                return START_NOT_STICKY
            }
        }

        isTestMode = intent?.getBooleanExtra("IS_TEST_MODE", false) ?: false
        isAlarmRinging = true
        isPausedForStudy = false
        isCelebrating = false

        val fullScreenIntent = Intent(this, AlarmRingingActivity::class.java).apply {
            addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP)
            putExtra("IS_TEST_MODE", isTestMode)
        }
        val fullScreenPendingIntent = PendingIntent.getActivity(
            this, 0, fullScreenIntent, PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )

        val notification = NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(android.R.drawable.ic_lock_idle_alarm)
            .setContentTitle("WAKE UP YOU LAZY KIDS!")
            .setContentText(if (isTestMode) "Mode Uji Coba Alarm Aktif" else "Selesaikan 5 soal misi bangun!")
            .setPriority(NotificationCompat.PRIORITY_MAX)
            .setCategory(NotificationCompat.CATEGORY_ALARM)
            .setOngoing(true)
            .setFullScreenIntent(fullScreenPendingIntent, true)
            .build()

        startForeground(NOTIFICATION_ID, notification)
        startActivity(fullScreenIntent)

        if (tts == null) {
            tts = TextToSpeech(this, this)
        }
        startSignatureSoundAndVibration()
        return START_STICKY
    }

    private fun startSignatureSoundAndVibration() {
        isPausedForStudy = false
        forceMaxAlarmVolume()

        val pattern = longArrayOf(0, 600, 300, 600)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            vibrator?.vibrate(VibrationEffect.createWaveform(pattern, 0))
        }

        if (mediaPlayer == null) {
            val rawResId = resources.getIdentifier("wake_up_speech", "raw", packageName)
            if (rawResId != 0) {
                runCatching {
                    mediaPlayer = MediaPlayer().apply {
                        setAudioAttributes(AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_ALARM).build())
                        val afd = resources.openRawResourceFd(rawResId)
                        setDataSource(afd.fileDescriptor, afd.startOffset, afd.length)
                        afd.close()
                        isLooping = true
                        setVolume(0.75f, 0.75f)
                        prepare()
                        start()
                    }
                }
            }
        } else if (mediaPlayer?.isPlaying == false) {
            runCatching { mediaPlayer?.start() }
        }

        handler.removeCallbacks(enforcementRunnable)
        handler.post(enforcementRunnable)
    }

    private fun pauseAudioForStudy() {
        isPausedForStudy = true
        handler.removeCallbacks(enforcementRunnable)
        runCatching {
            if (mediaPlayer?.isPlaying == true) mediaPlayer?.pause()
        }
        runCatching { tts?.stop() }
        vibrator?.cancel()
    }

    private fun resumeAlarmAudio() {
        if (isCelebrating) return
        isAlarmRinging = true
        startSignatureSoundAndVibration()
    }

    private fun triggerCelebrationAudio() {
        isCelebrating = true
        isAlarmRinging = false
        isPausedForStudy = false
        handler.removeCallbacks(enforcementRunnable)

        runCatching { mediaPlayer?.stop(); mediaPlayer?.release() }
        mediaPlayer = null
        vibrator?.cancel()

        runCatching {
            val notifUri = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION)
            RingtoneManager.getRingtone(this, notifUri)?.play()
        }

        if (isTtsReady) {
            tts?.setPitch(1.18f)
            tts?.setSpeechRate(1.05f)
            val params = Bundle().apply { putInt(TextToSpeech.Engine.KEY_PARAM_STREAM, AudioManager.STREAM_ALARM) }
            tts?.speak(
                "SURPRISE! YOU DID IT! Great job champion! All 5 missions completed. Have an awesome productive day!",
                TextToSpeech.QUEUE_FLUSH,
                params,
                "IRON_WAKE_CELEBRATION"
            )
        }
    }

    private fun forceMaxAlarmVolume() {
        runCatching {
            val maxVol = audioManager.getStreamMaxVolume(AudioManager.STREAM_ALARM)
            audioManager.setStreamVolume(AudioManager.STREAM_ALARM, maxVol, 0)
        }
    }

    override fun onInit(status: Int) {
        if (status == TextToSpeech.SUCCESS) {
            tts?.language = Locale.US
            tts?.setPitch(0.80f)
            tts?.setSpeechRate(1.08f)
            isTtsReady = true
            if (isAlarmRinging && !isPausedForStudy && !isCelebrating) {
                speakMotivation()
            }
        }
    }

    private fun speakMotivation() {
        val prefs = getSharedPreferences("IronWakePrefs", Context.MODE_PRIVATE)
        val shoutText = prefs.getString("motivation_text", "WAKE UP YOU LAZY KIDS!") ?: "WAKE UP YOU LAZY KIDS!"
        val params = Bundle().apply { putInt(TextToSpeech.Engine.KEY_PARAM_STREAM, AudioManager.STREAM_ALARM) }
        tts?.speak(shoutText, TextToSpeech.QUEUE_FLUSH, params, "IRON_WAKE_TTS")
    }

    override fun onDestroy() {
        isAlarmRinging = false
        isPausedForStudy = false
        isCelebrating = false
        isTestMode = false
        handler.removeCallbacks(enforcementRunnable)
        runCatching { mediaPlayer?.stop(); mediaPlayer?.release() }
        runCatching { tts?.stop(); tts?.shutdown() }
        vibrator?.cancel()
        super.onDestroy()
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
""",

    "app/src/main/java/com/example/ironwake/AlarmRingingActivity.kt": r"""package com.example.ironwake

import android.app.KeyguardManager
import android.content.Context
import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.view.WindowManager
import androidx.activity.ComponentActivity
import androidx.activity.OnBackPressedCallback
import androidx.activity.compose.setContent
import com.example.ironwake.model.Difficulty
import com.example.ironwake.model.MathTopic
import com.example.ironwake.service.AlarmService
import com.example.ironwake.ui.screens.RingingScreen
import com.example.ironwake.ui.theme.IronWakeTheme

class AlarmRingingActivity : ComponentActivity() {
    private var missionCompleted = false
    private var isTestMode = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        isTestMode = intent.getBooleanExtra("IS_TEST_MODE", AlarmService.isTestMode)

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O_MR1) {
            setShowWhenLocked(true)
            setTurnScreenOn(true)
            (getSystemService(Context.KEYGUARD_SERVICE) as KeyguardManager).requestDismissKeyguard(this, null)
        } else {
            @Suppress("DEPRECATION")
            window.addFlags(
                WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED or
                WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON or
                WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON
            )
        }

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (isTestMode || missionCompleted) {
                    exitAlarmCompletely()
                }
            }
        })

        val prefs = getSharedPreferences("IronWakePrefs", Context.MODE_PRIVATE)
        val motivationText = prefs.getString("motivation_text", "WAKE UP YOU LAZY KIDS!") ?: "WAKE UP YOU LAZY KIDS!"
        val difficulty = Difficulty.valueOf(prefs.getString("difficulty", Difficulty.NORMAL.name) ?: Difficulty.NORMAL.name)
        val enabledTopics = prefs.getStringSet("enabled_topics", null)
            ?.mapNotNull { runCatching { MathTopic.valueOf(it) }.getOrNull() }
            ?.toSet() ?: MathTopic.entries.toSet()

        setContent {
            IronWakeTheme {
                RingingScreen(
                    motivationText = motivationText,
                    enabledTopics = enabledTopics,
                    difficulty = difficulty,
                    isTestMode = isTestMode,
                    onExitTestMode = { exitAlarmCompletely() },
                    onEnterStudyMode = {
                        val intent = Intent(this, AlarmService::class.java).apply {
                            action = AlarmService.ACTION_PAUSE_FOR_STUDY
                        }
                        startService(intent)
                    },
                    onTimeoutBackToAlarm = {
                        val intent = Intent(this, AlarmService::class.java).apply {
                            action = AlarmService.ACTION_RESUME_ALARM
                        }
                        startService(intent)
                    },
                    onAllMissionsCompleted = {
                        missionCompleted = true
                        val celebrateIntent = Intent(this, AlarmService::class.java).apply {
                            action = AlarmService.ACTION_CELEBRATE
                        }
                        startService(celebrateIntent)
                    },
                    onFinishCelebration = { exitAlarmCompletely() }
                )
            }
        }
    }

    private fun exitAlarmCompletely() {
        missionCompleted = true
        stopService(Intent(this, AlarmService::class.java))
        finish()
    }

    override fun onUserLeaveHint() {
        super.onUserLeaveHint()
        if (!missionCompleted && !isTestMode && AlarmService.isAlarmRinging) {
            startActivity(Intent(this, AlarmRingingActivity::class.java).apply {
                addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_REORDER_TO_FRONT)
            })
        }
    }
}
""",

    "app/src/main/java/com/example/ironwake/ui/screens/RingingScreen.kt": r"""package com.example.ironwake.ui.screens

import androidx.compose.foundation.*
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.ironwake.R
import com.example.ironwake.model.Difficulty
import com.example.ironwake.model.MathTopic
import com.example.ironwake.ui.theme.*
import com.example.ironwake.util.MathGenerator
import kotlinx.coroutines.delay
import kotlin.random.Random

@Composable
fun RingingScreen(
    motivationText: String,
    enabledTopics: Set<MathTopic>,
    difficulty: Difficulty,
    isTestMode: Boolean,
    onExitTestMode: () -> Unit,
    onEnterStudyMode: () -> Unit,
    onTimeoutBackToAlarm: () -> Unit,
    onAllMissionsCompleted: () -> Unit,
    onFinishCelebration: () -> Unit
) {
    var currentStep by remember { mutableIntStateOf(1) }
    var currentProblem by remember { mutableStateOf(MathGenerator.generateProblem(enabledTopics, difficulty)) }
    var userAnswer by remember { mutableStateOf("") }
    var errorMessage by remember { mutableStateOf<String?>(null) }

    var isStudying by remember { mutableStateOf(false) }
    var hasTimedOutBefore by remember { mutableStateOf(false) }
    var timeLeft by remember { mutableIntStateOf(difficulty.durationSeconds) }
    var showTutorDialog by remember { mutableStateOf(false) }
    var isCelebrating by remember { mutableStateOf(false) }

    LaunchedEffect(isStudying, currentStep, isCelebrating) {
        if (isStudying && !isCelebrating) {
            timeLeft = difficulty.durationSeconds
            while (timeLeft > 0) {
                delay(1000L)
                timeLeft--
            }
            showTutorDialog = false
            isStudying = false
            hasTimedOutBefore = true
            onTimeoutBackToAlarm()
        }
    }

    fun startOrResumeStudy() {
        errorMessage = null
        isStudying = true
        onEnterStudyMode()
    }

    fun verifyAnswer() {
        val parsed = userAnswer.trim().toIntOrNull()
        if (parsed == null) {
            errorMessage = "Masukkan angka bulat!"
            return
        }
        if (parsed == currentProblem.correctAnswer) {
            errorMessage = null
            userAnswer = ""
            showTutorDialog = false
            if (currentStep >= 5) {
                isCelebrating = true
                onAllMissionsCompleted()
            } else {
                currentStep++
                currentProblem = MathGenerator.generateProblem(enabledTopics, difficulty)
                timeLeft = difficulty.durationSeconds
            }
        } else {
            errorMessage = "SALAH! Coba hitung lagi atau tanya pengajar!"
            userAnswer = ""
        }
    }

    Box(modifier = Modifier.fillMaxSize()) {
        Image(
            painter = painterResource(id = R.drawable.bg_boxer_punch),
            contentDescription = null,
            contentScale = ContentScale.Crop,
            modifier = Modifier.fillMaxSize()
        )
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(
                    Brush.verticalGradient(
                        when {
                            isCelebrating -> listOf(Color(0xD90A1F12), Color(0xCC0D0D0D), Color(0xE60A1F12))
                            isStudying -> listOf(Color(0xEB0B1220), Color(0xE0101828), Color(0xF2090D16))
                            else -> listOf(Color.Black.copy(0.78f), Color.Black.copy(0.55f), Color.Black.copy(0.88f))
                        }
                    )
                )
        )

        when {
            isCelebrating -> {
                val confettiPoints = remember {
                    List(45) {
                        Triple(
                            Random.nextFloat(),
                            Random.nextFloat(),
                            listOf(IronGold, IronEmerald, Color.White, IronRed).random()
                        )
                    }
                }
                Canvas(modifier = Modifier.fillMaxSize()) {
                    confettiPoints.forEach { (rx, ry, col) ->
                        drawCircle(
                            color = col.copy(alpha = 0.75f),
                            radius = 10f,
                            center = Offset(rx * size.width, ry * size.height)
                        )
                    }
                }

                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(24.dp),
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.Center
                ) {
                    Icon(
                        imageVector = Icons.Default.EmojiEvents,
                        contentDescription = null,
                        tint = IronGold,
                        modifier = Modifier.size(96.dp)
                    )
                    Spacer(Modifier.height(16.dp))
                    Text(
                        text = "SURPRISE! YOU DID IT!",
                        color = IronGold,
                        fontSize = 32.sp,
                        fontWeight = FontWeight.Black,
                        textAlign = TextAlign.Center
                    )
                    Spacer(Modifier.height(10.dp))
                    Text(
                        text = "GREAT JOB, CHAMPION!",
                        color = IronEmerald,
                        fontSize = 20.sp,
                        fontWeight = FontWeight.ExtraBold,
                        textAlign = TextAlign.Center
                    )
                    Spacer(Modifier.height(14.dp))
                    Text(
                        text = "Semua 5 soal berhasil ditaklukkan bersama pendamping belajarmu!",
                        color = Color.White,
                        fontSize = 15.sp,
                        textAlign = TextAlign.Center,
                        lineHeight = 22.sp
                    )
                    Spacer(Modifier.height(32.dp))
                    Button(
                        onClick = onFinishCelebration,
                        colors = ButtonDefaults.buttonColors(containerColor = IronEmerald),
                        shape = RoundedCornerShape(14.dp),
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(56.dp)
                    ) {
                        Text(
                            text = "SELESAI & KEMBALI KE BERANDA",
                            color = Color.Black,
                            fontWeight = FontWeight.Black,
                            fontSize = 16.sp
                        )
                    }
                }
            }

            isStudying -> {
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(20.dp),
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.SpaceBetween
                ) {
                    Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.fillMaxWidth()) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Surface(
                                color = IronCyan.copy(alpha = 0.15f),
                                shape = RoundedCornerShape(50),
                                modifier = Modifier.border(1.dp, IronCyan, RoundedCornerShape(50))
                            ) {
                                Text(
                                    text = "SOAL $currentStep / 5",
                                    color = IronCyan,
                                    fontWeight = FontWeight.Black,
                                    fontSize = 13.sp,
                                    modifier = Modifier.padding(horizontal = 14.dp, vertical = 6.dp)
                                )
                            }

                            val timerColor = if (timeLeft <= 15) IronCrimson else IronGold
                            Surface(
                                color = timerColor.copy(alpha = 0.15f),
                                shape = RoundedCornerShape(50),
                                modifier = Modifier.border(1.5.dp, timerColor, RoundedCornerShape(50))
                            ) {
                                Row(
                                    verticalAlignment = Alignment.CenterVertically,
                                    modifier = Modifier.padding(horizontal = 14.dp, vertical = 6.dp)
                                ) {
                                    Icon(Icons.Default.Timer, contentDescription = null, tint = timerColor, modifier = Modifier.size(16.dp))
                                    Spacer(Modifier.width(4.dp))
                                    Text(
                                        text = "${timeLeft}s",
                                        color = timerColor,
                                        fontWeight = FontWeight.Black,
                                        fontSize = 15.sp
                                    )
                                }
                            }

                            if (isTestMode) {
                                IconButton(onClick = onExitTestMode) {
                                    Icon(Icons.Default.Close, contentDescription = "Keluar Uji Coba", tint = IronGold)
                                }
                            }
                        }

                        Spacer(Modifier.height(8.dp))
                        LinearProgressIndicator(
                            progress = { timeLeft.toFloat() / difficulty.durationSeconds.toFloat() },
                            color = if (timeLeft <= 15) IronCrimson else IronCyan,
                            trackColor = Color.White.copy(alpha = 0.15f),
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(6.dp)
                        )
                    }

                    Card(
                        colors = CardDefaults.cardColors(containerColor = Color(0xF0131B2E)),
                        shape = RoundedCornerShape(18.dp),
                        modifier = Modifier
                            .fillMaxWidth()
                            .border(1.5.dp, IronCyan, RoundedCornerShape(18.dp))
                    ) {
                        Column(
                            modifier = Modifier.padding(20.dp),
                            horizontalAlignment = Alignment.CenterHorizontally
                        ) {
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text(
                                    text = currentProblem.topic.displayName.uppercase(),
                                    color = IronGold,
                                    fontSize = 11.sp,
                                    fontWeight = FontWeight.Bold,
                                    modifier = Modifier.weight(1f)
                                )

                                FilledTonalButton(
                                    onClick = { showTutorDialog = true },
                                    colors = ButtonDefaults.filledTonalButtonColors(
                                        containerColor = IronCyan,
                                        contentColor = Color.Black
                                    ),
                                    contentPadding = PaddingValues(horizontal = 12.dp, vertical = 6.dp),
                                    shape = RoundedCornerShape(50)
                                ) {
                                    Icon(Icons.Default.School, contentDescription = "Pengajar", modifier = Modifier.size(18.dp))
                                    Spacer(Modifier.width(6.dp))
                                    Text("Tanya Pengajar", fontWeight = FontWeight.Black, fontSize = 12.sp)
                                }
                            }

                            Spacer(Modifier.height(14.dp))
                            Text(
                                text = currentProblem.question,
                                color = Color.White,
                                fontSize = 19.sp,
                                fontWeight = FontWeight.Bold,
                                textAlign = TextAlign.Center,
                                lineHeight = 27.sp
                            )
                            Spacer(Modifier.height(16.dp))

                            OutlinedTextField(
                                value = userAnswer,
                                onValueChange = { userAnswer = it },
                                label = { Text("Jawaban (Angka Bulat)") },
                                singleLine = true,
                                keyboardOptions = KeyboardOptions(
                                    keyboardType = KeyboardType.Number,
                                    imeAction = ImeAction.Done
                                ),
                                keyboardActions = KeyboardActions(onDone = { verifyAnswer() }),
                                colors = OutlinedTextFieldDefaults.colors(
                                    focusedBorderColor = IronCyan,
                                    unfocusedBorderColor = IronGold,
                                    focusedTextColor = Color.White,
                                    unfocusedTextColor = Color.White,
                                    focusedLabelColor = IronCyan
                                ),
                                modifier = Modifier.fillMaxWidth()
                            )

                            if (errorMessage != null) {
                                Spacer(Modifier.height(8.dp))
                                Text(
                                    text = errorMessage!!,
                                    color = IronCrimson,
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 13.sp,
                                    textAlign = TextAlign.Center
                                )
                            }

                            Spacer(Modifier.height(16.dp))
                            Button(
                                onClick = { verifyAnswer() },
                                colors = ButtonDefaults.buttonColors(containerColor = IronEmerald),
                                shape = RoundedCornerShape(12.dp),
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .height(52.dp)
                            ) {
                                Text(
                                    text = if (currentStep < 5) "KIRIM JAWABAN ($currentStep/5)" else "SELESAIKAN MISI!",
                                    color = Color.Black,
                                    fontWeight = FontWeight.Black,
                                    fontSize = 16.sp
                                )
                            }
                        }
                    }

                    Text(
                        text = "Suara alarm dijeda selama pengerjaan. Selesaikan sebelum waktu habis!",
                        color = IronCyan.copy(alpha = 0.85f),
                        fontSize = 12.sp,
                        fontWeight = FontWeight.SemiBold,
                        textAlign = TextAlign.Center
                    )
                }
            }

            else -> {
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(24.dp),
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.SpaceBetween
                ) {
                    Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.fillMaxWidth()) {
                        if (isTestMode) {
                            Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.End) {
                                FilledTonalButton(
                                    onClick = onExitTestMode,
                                    colors = ButtonDefaults.filledTonalButtonColors(
                                        containerColor = IronGold,
                                        contentColor = Color.Black
                                    ),
                                    contentPadding = PaddingValues(horizontal = 14.dp, vertical = 6.dp)
                                ) {
                                    Icon(Icons.Default.Close, contentDescription = null, modifier = Modifier.size(18.dp))
                                    Spacer(Modifier.width(4.dp))
                                    Text("KELUAR UJI COBA", fontWeight = FontWeight.Black, fontSize = 12.sp)
                                }
                            }
                        }

                        Spacer(Modifier.height(16.dp))
                        Surface(
                            color = IronRed,
                            shape = CircleShape,
                            modifier = Modifier
                                .size(84.dp)
                                .border(2.dp, IronGold, CircleShape)
                        ) {
                            Box(contentAlignment = Alignment.Center) {
                                Icon(Icons.Default.NotificationsActive, contentDescription = null, tint = IronGold, modifier = Modifier.size(44.dp))
                            }
                        }
                        Spacer(Modifier.height(20.dp))
                        Text(
                            text = motivationText.uppercase(),
                            color = IronGold,
                            fontSize = 32.sp,
                            fontWeight = FontWeight.Black,
                            textAlign = TextAlign.Center,
                            lineHeight = 38.sp
                        )
                        Spacer(Modifier.height(12.dp))
                        Text(
                            text = if (hasTimedOutBefore)
                                "WAKTU PENGERJAAN HABIS! Alarm berbunyi kembali.\nTekan tombol di bawah untuk melanjutkan soal ke-$currentStep."
                            else
                                "Alarm aktif! Masuk ke ruang belajar untuk menjeda suara alarm dan menyelesaikan 5 soal misi.",
                            color = Color.White,
                            fontSize = 15.sp,
                            textAlign = TextAlign.Center,
                            lineHeight = 22.sp
                        )
                    }

                    Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.fillMaxWidth()) {
                        Surface(
                            color = IronSurface.copy(alpha = 0.9f),
                            shape = RoundedCornerShape(12.dp),
                            modifier = Modifier.border(1.dp, IronGold, RoundedCornerShape(12.dp))
                        ) {
                            Text(
                                text = "Progres: Soal $currentStep dari 5 • Durasi ${difficulty.durationSeconds} detik/soal",
                                color = IronGold,
                                fontWeight = FontWeight.Bold,
                                fontSize = 13.sp,
                                modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp)
                            )
                        }
                        Spacer(Modifier.height(16.dp))
                        Button(
                            onClick = { startOrResumeStudy() },
                            colors = ButtonDefaults.buttonColors(containerColor = IronRed),
                            shape = RoundedCornerShape(16.dp),
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(64.dp)
                                .border(2.dp, IronGold, RoundedCornerShape(16.dp))
                        ) {
                            Icon(Icons.Default.PlayArrow, contentDescription = null, tint = IronGold, modifier = Modifier.size(28.dp))
                            Spacer(Modifier.width(8.dp))
                            Text(
                                text = if (hasTimedOutBefore) "LANJUTKAN SOAL ($currentStep/5)" else "MULAI KERJAKAN SOAL",
                                color = Color.White,
                                fontWeight = FontWeight.Black,
                                fontSize = 18.sp
                            )
                        }
                    }

                    Text(
                        text = "IRONWAKE DISCIPLINE SYSTEM",
                        color = Color.White.copy(alpha = 0.6f),
                        fontSize = 11.sp,
                        fontWeight = FontWeight.Bold
                    )
                }
            }
        }

        if (showTutorDialog) {
            AlertDialog(
                onDismissRequest = { showTutorDialog = false },
                containerColor = Color(0xFF141E30),
                icon = {
                    Icon(Icons.Default.School, contentDescription = null, tint = IronCyan, modifier = Modifier.size(36.dp))
                },
                title = {
                    Text(
                        text = "Langkah Pengerjaan Pengajar",
                        color = IronCyan,
                        fontWeight = FontWeight.Black,
                        fontSize = 18.sp
                    )
                },
                text = {
                    Column(modifier = Modifier.verticalScroll(rememberScrollState())) {
                        Text(
                            text = "Ikuti tahapan berikut untuk menemukan jawabannya:",
                            color = IronGold,
                            fontSize = 13.sp,
                            fontWeight = FontWeight.Bold
                        )
                        Spacer(Modifier.height(10.dp))
                        currentProblem.tutorSteps.forEachIndexed { index, stepText ->
                            Row(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .padding(vertical = 4.dp),
                                verticalAlignment = Alignment.Top
                            ) {
                                Surface(
                                    color = IronCyan,
                                    shape = CircleShape,
                                    modifier = Modifier.size(22.dp)
                                ) {
                                    Box(contentAlignment = Alignment.Center) {
                                        Text(
                                            text = "${index + 1}",
                                            color = Color.Black,
                                            fontWeight = FontWeight.Black,
                                            fontSize = 12.sp
                                        )
                                    }
                                }
                                Spacer(Modifier.width(10.dp))
                                Text(
                                    text = stepText,
                                    color = Color.White,
                                    fontSize = 14.sp,
                                    lineHeight = 20.sp,
                                    modifier = Modifier.weight(1f)
                                )
                            }
                        }
                    }
                },
                confirmButton = {
                    Button(
                        onClick = { showTutorDialog = false },
                        colors = ButtonDefaults.buttonColors(containerColor = IronCyan)
                    ) {
                        Text("PAHAM, LANJUT HITUNG", color = Color.Black, fontWeight = FontWeight.Black)
                    }
                }
            )
        }
    }
}
""",

    "app/src/main/java/com/example/ironwake/ui/screens/HomeScreen.kt": r"""package com.example.ironwake.ui.screens

import android.app.TimePickerDialog
import android.content.Context
import android.content.Intent
import android.os.Build
import android.widget.Toast
import androidx.compose.foundation.*
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.ironwake.model.Difficulty
import com.example.ironwake.model.MathTopic
import com.example.ironwake.service.AlarmService
import com.example.ironwake.ui.theme.*
import com.example.ironwake.util.AlarmScheduler
import java.util.Locale

@Composable
fun HomeScreen() {
    val context = LocalContext.current
    val prefs = remember { context.getSharedPreferences("IronWakePrefs", Context.MODE_PRIVATE) }
    var hour by remember { mutableIntStateOf(prefs.getInt("alarm_hour", 5)) }
    var minute by remember { mutableIntStateOf(prefs.getInt("alarm_minute", 0)) }
    var isAlarmActive by remember { mutableStateOf(prefs.getBoolean("alarm_active", false)) }
    var motivationText by remember { mutableStateOf(prefs.getString("motivation_text", "WAKE UP YOU LAZY KIDS!") ?: "WAKE UP YOU LAZY KIDS!") }
    var difficulty by remember { mutableStateOf(Difficulty.valueOf(prefs.getString("difficulty", Difficulty.NORMAL.name) ?: Difficulty.NORMAL.name)) }
    var enabledTopics by remember {
        val savedSet = prefs.getStringSet("enabled_topics", null)
        mutableStateOf(savedSet?.mapNotNull { runCatching { MathTopic.valueOf(it) }.getOrNull() }?.toSet() ?: MathTopic.entries.toSet())
    }
    var showMissionDialog by remember { mutableStateOf(false) }

    val timePickerDialog = TimePickerDialog(context, { _, h, m ->
        hour = h; minute = m
        prefs.edit().putInt("alarm_hour", h).putInt("alarm_minute", m).apply()
        if (isAlarmActive) AlarmScheduler.scheduleAlarm(context, h, m)
    }, hour, minute, true)

    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(IronBlack)
            .padding(20.dp)
            .verticalScroll(rememberScrollState()),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.padding(top = 12.dp, bottom = 24.dp)) {
            Icon(Icons.Default.FitnessCenter, null, tint = IronGold, modifier = Modifier.size(32.dp))
            Spacer(Modifier.width(10.dp))
            Text("IRONWAKE ALARM", color = Color.White, fontSize = 24.sp, fontWeight = FontWeight.Black)
        }

        Card(
            colors = CardDefaults.cardColors(containerColor = IronSurface),
            shape = RoundedCornerShape(20.dp),
            modifier = Modifier
                .fillMaxWidth()
                .border(2.dp, if (isAlarmActive) IronGold else IronRed, RoundedCornerShape(20.dp))
        ) {
            Column(modifier = Modifier.padding(24.dp), horizontalAlignment = Alignment.CenterHorizontally) {
                Text("JADWAL BANGUN DISIPLIN", color = IronGold, fontSize = 12.sp, fontWeight = FontWeight.Bold)
                Spacer(Modifier.height(8.dp))
                Text(
                    text = String.format(Locale.getDefault(), "%02d:%02d", hour, minute),
                    color = Color.White,
                    fontSize = 64.sp,
                    fontWeight = FontWeight.Black,
                    modifier = Modifier.clickable { timePickerDialog.show() }
                )
                Text("Ketuk jam untuk mengubah waktu", color = Color.Gray, fontSize = 12.sp)
                Spacer(Modifier.height(20.dp))
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Icon(Icons.Default.Alarm, null, tint = IronRed)
                        Spacer(Modifier.width(8.dp))
                        Text(if (isAlarmActive) "ALARM AKTIF" else "ALARM NONAKTIF", color = Color.White, fontWeight = FontWeight.Bold)
                    }
                    Switch(
                        checked = isAlarmActive,
                        onCheckedChange = { checked ->
                            isAlarmActive = checked
                            prefs.edit().putBoolean("alarm_active", checked).apply()
                            if (checked) AlarmScheduler.scheduleAlarm(context, hour, minute) else AlarmScheduler.cancelAlarm(context)
                        },
                        colors = SwitchDefaults.colors(checkedThumbColor = IronGold, checkedTrackColor = IronRed)
                    )
                }
            }
        }

        Spacer(Modifier.height(20.dp))

        Button(
            onClick = { showMissionDialog = true },
            colors = ButtonDefaults.buttonColors(containerColor = IronGold),
            shape = RoundedCornerShape(12.dp),
            modifier = Modifier
                .fillMaxWidth()
                .height(54.dp)
        ) {
            Icon(Icons.Default.Tune, null, tint = Color.Black)
            Spacer(Modifier.width(8.dp))
            Text("MODIFIKASI MISI & DURASI", color = Color.Black, fontWeight = FontWeight.Black, fontSize = 16.sp)
        }

        Spacer(Modifier.height(12.dp))

        OutlinedButton(
            onClick = {
                val serviceIntent = Intent(context, AlarmService::class.java).apply {
                    putExtra("IS_TEST_MODE", true)
                }
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) context.startForegroundService(serviceIntent)
                else context.startService(serviceIntent)
            },
            shape = RoundedCornerShape(12.dp),
            modifier = Modifier
                .fillMaxWidth()
                .height(50.dp)
        ) {
            Icon(Icons.Default.PlayArrow, null, tint = IronRed)
            Spacer(Modifier.width(6.dp))
            Text("UJI COBA ALARM SEKARANG", color = IronRed, fontWeight = FontWeight.Bold)
        }
    }

    if (showMissionDialog) {
        AlertDialog(
            onDismissRequest = { showMissionDialog = false },
            containerColor = IronSurface,
            title = { Text("MODIFIKASI MISI & DURASI", color = IronGold, fontWeight = FontWeight.Black) },
            text = {
                Column(modifier = Modifier.verticalScroll(rememberScrollState())) {
                    Text("Teks Teriakan Alarm:", color = Color.White, fontWeight = FontWeight.Bold)
                    OutlinedTextField(value = motivationText, onValueChange = { motivationText = it }, singleLine = true, modifier = Modifier.fillMaxWidth())
                    Spacer(Modifier.height(12.dp))
                    Text("Tingkat Kesulitan & Durasi Soal:", color = Color.White, fontWeight = FontWeight.Bold)
                    Column(verticalArrangement = Arrangement.spacedBy(4.dp)) {
                        Difficulty.entries.forEach { diff ->
                            FilterChip(
                                selected = difficulty == diff,
                                onClick = { difficulty = diff },
                                label = { Text(diff.label) }
                            )
                        }
                    }
                    Spacer(Modifier.height(12.dp))
                    Text("Pilih Paket Materi & DLC:", color = Color.White, fontWeight = FontWeight.Bold)
                    MathTopic.entries.forEach { topic ->
                        val isChecked = enabledTopics.contains(topic)
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            modifier = Modifier
                                .fillMaxWidth()
                                .clickable {
                                    if (isChecked && enabledTopics.size > 1) enabledTopics = enabledTopics - topic else enabledTopics = enabledTopics + topic
                                }
                        ) {
                            Checkbox(
                                checked = isChecked,
                                onCheckedChange = { checked ->
                                    if (!checked && enabledTopics.size <= 1) Toast.makeText(context, "Minimal pilih 1!", Toast.LENGTH_SHORT).show()
                                    else enabledTopics = if (checked) enabledTopics + topic else enabledTopics - topic
                                },
                                colors = CheckboxDefaults.colors(checkedColor = IronRed)
                            )
                            Text(
                                text = topic.displayName,
                                color = if (topic == MathTopic.NOPJEK_DLC) IronCyan else Color.White,
                                fontWeight = if (topic == MathTopic.NOPJEK_DLC) FontWeight.Bold else FontWeight.Normal,
                                fontSize = 14.sp
                            )
                        }
                    }
                }
            },
            confirmButton = {
                Button(
                    onClick = {
                        prefs.edit()
                            .putString("motivation_text", motivationText.ifBlank { "WAKE UP YOU LAZY KIDS!" })
                            .putString("difficulty", difficulty.name)
                            .putStringSet("enabled_topics", enabledTopics.map { it.name }.toSet())
                            .apply()
                        showMissionDialog = false
                    },
                    colors = ButtonDefaults.buttonColors(containerColor = IronRed)
                ) { Text("SIMPAN", color = Color.White) }
            }
        )
    }
}
""",

    "app/src/main/java/com/example/ironwake/MainActivity.kt": r"""package com.example.ironwake

import android.Manifest
import android.app.AlarmManager
import android.app.admin.DevicePolicyManager
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.provider.Settings
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.result.contract.ActivityResultContracts
import androidx.core.content.ContextCompat
import com.example.ironwake.receiver.IronWakeAdminReceiver
import com.example.ironwake.ui.screens.HomeScreen
import com.example.ironwake.ui.theme.IronWakeTheme

class MainActivity : ComponentActivity() {
    private val requestNotificationPermission = registerForActivityResult(ActivityResultContracts.RequestPermission()) { _ -> }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU && ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) {
            requestNotificationPermission.launch(Manifest.permission.POST_NOTIFICATIONS)
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            val am = getSystemService(Context.ALARM_SERVICE) as AlarmManager
            if (!am.canScheduleExactAlarms()) startActivity(Intent(Settings.ACTION_REQUEST_SCHEDULE_EXACT_ALARM, Uri.parse("package:$packageName")))
        }
        if (!Settings.canDrawOverlays(this)) {
            startActivity(Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION, Uri.parse("package:$packageName")))
        }
        val dpm = getSystemService(Context.DEVICE_POLICY_SERVICE) as DevicePolicyManager
        val adminComponent = ComponentName(this, IronWakeAdminReceiver::class.java)
        if (!dpm.isAdminActive(adminComponent)) {
            startActivity(Intent(DevicePolicyManager.ACTION_ADD_DEVICE_ADMIN).apply {
                putExtra(DevicePolicyManager.EXTRA_DEVICE_ADMIN, adminComponent)
                putExtra(DevicePolicyManager.EXTRA_ADD_EXPLANATION, "Kunci Force Stop & Uninstall saat alarm berbunyi!")
            })
        }
        setContent { IronWakeTheme { HomeScreen() } }
    }
}
"""
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
print("Semua file proyek IronWake v5.1 + Nopjek DLC berhasil dibuat!")
