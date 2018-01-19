{-# LANGUAGE FlexibleContexts          #-}
{-# LANGUAGE NoMonomorphismRestriction #-}
{-# LANGUAGE TypeFamilies              #-}

import           Diagrams.Backend.Rasterific.CmdLine
import           Diagrams.Prelude

import           Control.Monad
import           Data.Maybe

import           System.Directory
import           System.Environment
import           System.FilePath

import qualified Data.Map                            as M

main :: IO ()
main = mainWith renderWorld

renderWorld :: FilePath -> IO (Diagram B)
renderWorld worldFile = do
  tileMap     <- loadTiles
  world       <- lines <$> readFile worldFile
  return . lw veryThin
         . cat' unitY (with & catMethod .~ Distrib & sep .~ 40)
         . reverse
         . map (hcat . map (alignB . getTile tileMap)) $ world

getTile :: M.Map Char (Diagram B) -> Char -> Diagram B
getTile m c = fromMaybe (square 40 # fc white) $ M.lookup c m

loadTiles :: IO (M.Map Char (Diagram B))
loadTiles = do
  tiles <- listDirectory "tiles"
  m <- forM tiles $ \tileFile -> do
    let (c:_) = takeBaseName tileFile
    Right dimg <- loadImageEmb ("tiles" </> tileFile)
    return (c, image dimg)
  return $ M.fromList m
