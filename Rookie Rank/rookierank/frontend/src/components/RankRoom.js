import React, { useState } from "react";
import { useParams } from "react-router-dom";


export default function RankRoom(props) {

    let [numberOfPlayers,setNumberOfPlayers] = useState(3);
    let [choosePlayers,setChoosePlayers] = useState(true);
    let [isHost,setIsHost] = useState(false);
    const {roomName} = useParams();


    return <div>
        <h3>{roomName}</h3>
        <p>Number Of Players: {numberOfPlayers}</p>
        <p>choosePlayers: {choosePlayers}</p>
        <p>Host: {isHost}</p>
    </div>

}



// export default class RankRoom extends Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             numberOfPlayers: 3,
//             choosePlayers: true,
//             isHost: false,
//         }
//         this.roomName = this.props.match.params.roomName;
//     }

//     render () {
//         return <div>
//             <h3>{this.roomName}</h3>
//             <p>Votes: {this.state.numberOfPlayers}</p>
//             <p>choosePlayers: {this.state.choosePlayers}</p>
//             <p>Host: {this.state.isHost}</p>
//         </div>
//     }
// }