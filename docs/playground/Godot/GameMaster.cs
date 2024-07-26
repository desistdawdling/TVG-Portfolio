using Godot;
using System;

public partial class GameMaster : Node {

    public static string gameVersion = "game versioning system";
    
    public static PlayerData playerData = new PlayerData();

    public static GameData gameData = new GameData();


    public override void _Ready() {
        string jsonString = Newtonsoft.Json.JsonConvert.SerializedObject(playerData);

        playerData.init();
    }


public override void _Process(double delta){}

}