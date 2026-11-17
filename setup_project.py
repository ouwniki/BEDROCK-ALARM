import os

files = {
    "settings.gradle.kts": """pluginManagement {
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

    "build.gradle.kts": """plugins {
    id("com.android.application") version "8.2.2" apply false
    id("org.jetbrains.kotlin.android") version "1.9.22" apply false
}
""",

    "gradle.properties": """org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
kotlin.code.style=official
android.nonTransitiveRClass=true
""",

    "app/build.gradle.kts": """plugins {
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
        versionCode = 2
        versionName = "2.0"
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

    "app/src/main/res/values/strings.xml": """<resources>
    <string name="app_name">IronWake Alarm</string>
</resources>
""",

    "app/src/main/res/xml/device_admin_policies.xml": """<?xml version="1.0" encoding="utf-8"?>
<device-admin xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-policies>
        <force-lock />
    </uses-policies>
</device-admin>
""",

    "app/src/main/res/drawable/ic_launcher_background.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <path android:fillColor="#0D0D10" android:pathData="M0,0h108v108h-108z" />
    <path android:fillColor="#26FFD700" android:pathData="M54,54m-42,0a42,42 0,1 1,84 0a42,42 0,1 1,-84 0" />
    <path android:strokeColor="#D32F2F" android:strokeWidth="3" android:pathData="M54,54m-44,0a44,44 0,1 1,88 0a44,44 0,1 1,-88 0" />
</vector>
""",

    "app/src/main/res/drawable/ic_launcher_foreground.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android"
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

    "app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml": """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_launcher_foreground" />
</adaptive-icon>
""",

    "app/src/main/res/mipmap-anydpi-v26/ic_launcher_round.xml": """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_launcher_foreground" />
</adaptive-icon>
""",

    "app/src/main/res/drawable/bg_boxer_punch.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android"
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

    "app/src/main/AndroidManifest.xml": """<?xml version="1.0" encoding="utf-8"?>
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

    "app/src/main/java/com/example/ironwake/ui/theme/Theme.kt": """package com.example.ironwake.ui.theme

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

    "app/src/main/java/com/example/ironwake/model/MathProblem.kt": """package com.example.ironwake.model

enum class MathTopic(val displayName: String) {
    QUADRATIC("Persamaan Kuadrat & Akar"),
    LOG_EXP("Logaritma & Eksponen"),
    CALCULUS("Turunan & Integral Dasar"),
    SEQUENCE("Barisan & Deret (Aritmatika/Geometri)"),
    TRIG_MATRIX("Trigonometri & Matriks 2x2")
}

enum class Difficulty(val label: String) {
    NORMAL("Standar SMA"),
    HARD("Intensif UTBK")
}

data class MathProblem(
    val topic: MathTopic,
    val question: String,
    val correctAnswer: Int,
    val hint: String
)
""",

    "app/src/main/java/com/example/ironwake/util/MathGenerator.kt": """package com.example.ironwake.util

import com.example.ironwake.model.Difficulty
import com.example.ironwake.model.MathProblem
import com.example.ironwake.model.MathTopic
import kotlin.math.pow
import kotlin.random.Random

object MathGenerator {
    fun generateProblem(enabledTopics: Set<MathTopic>, difficulty: Difficulty): MathProblem {
        val pool = if (enabledTopics.isEmpty()) MathTopic.entries else enabledTopics.toList()
        return when (pool.random()) {
            MathTopic.QUADRATIC -> generateQuadratic(difficulty)
            MathTopic.LOG_EXP -> generateLogExp(difficulty)
            MathTopic.CALCULUS -> generateCalculus(difficulty)
            MathTopic.SEQUENCE -> generateSequence(difficulty)
            MathTopic.TRIG_MATRIX -> generateTrigOrMatrix(difficulty)
        }
    }

    private fun generateQuadratic(difficulty: Difficulty): MathProblem {
        val x1 = Random.nextInt(-6, 8).let { if (it == 0) 2 else it }
        val x2 = Random.nextInt(-5, 9).let { if (it == 0) 3 else it }
        val b = -(x1 + x2)
        val c = x1 * x2
        val bStr = if (b >= 0) "+ ${b}x" else "- ${-b}x"
        val cStr = if (c >= 0) "+ $c" else "- ${-c}"

        return if (difficulty == Difficulty.NORMAL) {
            MathProblem(MathTopic.QUADRATIC, "Jika x₁ dan x₂ akar dari:\\nx² $bStr $cStr = 0\\nTentukan nilai (x₁ + x₂)!", x1 + x2, "x₁ + x₂ = -b/a")
        } else {
            MathProblem(MathTopic.QUADRATIC, "Akar persamaan x² $bStr $cStr = 0 adalah x₁ dan x₂.\\nHitung nilai x₁² + x₂²!", (x1 * x1) + (x2 * x2), "(x₁ + x₂)² - 2(x₁·x₂)")
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
            MathProblem(MathTopic.LOG_EXP, "Hitung nilai:\\n^${base1}log($val1) + ^${base2}log($val2) = ...", exp1 + exp2, "ᵃlog(aⁿ) = n")
        } else {
            val base = listOf(2, 3, 5).random()
            val x = Random.nextInt(2, 7)
            val k = Random.nextInt(1, 5)
            val expRes = (2 * x) - k
            val rhs = base.toDouble().pow(expRes).toInt()
            MathProblem(MathTopic.LOG_EXP, "Tentukan nilai x:\\n$base^(2x - $k) = $rhs", x, "2x - $k = $expRes")
        }
    }

    private fun generateCalculus(difficulty: Difficulty): MathProblem {
        return if (Random.nextBoolean()) {
            val a = Random.nextInt(1, 4)
            val b = Random.nextInt(2, 7)
            val c = Random.nextInt(1, 10)
            val k = if (difficulty == Difficulty.NORMAL) Random.nextInt(1, 3) else Random.nextInt(2, 5)
            MathProblem(MathTopic.CALCULUS, "Diketahui f(x) = ${a}x³ + ${b}x² + ${c}x.\\nTentukan f'($k)!", (3 * a * k * k) + (2 * b * k) + c, "f'(x) = ${3 * a}x² + ${2 * b}x + $c")
        } else {
            val a = Random.nextInt(1, 3)
            val c = Random.nextInt(1, 5)
            val upper = Random.nextInt(2, 4)
            MathProblem(MathTopic.CALCULUS, "Hitung integral tentu:\\n∫ (0 sampai $upper) (${3 * a}x² + ${2 * c}x) dx", (a * upper * upper * upper) + (c * upper * upper), "[${a}x³ + ${c}x²] dari 0 ke $upper")
        }
    }

    private fun generateSequence(difficulty: Difficulty): MathProblem {
        return if (Random.nextBoolean()) {
            val a = Random.nextInt(3, 15)
            val b = Random.nextInt(3, 9)
            val n = if (difficulty == Difficulty.NORMAL) Random.nextInt(8, 15) else Random.nextInt(15, 25)
            MathProblem(MathTopic.SEQUENCE, "Barisan aritmatika a = $a dan b = $b.\\nTentukan suku ke-$n (U$n)!", a + (n - 1) * b, "Un = a + (n - 1)b")
        } else {
            val a = Random.nextInt(2, 6)
            val r = listOf(2, 3).random()
            val n = Random.nextInt(4, 6)
            MathProblem(MathTopic.SEQUENCE, "Barisan geometri a = $a dan r = $r.\\nTentukan suku ke-$n (U$n)!", a * r.toDouble().pow(n - 1).toInt(), "Un = a · r^(n - 1)")
        }
    }

    private fun generateTrigOrMatrix(difficulty: Difficulty): MathProblem {
        return if (Random.nextBoolean()) {
            val a = Random.nextInt(2, 9)
            val b = Random.nextInt(1, 7)
            val c = Random.nextInt(1, 7)
            val d = Random.nextInt(2, 9)
            MathProblem(MathTopic.TRIG_MATRIX, "Matriks A = [ [$a, $b], [$c, $d] ].\\nTentukan det(A)!", (a * d) - (b * c), "det(A) = ad - bc")
        } else {
            val variants = listOf(
                Triple("Hitung: 4·sin(30°) + 6·cos(60°)!", 5, "sin(30°)=1/2, cos(60°)=1/2"),
                Triple("Hitung: 3·tan(45°) + 2·sin(90°)!", 5, "tan(45°)=1, sin(90°)=1"),
                Triple("Hitung: 8·cos(60°) + 5·tan(45°) - cos(0°)!", 8, "cos(60°)=1/2, tan(45°)=1, cos(0°)=1")
            )
            val chosen = variants.random()
            MathProblem(MathTopic.TRIG_MATRIX, chosen.first, chosen.second, chosen.third)
        }
    }
}
""",

    "app/src/main/java/com/example/ironwake/util/AlarmScheduler.kt": """package com.example.ironwake.util

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

    "app/src/main/java/com/example/ironwake/receiver/AlarmReceiver.kt": """package com.example.ironwake.receiver

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

    "app/src/main/java/com/example/ironwake/receiver/IronWakeAdminReceiver.kt": """package com.example.ironwake.receiver

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
            return "CURANG TERDETEKSI! Selesaikan 5 soal matematika SMA!"
        }
        return "Menonaktifkan proteksi ini membuka kunci Force Stop & Uninstall."
    }
}
""",

    "app/src/main/java/com/example/ironwake/service/AlarmService.kt": """package com.example.ironwake.service

import android.app.*
import android.content.Context
import android.content.Intent
import android.media.AudioAttributes
import android.media.AudioManager
import android.media.MediaPlayer
import android.media.Ringtone
import android.media.RingtoneManager
import android.media.ToneGenerator
import android.os.*
import android.speech.tts.TextToSpeech
import androidx.core.app.NotificationCompat
import com.example.ironwake.AlarmRingingActivity
import java.util.Locale

class AlarmService : Service(), TextToSpeech.OnInitListener {
    private var mediaPlayer: MediaPlayer? = null
    private var ringtone: Ringtone? = null
    private var toneGenerator: ToneGenerator? = null
    private var tts: TextToSpeech? = null
    private var isTtsReady = false
    private lateinit var audioManager: AudioManager
    private var vibrator: Vibrator? = null
    private val handler = Handler(Looper.getMainLooper())

    companion object {
        const val CHANNEL_ID = "IRON_WAKE_ALARM_CHANNEL"
        const val NOTIFICATION_ID = 999
        const val ACTION_CELEBRATE = "com.example.ironwake.ACTION_CELEBRATE"
        var isAlarmRinging = false
        var isTestMode = false
        var isCelebrating = false
    }

    private val enforcementRunnable = object : Runnable {
        override fun run() {
            if (!isAlarmRinging || isCelebrating) return
            forceMaxAlarmVolume()
            runCatching { toneGenerator?.startTone(ToneGenerator.TONE_CDMA_EMERGENCY_RINGBACK, 450) }
            if (mediaPlayer == null && isTtsReady) speakMotivation()
            handler.postDelayed(this, 3200L)
        }
    }

    override fun onCreate() {
        super.onCreate()
        audioManager = getSystemService(Context.AUDIO_SERVICE) as AudioManager
        vibrator = getSystemService(Context.VIBRATOR_SERVICE) as Vibrator
        runCatching { toneGenerator = ToneGenerator(AudioManager.STREAM_ALARM, 95) }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(CHANNEL_ID, "IronWake Alarm", NotificationManager.IMPORTANCE_HIGH).apply {
                setBypassDnd(true)
            }
            getSystemService(NotificationManager::class.java).createNotificationChannel(channel)
        }
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        if (intent?.action == ACTION_CELEBRATE) {
            triggerCelebrationAudio()
            return START_NOT_STICKY
        }

        isTestMode = intent?.getBooleanExtra("IS_TEST_MODE", false) ?: false
        isAlarmRinging = true
        isCelebrating = false
        forceMaxAlarmVolume()

        val pattern = longArrayOf(0, 600, 300, 600)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            vibrator?.vibrate(VibrationEffect.createWaveform(pattern, 0))
        }

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
            .setContentText(if (isTestMode) "Mode Uji Coba Alarm Aktif" else "Selesaikan 5 soal matematika SMA!")
            .setPriority(NotificationCompat.PRIORITY_MAX)
            .setCategory(NotificationCompat.CATEGORY_ALARM)
            .setOngoing(true)
            .setFullScreenIntent(fullScreenPendingIntent, true)
            .build()

        startForeground(NOTIFICATION_ID, notification)
        startActivity(fullScreenIntent)

        // 1. Putar Ringtone Alarm Sistem sebagai lapisan suara dasar
        runCatching {
            val alarmUri = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_ALARM)
                ?: RingtoneManager.getDefaultUri(RingtoneManager.TYPE_RINGTONE)
            ringtone = RingtoneManager.getRingtone(this, alarmUri)?.apply {
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
                    isLooping = true
                    volume = 0.65f
                }
                audioAttributes = AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_ALARM).build()
                play()
            }
        }

        // 2. Putar Voice Over YouTube (wake_up_speech.mp3)
        val rawResId = resources.getIdentifier("wake_up_speech", "raw", packageName)
        if (rawResId != 0) {
            try {
                mediaPlayer = MediaPlayer().apply {
                    setAudioAttributes(AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_ALARM).build())
                    val afd = resources.openRawResourceFd(rawResId)
                    setDataSource(afd.fileDescriptor, afd.startOffset, afd.length)
                    afd.close()
                    isLooping = true
                    setVolume(1.0f, 1.0f)
                    prepare()
                    start()
                }
            } catch (e: Exception) {
                tts = TextToSpeech(this, this)
            }
        } else {
            tts = TextToSpeech(this, this)
        }

        // Siapkan TTS juga untuk pengumuman perayaan saat misi selesai
        if (tts == null) {
            tts = TextToSpeech(this, this)
        }

        handler.post(enforcementRunnable)
        return START_STICKY
    }

    private fun triggerCelebrationAudio() {
        isCelebrating = true
        isAlarmRinging = false
        handler.removeCallbacks(enforcementRunnable)

        // Matikan semua suara alarm & getaran seketika
        runCatching { mediaPlayer?.stop(); mediaPlayer?.release() }
        mediaPlayer = null
        runCatching { ringtone?.stop() }
        ringtone = null
        vibrator?.cancel()

        // Mainkan nada perayaan / fanfare menang!
        runCatching {
            val notifUri = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION)
            RingtoneManager.getRingtone(this, notifUri)?.play()
        }
        handler.postDelayed({
            runCatching { toneGenerator?.startTone(ToneGenerator.TONE_PROP_ACK, 300) }
        }, 250L)
        handler.postDelayed({
            runCatching { toneGenerator?.startTone(ToneGenerator.TONE_PROP_BEEP2, 500) }
        }, 600L)

        // Suara pujian kemenangan ("SURPRISE! GREAT JOB!")
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
            tts?.setPitch(0.85f)
            tts?.setSpeechRate(1.1f)
            isTtsReady = true
            if (isAlarmRinging && mediaPlayer == null && !isCelebrating) {
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
        isCelebrating = false
        isTestMode = false
        handler.removeCallbacks(enforcementRunnable)
        runCatching { mediaPlayer?.stop(); mediaPlayer?.release() }
        runCatching { ringtone?.stop() }
        runCatching { toneGenerator?.release() }
        runCatching { tts?.stop(); tts?.shutdown() }
        vibrator?.cancel()
        super.onDestroy()
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
""",

    "app/src/main/java/com/example/ironwake/AlarmRingingActivity.kt": """package com.example.ironwake

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
                    onExitTestMode = {
                        exitAlarmCompletely()
                    },
                    onAllMissionsCompleted = {
                        missionCompleted = true
                        val celebrateIntent = Intent(this, AlarmService::class.java).apply {
                            action = AlarmService.ACTION_CELEBRATE
                        }
                        startService(celebrateIntent)
                    },
                    onFinishCelebration = {
                        exitAlarmCompletely()
                    }
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

    "app/src/main/java/com/example/ironwake/ui/screens/RingingScreen.kt": """package com.example.ironwake.ui.screens

import androidx.compose.foundation.*
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.EmojiEvents
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
import kotlin.random.Random

@Composable
fun RingingScreen(
    motivationText: String,
    enabledTopics: Set<MathTopic>,
    difficulty: Difficulty,
    isTestMode: Boolean,
    onExitTestMode: () -> Unit,
    onAllMissionsCompleted: () -> Unit,
    onFinishCelebration: () -> Unit
) {
    var currentStep by remember { mutableIntStateOf(1) }
    var currentProblem by remember { mutableStateOf(MathGenerator.generateProblem(enabledTopics, difficulty)) }
    var userAnswer by remember { mutableStateOf("") }
    var errorMessage by remember { mutableStateOf<String?>(null) }
    var isCelebrating by remember { mutableStateOf(false) }

    fun verifyAnswer() {
        val parsed = userAnswer.trim().toIntOrNull()
        if (parsed == null) {
            errorMessage = "Masukkan angka bulat!"
            return
        }
        if (parsed == currentProblem.correctAnswer) {
            errorMessage = null
            userAnswer = ""
            if (currentStep >= 5) {
                isCelebrating = true
                onAllMissionsCompleted()
            } else {
                currentStep++
                currentProblem = MathGenerator.generateProblem(enabledTopics, difficulty)
            }
        } else {
            errorMessage = "SALAH! Coba hitung lagi!"
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
                        if (isCelebrating) listOf(Color(0xD90A1F12), Color(0xCC0D0D0D), Color(0xE60A1F12))
                        else listOf(Color.Black.copy(0.78f), Color.Black.copy(0.55f), Color.Black.copy(0.88f))
                    )
                )
        )

        if (isCelebrating) {
            // Efek konfeti emas & hijau di latar perayaan
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
                    text = "Semua 5 soal matematika SMA berhasil ditaklukkan. Otakmu sudah 100% aktif dan siap menjalani hari!",
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
        } else {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(20.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.SpaceBetween
            ) {
                Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.fillMaxWidth()) {
                    if (isTestMode) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.End
                        ) {
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

                    Spacer(Modifier.height(8.dp))
                    Text(
                        text = motivationText.uppercase(),
                        color = IronGold,
                        fontSize = 28.sp,
                        fontWeight = FontWeight.Black,
                        textAlign = TextAlign.Center,
                        lineHeight = 34.sp
                    )
                    Spacer(Modifier.height(12.dp))
                    Surface(
                        color = IronRed,
                        shape = RoundedCornerShape(50),
                        modifier = Modifier.border(1.5.dp, IronGold, RoundedCornerShape(50))
                    ) {
                        Text(
                            text = "MISI DISIPLIN: $currentStep / 5",
                            color = Color.White,
                            fontWeight = FontWeight.ExtraBold,
                            fontSize = 15.sp,
                            modifier = Modifier.padding(horizontal = 20.dp, vertical = 6.dp)
                        )
                    }
                }

                Card(
                    colors = CardDefaults.cardColors(containerColor = Color(0xE6141418)),
                    shape = RoundedCornerShape(16.dp),
                    modifier = Modifier
                        .fillMaxWidth()
                        .border(2.dp, IronRed, RoundedCornerShape(16.dp))
                ) {
                    Column(
                        modifier = Modifier.padding(20.dp),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Text(
                            text = currentProblem.topic.displayName.uppercase(),
                            color = IronGold,
                            fontSize = 12.sp,
                            fontWeight = FontWeight.Bold
                        )
                        Spacer(Modifier.height(12.dp))
                        Text(
                            text = currentProblem.question,
                            color = Color.White,
                            fontSize = 19.sp,
                            fontWeight = FontWeight.Bold,
                            textAlign = TextAlign.Center,
                            lineHeight = 26.sp
                        )
                        Spacer(Modifier.height(8.dp))
                        Text(
                            text = "Petunjuk: ${currentProblem.hint}",
                            color = Color.LightGray,
                            fontSize = 12.sp,
                            textAlign = TextAlign.Center
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
                                focusedBorderColor = IronGold,
                                unfocusedBorderColor = IronRed,
                                focusedTextColor = Color.White,
                                unfocusedTextColor = Color.White,
                                focusedLabelColor = IronGold
                            ),
                            modifier = Modifier.fillMaxWidth()
                        )
                        if (errorMessage != null) {
                            Spacer(Modifier.height(8.dp))
                            Text(
                                text = errorMessage!!,
                                color = IronCrimson,
                                fontWeight = FontWeight.Bold,
                                fontSize = 14.sp
                            )
                        }
                        Spacer(Modifier.height(16.dp))
                        Button(
                            onClick = { verifyAnswer() },
                            colors = ButtonDefaults.buttonColors(containerColor = IronRed),
                            shape = RoundedCornerShape(10.dp),
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(52.dp)
                        ) {
                            Text(
                                text = if (currentStep < 5) "KUNCI JAWABAN ($currentStep/5)" else "MATIKAN ALARM SEKARANG!",
                                color = Color.White,
                                fontWeight = FontWeight.Black,
                                fontSize = 16.sp
                            )
                        }
                    }
                }

                Text(
                    text = if (isTestMode) "MODE UJI COBA: Ketuk tombol kuning di kanan atas untuk keluar." else "NO MUTE. NO SNOOZE. SELESAIKAN 5 SOAL.",
                    color = Color.White.copy(0.75f),
                    fontSize = 11.sp,
                    fontWeight = FontWeight.Bold,
                    textAlign = TextAlign.Center
                )
            }
        }
    }
}
""",

    "app/src/main/java/com/example/ironwake/ui/screens/HomeScreen.kt": """package com.example.ironwake.ui.screens

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
            Text("MODIFIKASI MISI", color = Color.Black, fontWeight = FontWeight.Black, fontSize = 16.sp)
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
            title = { Text("MODIFIKASI MISI DISIPLIN", color = IronGold, fontWeight = FontWeight.Black) },
            text = {
                Column(modifier = Modifier.verticalScroll(rememberScrollState())) {
                    Text("Teks Teriakan Alarm:", color = Color.White, fontWeight = FontWeight.Bold)
                    OutlinedTextField(value = motivationText, onValueChange = { motivationText = it }, singleLine = true, modifier = Modifier.fillMaxWidth())
                    Spacer(Modifier.height(12.dp))
                    Text("Tingkat Kesulitan:", color = Color.White, fontWeight = FontWeight.Bold)
                    Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        Difficulty.entries.forEach { diff -> FilterChip(selected = difficulty == diff, onClick = { difficulty = diff }, label = { Text(diff.label) }) }
                    }
                    Spacer(Modifier.height(12.dp))
                    Text("Pilih Materi SMA:", color = Color.White, fontWeight = FontWeight.Bold)
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
                            Text(topic.displayName, color = Color.White, fontSize = 14.sp)
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

    "app/src/main/java/com/example/ironwake/MainActivity.kt": """package com.example.ironwake

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
print("Semua file proyek IronWake v2.0 berhasil dibuat!")
