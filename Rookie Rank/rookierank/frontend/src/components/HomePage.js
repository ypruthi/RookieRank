import React, { Component } from "react";
import JoinRankRoomPage from "./JoinRankRoomPage";
import CreateRankRoomPage from "./CreateRankRoomPage"; 
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import RankRoom from "./RankRoom";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
          <Router>
            <Routes>
              <Route path="/" element={<p>This is the home page</p>} />
              <Route path="/joinrankroom" element={<JoinRankRoomPage />} />
              <Route path="/create" element={<CreateRankRoomPage />} />
              <Route path="/room/:roomName" element={<RankRoom />} />
            </Routes>
          </Router>
        );
      }
    }