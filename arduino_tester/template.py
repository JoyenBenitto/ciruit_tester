template_frame = '''
/*
 Welcome to arduino test generator
*/
{defines}

// the setup function runs once when you press reset or power the board
void setup() {
  pinMode({pin_number}, OUTPUT);
}

// the loop function runs over and over again forever
void loop(){
  {logic}
}
'''

template_digital ='''
digitalWrite({pin_number}, {set_high_or_low});
'''
template_delay ='''
delay({delay});
'''
