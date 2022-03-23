import React from 'react';
import { Card, Header } from 'react-native-elements';
import { Text, View, StyleSheet, Image } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
//import { Text } from './Text';

const ResultPanel = (props, { navigation }) => {
    return (
        
            <Card containerStyle={{
                width: '95%', backgroundColor: 'white',
                borderWidth: 0,
                shadowColor: 'white',
                justifyContent: 'center'

            }}
            >
                <Card.Title style={styles.cardTitle}>{props.data['title']}</Card.Title>
                <Card.Divider />
                <View style={styles.imgContainer}>
                    {
                        props.data['uri'].map((pic, index) => {
                            return (
                                <Image
                                    key={index}
                                    source={{ uri: pic }}
                                    style={styles.img}
                                />
                            );
                        })
                    }
                </View>
            </Card>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    cardTitle: {
        textAlign: 'left',
        fontFamily: 'Montserrat-Bold',
        fontSize: 17
    },
    img: {
        width: 50,
        height: 50,
        margin: 4
    },
    imgContainer: {
        flexDirection: 'row',
        flexWrap: 'wrap'
    },
   
});

export default ResultPanel;