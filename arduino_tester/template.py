template_frame = '''
/*
 Welcome to arduino test generator
*/
{defines}

// the setup function runs once when you press reset or power the board
void setup() 
{t}  
  {pin_mode}
{p}

// the loop function runs over and over again forever
void loop()
{t}
  {logic}
{p}
'''

template_pinmode = '''
    pinMode({pin_number}, {in_out});'''

template_digital ='''
    digitalWrite({pin_number}, {set_high_or_low});'''
template_delay ='''
    delay({delay});'''
