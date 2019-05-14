package aramburo.ariel.msgsender

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.telephony.SmsManager
import kotlinx.android.synthetic.main.activity_main.*
import android.widget.Toast
import android.widget.EditText


class MainActivity : AppCompatActivity() {
    private lateinit var txtMobile: EditText
    private lateinit var txtMessage: EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        txtMobile = findViewById(R.id.mblTxt)
        txtMessage = findViewById(R.id.msgTxt)
        btnSend.setOnClickListener {
            try {
                val smgr = SmsManager.getDefault()
                smgr.sendTextMessage(txtMobile.getText().toString(), null, txtMessage.getText().toString(), null, null)
                Toast.makeText(this@MainActivity, "SMS Enviado", Toast.LENGTH_SHORT).show()
            } catch (e: Exception) {
                Toast.makeText(this@MainActivity, "Fallo en envío, intente de nuevo", Toast.LENGTH_SHORT).show()
            }

        }
    }
}
