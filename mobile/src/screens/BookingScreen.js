import React from 'react';
import { View, Text, Button } from 'react-native';

export default function BookingScreen({ navigation }) {
  return (
    <View style={{ padding: 16, gap: 10 }}>
      <Text style={{ fontSize: 24 }}>Booking</Text>
      <Text>Select slot and confirm appointment.</Text>
      <Button title="Proceed to Payment" onPress={() => navigation.navigate('Payment')} />
    </View>
  );
}
