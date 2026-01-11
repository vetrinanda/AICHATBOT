import "./Sidebar.css";
import { assets } from "../../assets/assets";
import { useState } from "react";
import {
  Menu,
  Plus,
  MessageSquare,
  CircleQuestionMark,
  SquareActivity,
  Settings,
} from "lucide-react";

import React from "react";

const Sidebar = () => {
  const [extended, setExtended] = useState(false);
  return (
    <div className="sidebar">
      <div className="top">
        {/* <img className="menu" src={assets.menu_icon} alt="menu" /> */}
        <Menu onClick={() => setExtended(!extended)} className="menu" strokeWidth={2.5} />
        <div className="new-chat">
          {/* <img className="plus" src={assets.plus_icon} alt="plus" /> */}
          <Plus strokeWidth={2.5} />
          {extended ? <p>New Chat</p> : null}
        </div>
        {extended ? (
          <div className="recent">
            <p className="recent-title">Recent</p>
            <div className="recent-entry">
              {/* <img src={assets.message_icon} alt="" /> */}
              <MessageSquare size={20} strokeWidth={1.75} />
              <p>What is React...</p>
            </div>
          </div>
        ) : null}
      </div>
      <div className="bottom">
        <div className="bottom-item recent-entry">
          {/* <img src={assets.question_icon} alt="settings" /> */}
          <CircleQuestionMark strokeWidth={1.25} />
          {extended ? <p>Help</p> : null}
        </div>
        <div className="bottom-item recent-entry">
          {/* <img src={assets.history_icon} alt="settings" /> */}
          <SquareActivity strokeWidth={1.25} />
          {extended ? <p>Activity</p> : null}
        </div>
        <div className="bottom-item recent-entry">
          {/* <img src={assets.setting_icon} alt="settings" /> */}
          <Settings strokeWidth={1.25} />
          {extended ? <p>Settings</p> : null}
        </div>
      </div> 
    </div>
  );
};

export default Sidebar;
