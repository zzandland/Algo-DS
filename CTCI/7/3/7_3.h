#ifndef HEADER_H
#define HEADER_H

#include <iostream>
#include <map>
#include <set>
#include <vector>

class Artist;
class Music;

struct Date {
  int year_;
  int month_;
  int day_;
};

class Album {
 public:
  Album(std::string title, std::vector<Artist*> artists, Date released_date);

  Album(std::string title, Artist artist, Date released_date);

  virtual ~Album();

  void AddMusic(Music* music);

  std::vector<Music*> GetMusic();

  std::string GetTitle();

  int GetReleasedYear();

 private:
  static int n_albums_;
  int id_;
  std::string title_;
  std::vector<Artist*> artists_;
  Date released_date_;
  std::vector<Music*> musics_;
};


class Artist {
 public:
  Artist(std::string first_name, std::string last_name, Date dob,
         std::map<int, std::vector<Album*>> albums);

  virtual ~Artist();

  void AddAlbum(Album* album);

  std::vector<Album*> GetAllAlbums();

  std::string GetFirstName();

  std::string GetLastName();

 private:
  static int n_artists_;
  int id_;
  std::string first_name_;
  std::string last_name_;
  Date dob_;
  std::map<int, std::vector<Album*>> albums_;
};

class Music {
 public:
  Music(std::string title, std::vector<Artist*> artists, int track_id,
        int duration, std::string genre, Date released_date);

  Music(std::string title, Artist artist, int track_id, int duration,
        std::string genre, Date released_date);

  std::string GetTitle();

  int GetDuration();

  int GetTrackId();

  int GetReleasedYear();

  void SetAlbum(Album* album);

 private:
  static int n_musics_;
  int id_;
  int track_id_;
  int duration_;
  std::string title_;
  std::vector<Artist*> artists_;
  std::string genre_;
  Album* album_;
  Date released_date_;
};

class Jukebox {
 public:
  virtual ~Jukebox();

  void AddArtist(Artist* artist);

  void GetMusicByArtist(std::string artist);

 private:
  std::map<char, std::set<Music*>> musics_;
  std::map<char, std::set<Album*>> albums_;
  std::map<char, std::set<Artist*>> artists_;
};

#endif /* HEADER_H */
