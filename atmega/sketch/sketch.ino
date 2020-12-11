#include <SD.h>


typedef struct color {
unsigned char r = 0;
unsigned char g = 0;
unsigned char b = 0;
} color;

color theme_primary = (188, 46, 60);
color theme_secondary = (76, 73, 158);
color theme_tertiary = (83, 84, 92);
color theme_bg = (134, 135, 141);

theme_primary_user = theme_primary;
theme_secondary_user = theme_secondary;
theme_tertiary_user = theme_tertiary;
theme_bg_user = theme_bg;

unsigned int rate = 60;
unsigned int volume = 25;
unsigned char passcode_stored[4] = {1,1,1,1};
unsigned char passcode_entered[4] = {1,1,1,1};
unsigned char passcode_current_index = 0;

void enterState(uint state) {
  if (state == MenuState.boot) boot();
  if (state == MenuState.locked) locked();
  if (state == Menustate.unlock) unlock();
  if (state == Menustate.main_menu) menu();
  if (state == MenuState.feed) feed();
  if (state == MenuState.settings) settings();
  if (state == MenuState.feed_in_progress) transfuse();
  if (state == MenuState.colors) colors();
  if (state == MenuState.change_pin) change_pin();
  if (state == MenuState.rate) rate();
  if (state == MenuState.rate_low) rate_low();
  if (state == Menustate.rate_mid) rate_mid();
  if (state == MenuState.rate_high) rate_high();
  if (state == MenuState.volume) volume();
  if (state == Menustate.volume_bottom) volume_bottom();
  if (state == Menustate.volume_top) volume_top();
  if (state == Menustate.transfuse_paused) transfuse_pause();
  if (state == menustate.transfuse) transfuse();
  if (state == Menustate.color_confirm) color_confirm();
  if (state == MenuState.change_pin_auth) change_pin_auth();
  if (state == MenuState.change_pin_entry) change_pin_entry();
  if (state == MenuState.change_pin_verify) change_pin_verify();
  if (state == MenuState.alert_battery) alert_battery();
  if (state == MenuState.alert_clog_empty) alert_clog_empty();
  if (state == MenuState.alert_tube_disconnect) alert_tube_disconnect();
  if (state == MenuState.alert_cart_disconnect) alert_clog_disconnect();
}

void boot() {
  
}

void
enum UIState {
    boot = 0,
    locked = 1,
    unlock = 2,
    menu_main = 3,
    feed = 4,
    settings = 5,
    feed_in_progress = 6,
    colors = 7,
    change_pin = 8,
    rate = 9,
    rate_low = 10,
    rate_mid = 11,
    rate_high = 12,
    volume = 13,
    volume_bottom = 14,
    volume_top = 15,
    transfuse_paused = 16,
    transfuse = 17,
    color_confirm = 18,
    change_pin_auth = 19,
    change_pin_entry = 20,
    change_pin_verify = 21,
    alert_battery = 22,
    alert_clog_empty = 23,
    alert_tube_disconnect = 24,
    alert_cart_disconnect = 25
} MenuState;



typedef unsigned int uint;
uint state = MenuState.locked;


struct assets 
{
        String locked = "locked.png";
        String unlock = "unlock.png";
        String palette = "palette.png";
        String menu = "main_menu.png";
        String feed = "feed.png";
        String settings = "settings.png";
        String rate = "rate.png";
        String rate_low = "rate_low.png";
        String rate_mid = "rate_mid.png";
        String rate_top = "rate_top.png";
        String volume = "volume.png";
        String volume_bottom = "volume_bottom.png";
        String volume_top = "volume_top.png";
        String color = "color.png";
        String transfuse_play = "transfuse_play.png";
        String screen_transfuse_paused.png";
        String color_confirm = "color_confirm.png";
        String color_changepinauth = "changepinauth.png";
        String changepin = "changepin.png";
        String verifypin = "verifypin.png";
        String alert_battery = "alert_battery-01.png";
        String alert_tube = "alert_tube_disc-01.png";
        String alert_cart = "alert_cart_disc-01.png";
        String alert_clog = "screen_alert_clog_empty-01.png";
}


bool one = false;
bool two = false;
bool three = false;
bool four = false;
bool five = false;

void locked() {
  passcode_current_index = 0; 
  while(1) {
    display(locked);
    unlock();

    

    /* Button Event Handlers */
    if (one) {
        
    }
    elif (two) {
        
    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {
      
    }
  }
}
void unlock() {
  while(1) {
    display(unlock);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void menu() {
  while(1) {
    display(menu);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void feed() {
  while(1) {
    display(feed);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void settings() {
  while(1) {
    display(settings);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void transfuse() {
  while(1) {
    display(transfuse_play);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void colors() {
  while(1) {
    display(color);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void change_pin() {
  while(1) {
    display(changepin);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void rate() {
  while(1) {
    display(rate);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void rate_low() {
  while(1) {
    display(rate_low);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void rate_mid() {
  while(1) {
    display(rate_mid);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void rate_high() {
  while(1) {
    display(rate_high);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void volume() {
  while(1) {
    display(volume);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void volume_bottom() {
  while(1) {
    display(volume_bottom);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void volume_top() {
  while(1) {
    display("");

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void transfuse_pause() {
  while(1) {
    display(transfuse_paused);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void transfuse() {
  while(1) {
    display("");

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void color_confirm() {
  while(1) {
    display(color_confirm);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void change_pin_auth() {
  while(1) {
    display(change_pin_auth);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void change_pin_entry() {
  while(1) {
    display(change_pin);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void change_pin_verify() {
  while(1) {
    display(verifypin);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void alert_battery() {
  while(1) {
    display(alert_battery);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void alert_clog_empty() {
  while(1) {
    display(alert_clog);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void alert_tube_disconnect() {
  while(1) {
    display(alert_tube);

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}
void alert_cart_disconnect() {
  while(1) {
    display(alert_cart );

    /* Button Event Handlers */
    if (one) {

    }
    elif (two) {

    }
    elif (three) {

    }
    elif (four) {

    }
    elif (five) {

    }
  }
}


void setup() {
  // put your setup code here, to run once:
  cli();//stop interrupts

//set timer0 interrupt at 2kHz
  TCCR0A = 0;// set entire TCCR2A register to 0
  TCCR0B = 0;// same for TCCR2B
  TCNT0  = 0;//initialize counter value to 0
  // set compare match register for 2khz increments
  OCR0A = 124;// = (16*10^6) / (2000*64) - 1 (must be <256)
  // turn on CTC mode
  TCCR0A |= (1 << WGM01);
  // Set CS01 and CS00 bits for 64 prescaler
  TCCR0B |= (1 << CS01) | (1 << CS00);   
  // enable timer compare interrupt
  TIMSK0 |= (1 << OCIE0A);

//set timer1 interrupt at 1Hz
  TCCR1A = 0;// set entire TCCR1A register to 0
  TCCR1B = 0;// same for TCCR1B
  TCNT1  = 0;//initialize counter value to 0
  // set compare match register for 1hz increments
  OCR1A = 15624;// = (16*10^6) / (1*1024) - 1 (must be <65536)
  // turn on CTC mode
  TCCR1B |= (1 << WGM12);
  // Set CS12 and CS10 bits for 1024 prescaler
  TCCR1B |= (1 << CS12) | (1 << CS10);  
  // enable timer compare interrupt
  TIMSK1 |= (1 << OCIE1A);

//set timer2 interrupt at 8kHz
  TCCR2A = 0;// set entire TCCR2A register to 0
  TCCR2B = 0;// same for TCCR2B
  TCNT2  = 0;//initialize counter value to 0
  // set compare match register for 8khz increments
  OCR2A = 249;// = (16*10^6) / (8000*8) - 1 (must be <256)
  // turn on CTC mode
  TCCR2A |= (1 << WGM21);
  // Set CS21 bit for 8 prescaler
  TCCR2B |= (1 << CS21);   
  // enable timer compare interrupt
  TIMSK2 |= (1 << OCIE2A);


sei();//allow interrupts

}//end setup


}

void loop() {
  // put your main code here, to run repeatedly:

}