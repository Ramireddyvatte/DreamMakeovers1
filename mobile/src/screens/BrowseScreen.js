import React from 'react';
import { View, Text, Button } from 'react-native';

export default function BrowseScreen({ navigation }) {
  return (
    <View style={{ padding: 16, gap: 10 }}>
      <Text style={{ fontSize: 24 }}>Browse Beauticians</Text>
      <Text>Find certified professionals near you.</Text>
      <Button title="Book Now" onPress={() => navigation.navigate('Booking')} />
    </View>
  );
}
